#! /usr/bin/env python3

import json
import time
import sys
import os
import argparse
from twitter import *
from datetime import date, timedelta
from urllib.request import urlopen

# Twitter Info read from the environment
t = Twitter(
    auth=OAuth(os.environ.get('TWITTER_TOKEN'),
        os.environ.get('TWITTER_TOKEN_KEY'),
        os.environ.get('TWITTER_CON_SECRET'),
        os.environ.get('TWITTER_CON_SECRET_KEY'))
    )

# Check if debug flag is set to NOT tweet
parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_false')
args = parser.parse_args()
debug = args.debug

def grabCounts(installation, yesterday, today):
    # City of Calgary's domain id
    domain = '4190'
    countURL = "https://www.eco-visio.net/api/aladdin/1.0.0/pbl/publicwebpageplus/data/" + installation['id'] + "?idOrganisme=" + domain + "&idPdc=" + installation['id'] + "&fin=" + today + "&debut=" + yesterday + "&interval=4&flowIds=" + installation['components']
    if debug != False:
        print(countURL)
    amount = 0
    try:
        response = urlopen(countURL)
        json_data = response.read()
        loaded_data = json.loads(json_data)

        # Handle Case where multiple values are available for the daily total (eg. Lindsay Park counter)
        if len(loaded_data) > 1:
            print(f"More than one entry encountered on {id}")
            for entry in loaded_data:
                if entry[1] is not None:
                    amount += entry[1]
        else:
            amount = loaded_data[0][1]

    except:
        amount = 0

        if amount is None or amount == 0:
            amount = 0
            print(f"Error loading - amount is None (counter down?) for {id} - {countURL}")
        else:
            print(f"Error loading {id} - {countURL}")

    return int(amount)

# Long list of counters to pull data from. There are two styles - those that only count bikes and only have an ID
# And those that count multiple items and as such have a component section needed to grab the correct numbers
# These IDs can be found in the README or otherwise at the URL:
#
PEACE_BRIDGE = {
    'installation':"Peace Bridge",
    'value': 0,
    'id': '100013817',
    'components': '103013817;104013817'
}

SEVENTH = {
    'installation': "7th St at 3rd Ave",
    'value': 0,
    'id': '100017181',
    'components': '100017181'
}

# No longer working as of Sept. 8, 2022
STEPHEN_AVE = {
    'installation': "Stephen Ave.",
    'value': 0,
    'id': '100020207',
    'components': '102020207'
}

# No longer as of Oct. 6, 2022
FIFTH_5 = {
    'installation': "5th St and 4th Ave",
    'value': 0,
    'id': '100022540',
    'components': '100022540'
}
FIFTH_10 = {
    'installation': "5th St Underpass",
    'value': 0,
    'id': '100020095',
    'components': '100020095'
}
FIFTH_15 = {
    'installation': "5th St and 15th Ave",
    'value': 0,
    'id': '100022541',
    'components': '100022541'
}

# No longer working as of Oct. 14, 2022
TWELFTH_8 = {
    'installation': "12th Ave and 8th St SW",
    'value': 0,
    'id': '100022581',
    'components': '100022581'
}
TWELFTH_2 = {
    'installation': "12th Ave and 2nd St SW",
    'value': 0,
    'id': '100022580',
    'components': '100022580'
}
# No longer working as of June 18, 2022
TWELFTH_3 = {
    'installation': "12th Ave and 3rd St SE",
    'value': 0,
    'id': '100022582',
    'components': '100022582'
}

NINTH_4 = {
    'installation': "9th Ave at 4th St SE",
    'value': 0,
    'id': '100059438',
    'components': '100059438'
}
# Removed but has sign... Need to find updated installation ID?
EIGHTH_3 = {
    'installation': "8th Ave at 3rd St SW",
    'value': 0,
    'id': '100030768',
    'components': '100030768'
}
EIGHTH_8 = {
    'installation': "8th Ave at 8th St SW",
    'value': 0,
    'id': '100031411',
    'components': '100031411'
}

# Construction in late 2022
TENTH = {
    'installation': "10th St NW N of 5th Ave NW",
    'value': 0,
    'id': '100020661',
    'components': '100020661'
}

# No longer functioning since Oct. 2022
EDMONTON_TRAIL = {
    'installation': "Edmonton Trail at Memorial Drive",
    'value': 0,
    'id': '100033550',
    'components': '100033550'
}

# Keeps flooding. Removed
RIVERWALK = {
    'installation':"Riverwalk",
    'value': 0,
    'id': '100138638',
    'components': '103138638;104138638'
}

# No longer working as of Nov. 1, 2022
NOSE_CREEK = {
    'installation':"Nose Creek",
    'value': 0,
    'id': '100128045',
    'components': '103128045;104128045'
}

