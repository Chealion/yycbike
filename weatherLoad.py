#! /usr/bin/python
# :set tabstop=4 shiftwidth=4 expandtab

# Downoads Environment Canada data and sends the data to Graphite. Additionally logs the data to a file we can use to import later

import csv
import time
import graphitesend
import urllib2
from datetime import date, timedelta
import datetime

graphitesend.init(graphite_server='localhost',prefix='yycbike',system_name='')
metriclog = open('/home/ubuntu/devmetriclog.log', 'a')

# Watch out for timezones - this script fails to function past 5 PM MST.

yesterday = date.today() - timedelta(1)
year = yesterday.strftime('%Y')
month = yesterday.strftime('%m')
day = yesterday.strftime('%d')

#Installations

# URLs per ftp://ftp.tor.ec.gc.ca/Pub/Get_More_Data_Plus_de_donnees/Readme.txt

HOURLY_URL='http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=50430&Year=' + year + '&Month=' + month + '&Day=' + day + '&submit=Download+Data&timeframe=1'
DAILY_URL= 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=50430&Year=' + year + '&Month=' + month + '&Day=' + day + '&submit=Download+Data&timeframe=2'

## HOURLY

url = HOURLY_URL
print 'Loading Hourly Weather Data...'
response = urllib2.urlopen(url)
csv_data = response.read()

# Delete first 17 lines - up to and inlcuding header line
cleaned_data = '\n'.join(csv_data.split('\n')[17:]) 
# split into list, and use non unicode field names
csv_reader = csv.DictReader(cleaned_data.split('\n'), fieldnames=['Date', 'Year', 'Month', 'Day', 'Time', 'Quality', 'Temp', 'TempFlag', 'DewPoint', 'DewPointFlag', 'Humidity', 'HumFlag', 'WindDir', 'WindFlag', 'WindSpd', 'WindFlg', 'Visbility', 'VisFlag', 'Pressure', 'PressFlag', 'Humidex', 'HmdxFlag', 'WindChill', 'WindChillFlag', 'Weather'])

for row in csv_reader:
    #Create timestamp
    timestamp = time.mktime(datetime.datetime.strptime(row['Date'], "%Y-%m-%d %H:%M").timetuple())
    yesterday_timestamp = float(yesterday.strftime('%s'))

    #Ignore any data "newer" than yesterday. Data that doesn't exist yet.
    if timestamp > yesterday_timestamp:
        break
    else:
        timestamp = str(int(timestamp))
        #print row

        # Data Cleaning - Wind Chill or Humidex - merge
        if row['Temp'] is None or row['Temp'] == '':
            continue

        if row['Humidex'] == '' and row['WindChill'] == '':
            feelslike = row['Temp']
        elif row['Humidex'] == '':
            feelslike = row['WindChill']
        else:
            feelslike = row['Humidex']

        if row['WindSpd'] == '':
            row['WindSpd'] = 0

        if row['WindDir'] == '':
            row['WindDir'] = 0

        metric_string = 'weather.hourly.temp ' + str(row['Temp']) + ' ' + timestamp
        metriclog.write(metric_string + "\n")
        graphitesend.send('weather.hourly.temp', str(row['Temp']), timestamp)

        metric_string = 'weather.hourly.windspeed ' + str(row['WindSpd']) + ' ' + timestamp
        metriclog.write(metric_string + "\n")
        graphitesend.send('weather.hourly.windspeed', str(row['WindSpd']), timestamp)

        metric_string = 'weather.hourly.winddir ' + str(row['WindDir']) + ' ' + timestamp
        metriclog.write(metric_string + "\n")
        graphitesend.send('weather.hourly.winddir', str(row['WindDir']), timestamp)

        metric_string = 'weather.hourly.humidity ' + str(row['Humidity']) + ' ' + timestamp
        metriclog.write(metric_string + "\n")
        graphitesend.send('weather.hourly.humidity', str(row['Humidity']), timestamp)

        metric_string = 'weather.hourly.feelslike ' + str(feelslike) + ' ' + timestamp
        metriclog.write(metric_string + "\n")
        graphitesend.send('weather.hourly.feelslike', str(feelslike), timestamp)

## DAILY
url = DAILY_URL
print 'Loading Daily Weather Data...'
response = urllib2.urlopen(url)
csv_data = response.read()

# Delete first 26 lines - up to and including header line
cleaned_data = '\n'.join(csv_data.split('\n')[26:]) 
# split into list, and use non unicode field names
csv_reader = csv.DictReader(cleaned_data.split('\n'), fieldnames=['Date', 'Year', 'Month', 'Day', 'Quality', 'Max', 'MaxFlag', 'Min', 'MinFlag', 'Mean', 'MeanFlag', 'Heat1', 'Heat2', 'Heat3', 'Heat4', 'Rain', 'RainFlag', 'Snow', 'SnowFlag', 'TotalPrecip', 'PrecipFlag', 'SnowonGround', 'SnowFlag', 'Wind1', 'Wind2', 'Wind3', 'Wind4'])

for row in csv_reader:
    #Create timestamp
    timestamp = time.mktime(datetime.datetime.strptime(row['Date'], "%Y-%m-%d").timetuple())
    yesterday_timestamp = float(yesterday.strftime('%s'))

    #Ignore any data "newer" than yesterday. Data that doesn't exist yet.
    if timestamp > yesterday_timestamp:
        break
    else:
        timestamp = str(int(timestamp))
        #print row

        if row['Max'] is None or row['Max'] == '' or row['Min'] == '':
            continue

        metric_string = 'weather.daily.high ' + str(row['Max']) + ' ' + timestamp
        metriclog.write(metric_string + "\n")
        graphitesend.send('weather.daily.high', str(row['Max']), timestamp)

        metric_string = 'weather.daily.low ' + str(row['Min']) + ' ' + timestamp
        metriclog.write(metric_string + "\n")
        graphitesend.send('weather.daily.low', str(row['Min']), timestamp)
        
        metric_string = 'weather.daily.mean ' + str(row['Mean']) + ' ' + timestamp
        metriclog.write(metric_string + "\n")
        graphitesend.send('weather.daily.mean', str(row['Mean']), timestamp)

        # Data Cleaning
        if row['TotalPrecip'] == '':
            row['TotalPrecip'] = 0

        metric_string = 'weather.daily.precip ' + str(row['TotalPrecip']) + ' ' + timestamp
        metriclog.write(metric_string + "\n")
        graphitesend.send('weather.daily.precip', str(row['TotalPrecip']), timestamp)

        # Data Cleaning
        if row['SnowonGround'] == '':
            row['SnowonGround'] = 0

        metric_string = 'weather.daily.snowamt ' + str(row['SnowonGround']) + ' ' + timestamp
        metriclog.write(metric_string + "\n")
        graphitesend.send('weather.daily.snowamt', str(row['SnowonGround']), timestamp)


# OUTPUT FORMAT:
# <metric path> <metric value> <metric timestamp>
# yycbike.peacebridge.north.trips 5 123456789 

metriclog.close()

print 'Done.'

