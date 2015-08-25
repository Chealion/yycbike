# #yycbike Counter

Collection of scripts and bits and bobs I used to create [http://calgary.bike](http://calgary.bike) and the [yycbike_count](https://twitter.com/yycbike_count) Twitter bot.

The data is collected from the following sources:

  * [Environment Canada](http://climate.weather.gc.ca)
  * Public Eco-Counter Pages for individual counters.
    * [Calgary Bike Counter Page](http://www.eco-public.com/ParcPublic/?id=4190)
    * [Peace Bridge - Bikes and Pedestrians](http://www.eco-public.com/public2/?id=100018487)
    * [Stephen Ave](http://eco-public.com/public2/?id=100020207)
    * [7th St.](http://www.eco-public.com/public2/?id=100017181)
    * 5th St. - [North Leg](http://www.eco-public.com/public2/?id=100022540), [Under the Tracks](http://www.eco-public.com/public2/?id=100020095), [South Leg](http://www.eco-public.com/public2/?id=100022541)
    * 12th Ave. - [West Leg](http://www.eco-public.com/public2/?id=100022581), [Central Memorial](http://www.eco-public.com/public2/?id=100022580), [East Leg](http://www.eco-public.com/public2/?id=100022582)
    * 8th Ave. - [West Leg](http://www.eco-public.com/public2/?id=100024297), [Centre](http://www.eco-public.com/public2/?id=100024406)
    * 9th Ave. - [NMC](http://www.eco-public.com/public2/?id=100023675)

## Thank You

Thanks to the City of Calgary and the team working on the project for making this data public. Thanks to those members of the public who pushed for this data to be made available. Awesome to have timely easy access to the data.

## Source Data Notes

Environment Canada's data is available as hourly readings (a month's worth), or as daily readings (a year's worth). I use Station 50430 (the Airport)

    Hourly Data:
    http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=50430&Prov=AB&hlyRange=2012-07-09&7C2014-01-01&Year=2014&Month=1&Day=1&timeframe=1&submit=Download+Data
    Daily Data:
    http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=50430&Prov=AB&dlyRange=2012-07-97&7C2015-01-01&Year=2015&Month=1&Day=1&timeframe=2&submit=Download+Data

Eco-Counter has a private API that can be figured out by reading the AJAX requests performed on each of the counter pages. The data in question is owned by the City of Calgary. The counts are posted once a day normally between 5:00 and 6:00 AM MST, so the counts are *not* live.

    Individual Data Sets:
    http://www.eco-public.com/api/h7q239dd/data/periode/[ID]/?begin=YYYYMMDD&endYYYYMMDD&step=[NUMBER]
    Data Set Names for Installation:
    http://www.eco-public.com/api/h7q239dd/counter/channels/[ID]
    Public Page Details:
    http://www.eco-public.com/api/dfd15sd1ds/public/page/[ID]

The step ID can be 2 (daily), 3 (hourly), or 4 (15 minute).

Installation Name |     ID    | Start Date
------------------|-----------|------------
**Peace Bridge - Bikes and Peds**  | 100013817 | April 24, 2014
Peds Northbound   | 101013817 | 
Peds Southbound   | 102013817 | 
Bikes Northbound  | 103018487 | 
Bikes Southbound  | 104018487 | 
**Stephen Ave**   | 100020207 | October 23, 2014
Peds              | 101020207 |
Bikes             | 102020207 | 
Cars              | 103020207 |
**7th Street**    | 100017181 | December 11, 2014
Northbound        | 101017181 | 
Southbound        | 102017181 |
**5th Street N Leg**  | 100022540 | June 17, 2015
Northbound        | 102022540 | *
Southbound        | 101022540 | *
**5th Street CPR** | 100020095 | June 18, 2015
Northbound        | 101020095 |
Southbound        | 102020095 |
**5th Street S Leg**  | 100022541 | June 16, 2015
Northbound        | 101022541 | *
Southbound        | 102022541 | *
**12th Avenue W Leg** | 100022581 | June 16, 2015
Eastbound        | 101022581 | 
Westbound        | 102022581 |
**12th Avenue**  | 100022580 | June 16, 2015
Eastbound        | 102022580 | 
Westbound        | 101022580 |
**12th Avenue E Leg** | 100022582 | June 16, 2015
Eastbound        | 102022582 |
Westbound        | 101022582 |
**8th Avenue W Leg** | 100024297 | July 11, 2015
Eastbound        | 101024297 |
Westbound        | 102024297 |
**8th Avenue Centre** | 100024406 | July 9, 2015
Eastbound        | 1010124406 | 
Westbound        | 1020124406 | 
**9th Ave** | 100023675 | June 17, 2015
Eastbound        | 101023675 |
Westbound        | 102023675 |
**2015 Totals** | 100023678 | January 1, 2015 


There were also some other presentation or counters that have been retired in favour of news ones.

Installation Name |     ID    | Notes
------------------|-----------|------------
**Stephen Ave**   | 100017165 | October 23, 2014
**8th Ave**       | 100023674 | 
**8th Ave**       | 100024162 | 
**Peace Bridge**  | 100018487 | Original counter page for only bikes
**Stephen Ave**   | 100020243 | Original Stephen Ave Page didn't show peds.

## File Listing

### monthlyArchive.py

Save a monthly archive for reloading later

### statsLoad.py

Load the Eco Counter numbers into Graphite

### twitterBot.py

The script that runs the #yycbike\_count Twitter feed. Runs once a day.

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
