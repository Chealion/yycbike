# #yycbike Counter

Collection of scripts and bits and bobs I used to create [http://calgary.bike](http://calgary.bike) and the [yycbike_count](https://twitter.com/yycbike_count) Twitter bot.

The data is collected from the following sources:

  * [Environment Canada](http://climate.weather.gc.ca)
  * Public Eco-Counter Pages for individual counters.
    * [Calgary Bike Counter Page](https://data.eco-counter.com/ParcPublic/?id=4190)
    * [Peace Bridge - Bikes and Pedestrians](https://data.eco-counter.com/public2/?id=100013817)
    * [Stephen Ave](https://data.eco-counter.com/public2/?id=100020207)
    * [7th St.](https://data.eco-counter.com/public2/?id=100017181)
    * 5th St. - [North Leg](https://data.eco-counter.com/public2/?id=100022540), [N of 9th](https://data.eco-counter.com/public2/?id=100059885], [Under the Tracks](https://data.eco-counter.com/public2/?id=100020095), [South Leg](https://data.eco-counter.com/public2/?id=100022541)
    * 12th Ave. - [West Leg](https://data.eco-counter.com/public2/?id=100022581), [Central Memorial](https://data.eco-counter.com/public2/?id=100022580), [East Leg](https://data.eco-counter.com/public2/?id=100022582)
    * 8th Ave. - [West Leg](https://data.eco-counter.com/public2/?id=100031441), [Centre](https://data.eco-counter.com/public2/?id=100030768)
    * 9th Ave. - [NMC](https://data.eco-counter.com/public2/?id=100030452)
    * [Riverwalk](https://data.eco-counter.com/public2/?id=100138638)
    * [Nose Creek at Bow River](https://data.eco-counter.com/public2/?id=100128045)
    * [Memorial Drive at Prince's Island](https://data.eco-counter.com/public2/?id=100128046)
    * [Memorial Drive at 19th St. NW](https://data.eco-counter.com/public2/?id=100128047)
    * [Lindsay Park](https://data.eco-counter.com/public2/?id=100128048)
    * [10th St.](https://data.eco-counter.com/public2/?id=100020661)
    * [S Bow River Pathway](https://data.eco-counter.com/public2/?id=100030402)
    * Wetlands Trail Corridor
    * [Edmonton Trail Cycle Track](https://data.eco-counter.com/public2/?id=100033550)
    * [Nose Hill Park](https://data.eco-counter.com/public2/?id=100134303)
    * [Parkdale](https://data.eco-counter.com/public2/?id=100134305)
    * [North Glenmore](https://data.eco-counter.com/public2/?id=100134306)
    * [South Glenmore](https://data.eco-counter.com/public2/?id=100134304)
    * [Inglewood Bird Sanctuary](https://data.eco-counter.com/public2/?id=100138344)
    * [12th St. SE beside Zoo](https://data.eco-counter.com/public2/?id=100044714)

The City also makes this data available via their Open Data Portal in two
datasets, with some delay:

    1. [Counter Locations](https://data.calgary.ca/Transportation-Transit/Bike-and-Pedestrian-Counts-Monitoring-Locations/uwis-xpm2)
    2. [Count Data](https://data.calgary.ca/Transportation-Transit/Bike-and-Pedestrian-Counts/pede-tz7g)

## Thank You

Thanks to the City of Calgary and the team working on the project for making this data public. Thanks to those members of the public who pushed for this data to be made available. Awesome to have timely easy access to the data.

## Tweet Information

Two tweets are sent out each day:

1 - A total and the top 3 counters of on street counters.  
2 - A total and the top 3 counters of pathway counters.  

On street counters: 5th St SW, 7th St SW, 8 Ave SW, 9 Ave SE, 10 St NW, 12 Ave 
Pathway counters: Peace Bridge, Riverwalk, Nose Creek at Bow River, Lindsay Park, N Glennore Park, SE Glenmore Park, Nose Hill, Memorial Drive E of Prince's Island, Memorial Drive at 19th St NW, Memorial Drive at 29th St NW  

The total value is best used as a comparison to itself over the course of time.

## How does it run?

The script nows runs via GitHub Actions. If you want to run your own, you can use the workflow in the .github folder and note you will need to make 4 secrets corresponding to the Twitter credentials.

## Source Data Notes

Environment Canada's data is available as hourly readings (a month's worth), or as daily readings (a year's worth). I use Station 50430 (the Airport)

    Hourly Data:
    http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=50430&Year=2016&Month=06&Day=07&submit=Download+Data&timeframe=1
    Daily Data:
    http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=50430&Prov=AB&dlyRange=2012-07-09&7C2016-06-07&Year=2016&Month=06&Day=07&submit=Download+Data&timeframe=2

Eco-Counter has an API and is documented at https://developers.eco-counter.com/
The data in question is owned by the City of Calgary. The counts are posted once a day normally between 5:00 and 6:00 AM MST, so the counts are **not** live.

Website API Breakdown:

    Individual Data Sets:
    https://www.eco-visio.net/api/aladdin/1.0.0/pbl/publicwebpageplus/data/[ID]?idOrganisme=[CITY]&idPdc=[ID]&fin=DD/MM/YYY&debut=DD/MM/YYYY&interval=[NUMBER]&flowIds=[COMPONENT_ID,COMPONENT_ID,COMPONENT_ID]
    Alternative from dedicated pages:
    https://www.eco-visio.net/api/aladdin/1.0.0/pbl/publicwebpage/data/[ID]?begin=YYYYMMDD&end=YYYYMMDD&step=[NUMBER]&domain=[CITY]&t=[TOKEN]&withNull=true
    Data Set Names for Installation and the Public Page Details:
    https://www.eco-visio.net/api/aladdin/1.0.0/pbl/publicwebpage/[Installation_ID]?withNull=true

The installation details call provides a valid token that can be used for the
individual data sets.

The step number can be 1 (15 minute), 2 (30 minute), 3 (hourly), 4 (daily), 5 (weekly),
6 (monthly) or 7 (annual).

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
**5th Street N of 9th** | 100059885 | June 1, 2020
Northbound | 101059885 |
Soundbound | 101059885 |
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
Westbound        | 102024297 | Only WB in 2016?
**8th Ave W Leg Perm Counter** | 100031441 | May 15, 2016
Bikes Eastbound | 102031441 |
Bikes Westbound | 101031441 |
**8th Avenue Centre** | 100030768 | July 9, 2015
Eastbound        | 101030768 | 
Westbound        | 102030768 | 
**9th Ave** | 100030452 | June 17, 2015 - changed to 100059438
Eastbound        | 101030452 |
Westbound        | 102030452 |
**Riverwalk**  | 100138638 | October 15, 2015
Peds Eastbound   | 102138638 |
Peds Westbound   | 101138638 |
Bikes Eastbound  | 104138638 |
Bikes Westbound  | 103138638 |
**Nose Creek at Bow River**  | 100128045 | October 16, 2015
Peds Northbound   | 102128045 | 
Peds Southbound   | 101128045 | 
Bikes Northbound  | 104128045 | 
Bikes Southbound  | 103128045 | 
**Memorial Drive at Prince's Island**  | 100128046 | October 16, 2015
Peds Eastbound   | 102128046 | 
Peds Westbound   | 101128046 | 
Bikes Eastbound  | 104128046 | 
Bikes Westbound  | 103128046 | 
**Memorial Drive at 19th St. NW**  | 100128047 | October 15, 2015
Peds Eastbound   | 101128047 | 
Peds Westbound   | 102128047 | 
Bikes Eastbound  | 103128047 | 
Bikes Westbound  | 104128047 | 
**Lindsay Park**  | 100128048 | October 15, 2015
Peds Northbound   | 101128048 | 
Peds Southbound   | 102128048 | 
Bikes Northbound  | 103128048 | 
Bikes Southbound  | 104128048 | 
**10th St.** | 100020661 | March 22, 2016
Northbound | 102020661 |
Southbound | 101020661 |
**S Bow River Pathway** | S Bow River Pathway | March 30, 2016
Peds Eastbound   | 101030402 | 
Peds Westbound   | 102030402 | 
Bikes Eastbound  | 103030402 | 
Bikes Westbound  | 104030402 | 
**Wetlands Trail Counter** | 100130911 | May 5, 2016
Peds Eastbound   | 101130911 |
Peds Westbound   | 102130911 |
Bikes Eastbound  | 103130911 |
Bikes Westbound  | 104130911 |
**Edmonton Trail Cycle Track** | 100033550 | Sept. 7, 2016
Northbound | 102033550 |
Southbound | 101033550 |
**Parkdale Bow River Pathway** | 100153497 | October 13, 2016
Peds Eastbound   | 101153497 |
Peds Westbound   | 102153497|
Bikes Eastbound  | 103153497 |
Bikes Westbound  | 104153497 |
**North Glenmore** | 100134306 | October 13, 2016
Peds Eastbound   | 101134306 |
Peds Westbound   | 102134306 |
Bikes Eastbound  | 103134306 |
Bikes Westbound  | 104134306 |
**South Glenmore** | 100134304 | October 13, 2016
Peds Northbound   | 101134304 |
Peds Southbound   | 102134304 |
Bikes Northbound  | 103134304 |
Bikes Southbound  | 104134304 |
**Inglewood Bird Sanctuary** | 100138344 | May 19, 2017
Peds Northbound   | 101138344 |
Peds Southbound   | 102138344 |
Bikes Northbound  | 103138344 |
Bikes Southbound  | 104138344 |
**2015 Totals** | 100023678 | January 1, 2015 
**12th St. SE near Zoo** | 100044714 | June 12, 2019
Peds Eastbound | 101044714 |
Peds Westbound | 102044714 |
Bikes Eastbound | 103044714 |
Bikes Westbound | 104044714 |

Totems:  
**5th Street at CPR**: 100127783  
**8th Ave at 3rd St.**: 100030761  
**12th Ave at 8th St.**: 100128055

There were also some other presentation or counters that have been retired in favour of new ones.

Installation Name |     ID    | Notes
------------------|-----------|------------
**Stephen Ave**   | 100017165 | October 23, 2014
**8th Ave**       | 100023674 | 
**8th Ave**       | 100024162 | 
**Peace Bridge**  | 100018487 | Original counter page for only bikes
**Stephen Ave**   | 100020243 | Original Stephen Ave Page didn't show peds.
**9th Ave**       | 100023675 | Original portable counter for 9th Ave.
**8th Ave**       | 100024406 | 8th Ave and 3rd St. Changed in late April 2016.
**8th Ave Display** | 100128054 | 
**Riverwalk**  | 100128044 | Original counter until totem installed.
**Nose Hill Park** | 100134303 | October 17, 2016

## File Listing

### twitterBot.py

The script that runs the #yycbike\_count Twitter feed. Runs once a day. Tweets a summary with the 3 busiest counters, and one with the numbers for each major route. If multiple counters are on a route - choses the midpoint/median.

### Archived Files

This project used to also store weather and count data into Graphite. These scripts are no longer updated.

### archive/statsLoad.py

Load the Eco Counter numbers into Graphite

### archive/weatherLoad.py

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

## LICENSE

[MIT License](http://choosealicense.com/licenses/mit/)
