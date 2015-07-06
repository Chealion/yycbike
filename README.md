# #yycbike Counter

Collection of scripts and bits and bobs I used to create [http://calgary.bike](http://calgary.bike) and the [yycbike_count](https://twitter.com/yycbike_count) Twitter bot.

The data is collected from the following sources:

  * [Environment Canada](http://climate.weather.gc.ca)
  * Public Eco-Counter Pages for individual counters.
    * [Peace Bridge](http://www.eco-public.com/public2/?id=100018487)
    * [7th St.](http://www.eco-public.com/public2/?id=100017181)
    * [Stephen Ave](http://eco-public.com/public2/?id=100020243)


## Thank You

Thanks to the City of Calgary and the team working on the project for making this data public. Thanks to those members of the public who pushed for this data to be made available. Awesome to have timely easy access to the data.

## Source Data Notes

Environment Canada's data is available as hourly readings (a month's worth), or as daily readings (a year's worth). I use Station 50430 (the Airport)

    Hourly Data:
    http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=50430&Prov=AB&hlyRange=2012-07-09&7C2014-01-01&Year=2014&Month=1&Day=1&timeframe=1&submit=Download+Data
    Daily Data:
    http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=50430&Prov=AB&dlyRange=2012-07-97&7C2015-01-01&Year=2015&Month=1&Day=1&timeframe=2&submit=Download+Data

Eco-Counter has a private API that can be figured out by reading the AJAX requests performed on each of the counter pages. The counts are posted once a day normally between 5:00 and 6:00 AM MST, so the counts are *not* live.

    Individual Data Sets:
    http://www.eco-public.com/api/h7q239dd/data/periode/[ID]/?begin=YYYYMMDD&endYYYYMMDD&step=[NUMBER]
    Data Set Names for Installation:
    http://www.eco-public.com/api/h7q239dd/counter/channels/[ID]

The step ID can be 2 (daily), 3 (hourly), or 4 (15 minute).

Installation Name |     ID    | Start Date
------------------|-----------|------------
*Peace Bridge*    | 100018487 | April 24, 2014
Northbound        | 101018487 | 
Southbound        | 102018487 | 
*Stephen Ave*     | 100020243 | October 23, 2014
Bikes             | 101020243 | 
Cars              | 102020243 |
*7th Street*      | 100017181 | December 11, 2014
Northbound        | 101017181 | 
Southbound        | 102017181 |

There is also one counter that is no longer public; the original Stephen Ave counter that was done with infrared cameras instead of in road sensors. Calgary.bike doesn't record any of this data.

Installation Name |     ID    | Start Date
*Stephen Ave OLD* | 100017165 | October 23, 2014
Pedestrian        | 101017165 |
Bikes             | 102017165 |
Cars              | 103017165 | 


## File Listing

### monthlyArchive.py

Save a monthly archive for reloading later

### statsLoad.py

Load the Eco Counter numbers into Graphite

### twitterBot.py

The script that runs the #yycbike_count Twitter feed. Runs once a day.

### weatherLoad.py

Load Environemnt Canada weather data into Graphite

### Metric Naming

Trips:
15 minute increments: yycbike.installation.direction.trips
Daily counts: yycbike.daily.installation.direction.trips

Weather Data recorded:

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
