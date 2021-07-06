#! /usr/bin/python
# :set tabstop=4 shiftwidth=4 expandtab

# monthlyArchive.py - downloads last month's raw data and places it in the archive folder for that month.
# Cron should run this on the ?th of the month. (How far back is Env. Canada?)

import json
import urllib2
from datetime import datetime, date, timedelta 
import os

# Manually set lastMonth (use last day) when running manually:
#lastMonth = date(2014,4,30)
lastMonth = (datetime.utcnow().replace(day=1) - timedelta(days=1))

directory='/home/ubuntu/archive/' + lastMonth.strftime("%Y-%m")
if not os.path.exists(directory):
        os.makedirs(directory)

# Get first and last day of last month
firstDay = lastMonth.replace(day=1)

# Download weather data snapshots.
# Hourly weather data is provided as an entire month's worth of values.
# Daily weather data is provided as an entire year's worth of values.

year = firstDay.strftime('%Y')
month = firstDay.strftime('%m')
day = firstDay.strftime('%d')

HOURLY_URL='http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=50430&Prov=AB&hlyRange=2012-07-09&7C' + year + '-' + month + '-' + day + '&Year=' + year + '&Month=' + month + '&Day=' + day + '&submit=Download+Data&timeframe=1'

DAILY_URL='http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=50430&Prov=AB&dlyRange=2012-07-0&7C' + year + '-' + month + '-' + day + '&Year=' + year + '&Month=' + month + '&Day=' + day + '&submit=Download+Data&timeframe=2'

print "Downloading hourly"
f = urllib2.urlopen(HOURLY_URL)
with open(directory + '/wx-hourly.txt', 'wb') as hourly_file:
    hourly_file.write(f.read())

print "Downloading monthly"
f = urllib2.urlopen(DAILY_URL)
with open(directory + '/wx-daily.txt', 'wb') as daily_file:
    daily_file.write(f.read())

#Installations
# Really need to rewrite this to be shared among scripts

# Peace Bridge
PB_NB={'installation':"peacebridge", 'direction':"north", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101018487/"}
PB_SB={'installation':"peacebridge", 'direction':"south", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102018487/"}

SEVEN_NB={'installation':"sevenst", 'direction':"north", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101017181/"}
SEVEN_SB={'installation':"sevenst", 'direction':"south", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102017181/"}

STEPHEN_CAR={'installation':"stephenave", 'direction':"car", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/103017165/"}
STEPHEN_BIKE={'installation':"stephenave", 'direction':"bike", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102017165"}
STEPHEN_PED={'installation':"stephenave", 'direction':"ped", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101017165"}

# Set dates
monthStart = firstDay.strftime("%Y%m%d")
monthEnd = lastMonth.strftime("%Y%m%d") 

for i in [ PB_NB, PB_SB, SEVEN_NB, SEVEN_SB, STEPHEN_CAR, STEPHEN_BIKE, STEPHEN_PED ]:
    # Specify yesterday to download
    url=i['url'] + "?begin=" + monthStart + "&end=" + monthEnd + "&step=2"
    print 'Loading ' + i['installation'] + ' ' + i['direction'] + '...'
    #print url
    f = urllib2.urlopen(url)
    with open(directory + '/' + i['installation'] + '-' + i['direction'] + '.txt', 'wb') as monthly_file:
        monthly_file.write(f.read())

print 'Done.'


