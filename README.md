# YYCBIKE Project

Collection of scripts and bits and bobs I used to create <URL TO GO HERE>.

## File Listing

### monthlyArchive.py

Save a monthly archive for reloading later

### statsLoad.py

Load the Eco Counter numbers into Graphite

### twitterBot.py

The script that runs the #yycbike_count Twitter feed. Runs once a day.

### weatherLoad.py

Load Environemnt Canada weather data into Graphite

## Thank You

Thanks to the City of Calgary and the team working on the project for making this data public. Thanks to those members of the public who pushed for this data to be made available. Awesome to have timely easy access to the data.

Apologies for just scraping the data and not asking permission.

## Notes

A couple things worth noting:

### Installation Start Dates

  * Peace Bridge: April 24, 2014
  * 7th St.: Decemeber 11, 2014
  * Stephen Ave: Oct. 23, 2014

### URLs

Environment Canada: Hourly data: http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=50430&Prov=AB&hlyRange=2012-07-09&7C2014-01-01&Year=2014&Month=1&Day=1&timeframe=1&submit=Download+Data

Gives full month's info of hourly data.

Daily data: http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=50430&Prov=AB&dlyRange=2012-07-97&7C2015-01-01&Year=2015&Month=1&Day=1&timeframe=2&submit=Download+Data

Gives full year's info of daily data. Appears to update much more quickly... 

EcoCounter: 

http://www.eco-public.com/api/h7q239dd/data/periode/[ID]/?begin=YYYYMMDD&endYYYYMMDD&step=[NUMBER]

IDs:

Peace Bridge (Total): 100018487
Peace Bridge (North): 101018487
Peace Bridge (South): 102018487

7th St (Total): 100018487
7th St (North): 101018487
7th St (South): 102018487

Stephen Ave (Bike): 102017165

### Metric Naming

Trips were yycbike.installation.direction/type

Weather:

yycbike.weather.daily.high
yycbike.weather.daily.low
yycbike.weather.daily.mean
yycbike.weather.daily.precip
yycbike.weather.daily.snowamt

yycbike.weather.hourly.temp
yycbike.weather.hourly.feels
yycbike.weather.hourly.windspeed
yycbike.weather.hourly.winddir
yycbike.weather.hourly.humidity
