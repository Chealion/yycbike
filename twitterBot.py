#! /usr/bin/python

import json
import urllib2
from datetime import date, timedelta

#sixohsix/twitter
from twitter import *

#Set Twitter Info
token='REPLACE_ME'
token_key='REPLACE_ME'
con_secret='REPLACE_ME'
con_secret_key='REPLACE_ME'

t = Twitter(
	auth=OAuth(token, token_key, con_secret, con_secret_key))

# Get numbers from Eco Public
# Watch out for timezones - this script fails to function past 5 PM MST if VM set to UTC.

yesterday = date.today() - timedelta(1)
yesterday = yesterday.strftime('%Y%m%d')

# Wall of URLs

PB={'value':0, 'name':'Peace Bridge', 'url':"null"}
PB_NB={'value':0, 'name':'PB_NB', 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/103013817/"}
PB_SB={'value':0, 'name':'PB_SB', 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/104013817/"}

STEPHEN={'value':0, 'name':'Stephen Ave', 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102020207/"}

SEVENTH={'value':0, 'name':'7th St', 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/100017181/"}

FIFTH_5={'value':0, 'name':'5 St at 5th', 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/100022540/"}
FIFTH_10={'value':0, 'name':'5 St at CPR', 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/100020095/"}
FIFTH_15={'value':0, 'name':'5 St at 15th', 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/100022541/"}

TWELVE_8={'value':0, 'name':'12 Ave at 8th', 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/100022581/"}
TWELVE_2={'value':0, 'name':'12 Ave at 2nd', 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/100022580/"}
TWELVE_3={'value':0, 'name':'12 Ave at 3rd', 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/100022582/"}

NINTH_4={'value':0, 'name':'9 Ave at 4th', 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/100023675/"}
EIGHTH_8={'value':0, 'name':'8 Ave at 8th', 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/100024297/"}
EIGHTH_3={'value':0, 'name':'8 Ave at 3rd', 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/100024406/"}

total = 0

# Load Data into Dictionaries

for i in [ PB_NB, PB_SB, STEPHEN, SEVENTH, FIFTH_5, FIFTH_10, FIFTH_15, TWELVE_8, TWELVE_2, TWELVE_3, NINTH_4, EIGHTH_8, EIGHTH_3 ]:
    url=i['url'] + "?begin=" + yesterday + "&end=" + yesterday + "&step=4"
    response = urllib2.urlopen(url)
    json_data = response.read()
    amount = json.loads(json_data)[0]['comptage']
    i['value'] = amount

# Create Peace Bridge total

PB['value'] = PB_NB['value']+PB_SB['value']

# Create list and sort for top 3.

listOfCounters = []
for i in [ PB, STEPHEN, SEVENTH, FIFTH_5, FIFTH_10, FIFTH_15, TWELVE_8, TWELVE_2, TWELVE_3, NINTH_4, EIGHTH_8, EIGHTH_3 ]:
    listOfCounters.append(i)
    total += i['value']


sortedList = sorted(listOfCounters, key=lambda k: k['value'], reverse=True)
top3String = ""
counter = 0

# Grab top 3
for i in sortedList:
    top3String += "%s: %d\n" % (i['name'], i['value'])
    counter += 1
    if counter == 3:
        break

# Calculate averages

eighthAvg = int(round((EIGHTH_8['value'] + EIGHTH_3['value'] + NINTH_4['value'])/3,0))
#fifthAvg = int(round((FIFTH_5['value'] + FIFTH_10['value'] + FIFTH_15['value'])/3,0))
# Fifth only using two for now as the whole south of 5th track is closed...
fifthAvg = int(round((FIFTH_5['value'] + FIFTH_10['value'])/2,0))
twelfthAvg = int(round((TWELVE_8['value'] + TWELVE_2['value'] + TWELVE_3['value'])/3,0))

# Send out 2 tweets - summary of all, and top hits

## Top Hits

count_status="Yesterday a total of %d #yycbike trips were counted.\n\nBusiest Counters:\n%s" % (total, top3String)
print count_status

t.statuses.update(
	status=count_status)

## Summary

count_status="Yesterday's #yycbike trip counts:\n\n7 St: %d\nPeace Bridge: %d\nStephen Ave: %d\n8/9 Ave Avg: %d\n5 St Avg: %d\n12 Ave Avg: %d" % (SEVENTH['value'], PB['value'], STEPHEN['value'], eighthAvg, fifthAvg, twelfthAvg)
print count_status

t.statuses.update(
	status=count_status)