MEMORIAL_DR = {
    'installation':"Memorial Drive E of Prince's Island Bridge",
    'value': 0,
    'id': '100128046',
    'components': '103128046;104128046'
}

# No longer working as of Dec. 2021
MEMORIAL_19 = {
    'installation':"Memorial Drive at 19th St NW",
    'value': 0,
    'id': '100128047',
    'components': '103128047;104128047'
}

# No longer working as of June 2021
LINDSAY = {
    'installation':"Lindsay Park",
    'value': 0,
    'id': '100128048',
    'components': '103128048;104128048'
}

# No longer working as of Oct. 31, 2022
SBR_11 = {
    'installation':"South Bow River at 11th St SW",
    'value': 0,
    'id': '100030402',
    'components': '103030402;104030402'
}

# No longer working as of Aug. 2021
PARKDALE = {
    'installation':"North Bow River at 29th St NW",
    'value': 0,
    'id': '100153497',
    'components': '103153497;104153497'
}

# No longer working as of Jan. 2022
INGLEWOOD_SANCTUARY = {
    'installation':"Inglewood Bird Sanctuary",
    'value': 0,
    'id': '100138344',
    'components': '103138344;104138344'
}

# No longer working as of Sept. 2022
NORTH_GLENMORE_PARK = {
    'installation':"North Glenmore Park",
    'value': 0,
    'id': '100134306',
    'components': '103134306;104134306'
}

GLENMORE_LANDING = {
    'installation':"Glenmore Pathway near Glenmore Landing",
    'value': 0,
    'id': '100134304',
    'components': '103134304;104134304'
}

# No longer working as of Nov. 2022
TWELFTH_ST_ZOO = {
    'installation':"12th St. SE near the Zoo",
    'value': 0,
    'id': '100044714',
    'components': '103044714;104044714'
}

# Timezones make time math hard. Also convert the time into three formats.
yesterday = date.today() - timedelta(1)
today = date.today()
fancyDate = yesterday.strftime('%a %b %d')
yesterday = yesterday.strftime('%d/%m/%Y')
today = today.strftime('%d/%m/%Y')

# For each installation
for installation in [ PEACE_BRIDGE, SEVENTH, FIFTH_10, TWELFTH_3,
   NINTH_4, EIGHTH_8, NOSE_CREEK, MEMORIAL_DR, LINDSAY,
   GLENMORE_LANDING, TWELFTH_ST_ZOO]:
    print("Attempting to grab " + installation['installation'])
    try:
        installation['value'] = grabCounts(installation, yesterday, today)
        print(installation['installation'])
        print(installation['value'])
    except:
        print("Failed to load installation info - skipping")
        print("Unexpected error:", sys.exc_info()[0])

# Now that we have all the data loaded... time for a little math to compose our tweets.

streetTotal = 0
pathwayTotal = 0

listOfStreetCounters = []
for i in [ SEVENTH, STEPHEN_AVE, FIFTH_5, FIFTH_10, FIFTH_15, TWELFTH_8, TWELFTH_2, TWELFTH_3, NINTH_4, EIGHTH_3, EIGHTH_8, TENTH, EDMONTON_TRAIL ]:
    listOfStreetCounters.append(i)
    streetTotal += i['value']

sortedStreetList = sorted(listOfStreetCounters, key=lambda k: k['value'], reverse=True)

listOfPathwayCounters = []
for i in [ PEACE_BRIDGE, RIVERWALK, NOSE_CREEK, MEMORIAL_DR, MEMORIAL_19, LINDSAY, SBR_11, PARKDALE, INGLEWOOD_SANCTUARY, NORTH_GLENMORE_PARK, GLENMORE_LANDING, TWELFTH_ST_ZOO ]:
    listOfPathwayCounters.append(i)
    pathwayTotal += i['value']

sortedPathwayList = sorted(listOfPathwayCounters, key=lambda k: k['value'], reverse=True)

top3StreetString = ""
top3PathwayString = ""
counter = 0

# Grab top 3
for i in sortedStreetList:
    top3StreetString += "%s: %d\n" % (i['installation'], i['value'])
    counter += 1
    if counter == 3:
        break

counter = 0

for i in sortedPathwayList:
    top3PathwayString += "%s: %d\n" % (i['installation'], i['value'])
    counter += 1
    if counter == 3:
        break

## On Street Count with Top 3
try:
    count_status=f"{streetTotal} #yycbike trips were counted on street on {fancyDate}\n\nBusiest:\n{top3StreetString}"
    print(count_status)
    if debug != True:
        t.statuses.update(status=count_status)
except:
    pass

## Pathway Count with Top 3
try:
    count_status=f"{pathwayTotal} #yycbike trips were counted on MUPs on {fancyDate}\n\nBusiest:\n{top3PathwayString}"
    print(count_status)
    if debug != True:
        t.statuses.update(status=count_status)
except:
    pass
