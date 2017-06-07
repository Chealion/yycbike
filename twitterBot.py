#! /usr/bin/python

# Downloads data from Eco-Counter, and publishes a series of 4 tweets:
# 1. Total Summary of on street counters with 3 busiest counters
# 2. Total Summary of pathway counters with 3 busiest counters
# 3. Midpoints and counts for On street counters
# 4. Counts for a selection of other Pathway counters
#

import json
import urllib2
import time
from datetime import date, timedelta

#sixohsix/twitter
from twitter import *
from config import *

# Twitter Info set by config.py file
t = Twitter(
    auth=OAuth(twitter_token, twitter_token_key, twitter_con_secret, twitter_con_secret_key))

# Get numbers from Eco Public
# Watch out for timezones - this script fails to function past 5 PM MST if VM set to UTC.

yesterday = date.today() - timedelta(1)
fancyDate = yesterday.strftime('%a %b %d')
yesterday = yesterday.strftime('%Y%m%d')

# Wall of URLs - we want totals. Counters with multiple modes need each direction polled separately
# Peace Bridge
PB={'value':0, 'installation':'Peace Bridge', 'url':"null"}
PB_NB={'installation':"peacebridge", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103013817/"}
PB_SB={'installation':"peacebridge", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/104013817/"}

PB_PED_NB={'installation':"yycwalk.peacebridge", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101013817/"}
PB_PED_SB={'installation':"yycwalk.peacebridge", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102013817/"}

SEVENTH={'installation':"7th St", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/100017181/"}

STEPHEN_CAR={'installation':"stephenave", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103020207/"}
STEPHEN_BIKE={'installation':"Stephen Ave", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102020207/"}
STEPHEN_PED={'installation':"stephenave", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101020207"}

FIFTH_5={'installation':"5th and 5th", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/100022540/"}
FIFTH_10={'installation':"5th at CPR", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/100020095/"}
FIFTH_15={'installation':"5th and 15th", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/100022541/"}

TWELFTH_8={'installation':"8th and 12th SW", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/100022581/"}
TWELFTH_2={'installation':"2nd and 12th", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/100022580/"}
TWELFTH_3={'installation':"3rd SE and 12th", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/100022582/"}

NINTH_4={'installation':"4th SE and 9th", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/100030452/"}
EIGHTH_8={'installation':"8th and 8th", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/100031441/"}
EIGHTH_3={'installation':"3rd and 8th", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/100030768/"}

RIVERWALK={'value':0, 'installation':'Riverwalk', 'url':"null"}
RIVERWALK_PED_EB={'installation':"yycwalk.riverwalk", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102138343/"}
RIVERWALK_PED_WB={'installation':"yycwalk.riverwalk", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101138343/"}
RIVERWALK_EB={'installation':"riverwalk.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/104138343/"}
RIVERWALK_WB={'installation':"riverwalk.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103138343/"}

NOSECREEK_BOW={'value':0, 'installation':'Nose Creek', 'url':"null"}
NOSECREEK_BOW_PED_NB={'installation':"yycwalk.nosebow", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102128045/"}
NOSECREEK_BOW_PED_SB={'installation':"yycwalk.nosebow", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101128045/"}
NOSECREEK_BOW_NB={'installation':"nosebow.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/104128045/"}
NOSECREEK_BOW_SB={'installation':"nosebow.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103128045/"}

MEMORIAL_PRINCE={'value':0, 'installation':'NBR E of Princes Isl', 'url':"null"}
MEMORIAL_PRINCE_PED_EB={'installation':"yycwalk.memorialprinces", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102128046/"}
MEMORIAL_PRINCE_PED_WB={'installation':"yycwalk.memorialprinces", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101128046/"}
MEMORIAL_PRINCE_EB={'installation':"memorialprinces.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/104128046/"}
MEMORIAL_PRINCE_WB={'installation':"memorialprinces.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103128046/"}

MEMORIAL_19={'value':0, 'installation':'NBR near 19 St NW', 'url':"null"}
MEMORIAL_19_PED_EB={'installation':"yycwalk.memorialnineteen", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101128047/"}
MEMORIAL_19_PED_WB={'installation':"yycwalk.memorialnineteen", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102128047/"}
MEMORIAL_19_EB={'installation':"memorialnineteen.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103128047/"}
MEMORIAL_19_WB={'installation':"memorialnineteen.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/104128047/"}

LINDSAY={'value':0, 'installation':'Lindsay Park', 'url':"null"}
LINDSAY_PED_NB={'installation':"yycwalk.lindsay", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102128048/"}
LINDSAY_PED_SB={'installation':"yycwalk.lindsay", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101128048/"}
LINDSAY_NB={'installation':"lindsay.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/104128048/"}
LINDSAY_SB={'installation':"lindsay.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103128048/"}

TENTH={'installation':"10th St", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/100020661/"}

SBOW_10={'value':0, 'installation':'SBR @ 11 St', 'url':"null"}
SBOW_10_PED_EB={'installation':"yycwalk.sbowten", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102030402/"}
SBOW_10_PED_WB={'installation':"yycwalk.sbowten", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101030402/"}
SBOW_10_EB={'installation':"sbowten.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/104030402/"}
SBOW_10_WB={'installation':"sbowten.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103030402/"}

EDM_TR={'installation':"Edmonton Trail", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/100033550/"}

NOSE_HILL={'value':0, 'installation':'Nose Hill', 'url':"null"}
NOSE_HILL_PED_SB={'installation':"yycwalk.nosehill", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101134303/"}
NOSE_HILL_PED_NB={'installation':"yycwalk.nosehill", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102134303/"}
NOSE_HILL_SB={'installation':"nosehill.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103134303/"}
NOSE_HILL_NB={'installation':"nosehill.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103134303/"}

PARKDALE={'value':0, 'installation':'NBR @ 29 St', 'url':"null"}
PARKDALE_PED_EB={'installation':"yycwalk.parkdale", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101134305/"}
PARKDALE_PED_WB={'installation':"yycwalk.parkdale", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102134305/"}
PARKDALE_EB={'installation':"parkdale.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103134305/"}
PARKDALE_WB={'installation':"parkdale.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103134305/"}

NGLENMORE={'value':0, 'installation':'N Glenmore Park', 'url':"null"}
NGLENMORE_PED_EB={'installation':"yycwalk.nglenmore", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101134306/"}
NGLENMORE_PED_WB={'installation':"yycwalk.nglenmore", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102134306/"}
NGLENMORE_EB={'installation':"nglenmore.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103134306/"}
NGLENMORE_WB={'installation':"nglenmore.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103134306/"}

SGLENMORE={'value':0, 'installation':'Glenmore Resv', 'url':"null"}
SGLENMORE_PED_NB={'installation':"yycwalk.sglenmore", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101134304/"}
SGLENMORE_PED_SB={'installation':"yycwalk.sglenmore", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102134304/"}
SGLENMORE_NB={'installation':"sglenmore.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103134304/"}
SGLENMORE_SB={'installation':"sglenmore.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103134304/"}

INGLEWOOD_BS={'value':0, 'installation':'Bird Sanctuary', 'url':"null"}
INGLEWOOD_BS_PED_NB={'installation':"yycwalk.inglewoodbs", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101138344/"}
INGLEWOOD_BS_PED_SB={'installation':"yycwalk.inglewoodbs", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102138344/"}
INGLEWOOD_BS_NB={'installation':"inglewoodbs.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103138344/"}
INGLEWOOD_BS_SB={'installation':"inglewoodbs.bike", 'value':0, 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103138344/"}

streetTotal = 0
pathwayTotal = 0
errorFound = False

# Load Data into Dictionaries
for i in [ PB_NB, PB_SB, SEVENTH, STEPHEN_BIKE, FIFTH_5, FIFTH_10, FIFTH_15, TWELFTH_8, TWELFTH_2, TWELFTH_3, NINTH_4, EIGHTH_8, EIGHTH_3, RIVERWALK_EB, RIVERWALK_WB, NOSECREEK_BOW_NB, NOSECREEK_BOW_SB, MEMORIAL_PRINCE_EB, MEMORIAL_PRINCE_WB, MEMORIAL_19_EB, MEMORIAL_19_WB, LINDSAY_NB, LINDSAY_SB, TENTH, SBOW_10_EB, SBOW_10_WB, EDM_TR, NOSE_HILL_SB, NOSE_HILL_NB, PARKDALE_EB, PARKDALE_WB, NGLENMORE_EB, NGLENMORE_WB, SGLENMORE_NB, SGLENMORE_SB, INGLEWOOD_BS_NB, INGLEWOOD_BS_SB ]:
    url=i['url'] + "?begin=" + yesterday + "&end=" + yesterday + "&step=4"
    amount = 0
    try:
        response = urllib2.urlopen(url)
        json_data = response.read()
	loaded_data = json.loads(json_data)

	# Handle Case where multiple values are available for the daily total (eg. Lindsay Park counter)
	if len(loaded_data) > 1:
		print "More than one entry encountered on %s" % (i['installation'])
		for entry in loaded_data:
			if entry['comptage'] is not None:
				amount += entry['comptage']
	else:
		amount = json.loads(json_data)[0]['comptage']

	time.sleep(1)
    except:
	# If comptage is not there at all - set to 0.
		amount = 0
		errorFound = True
		print "Error loading %s - %s" % (i['installation'], url)

    if amount is None or amount == 0:
	amount = 0
	errorFound = True
	print "Error loading - amount is None for %s" % (i['installation'])
    i['value'] = amount

# Total multi mode counters

PB['value'] = PB_NB['value'] + PB_SB['value']
RIVERWALK['value'] = RIVERWALK_EB['value'] + RIVERWALK_WB['value']
NOSECREEK_BOW['value'] = NOSECREEK_BOW_NB['value'] + NOSECREEK_BOW_SB['value']
MEMORIAL_PRINCE['value'] = MEMORIAL_PRINCE_EB['value'] + MEMORIAL_PRINCE_WB['value']
MEMORIAL_19['value'] = MEMORIAL_19_EB['value'] + MEMORIAL_19_WB['value']
LINDSAY['value'] = LINDSAY_NB['value'] + LINDSAY_SB['value']
SBOW_10['value'] = SBOW_10_WB['value'] + SBOW_10_EB['value']
NOSE_HILL['value'] = NOSE_HILL_NB['value'] + NOSE_HILL_SB['value']
PARKDALE['value'] = PARKDALE_WB['value'] + PARKDALE_EB['value']
NGLENMORE['value'] = NGLENMORE_WB['value'] + NGLENMORE_EB['value']
SGLENMORE['value'] = SGLENMORE_NB['value'] + SGLENMORE_SB['value']
INGLEWOOD_BS['value'] = INGLEWOOD_NB['value'] + INGLEWOOD_SB['value']

# Create list and sort for top 3, street and pathway.

listOfStreetCounters = []
for i in [ STEPHEN_BIKE, SEVENTH, FIFTH_5, FIFTH_10, FIFTH_15, TWELFTH_8, TWELFTH_2, TWELFTH_3, NINTH_4, EIGHTH_8, EIGHTH_3, EDM_TR, TENTH ]:
    listOfStreetCounters.append(i)
    print "%s: %d" % (i['installation'], i['value'])
    streetTotal += i['value']

sortedStreetList = sorted(listOfStreetCounters, key=lambda k: k['value'], reverse=True)

listOfPathwayCounters = []
for i in [ PB, RIVERWALK, NOSECREEK_BOW, MEMORIAL_PRINCE, MEMORIAL_19, LINDSAY, SBOW_10, NOSE_HILL, PARKDALE, NGLENMORE, SGLENMORE, INGLEWOOD_BS ]:
    listOfPathwayCounters.append(i)
    print "%s: %d" % (i['installation'], i['value'])
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

# Send Tweets

if errorFound:
    flag = '*Incomplete Data'
else:
    flag = ''

## On Street Count with Top 3
try:
    count_status="%d #yycbike trips were counted on street on %s\n\nBusiest:\n%s%s" % ( streetTotal, fancyDate, top3StreetString, flag)
    print count_status
    t.statuses.update(
	status=count_status)
except:
    pass

## Pathway Count with Top 3
try:
    count_status="%d #yycbike trips were counted on MUPs on %s\n\nBusiest:\n%s%s" % ( pathwayTotal, fancyDate, top3PathwayString, flag)
    if len(count_status) > 140:
	count_status="%d #yycbike trips were counted on MUPs on %s\n\nBusiest:\n%s\n**" % ( pathwayTotal, fancyDate, top3PathwayString)
    print count_status
    t.statuses.update(
	status=count_status)
except:
    pass

## Street Raw

try:
    count_status="%s (Centre Points):\n5 St: %d\n7 St: %d\n8 Ave: %d\n10 St: %d\n12 Ave: %d\nEdm Tr: %d\nStephen Ave: %d" % (fancyDate, FIFTH_10['value'], SEVENTH['value'], EIGHTH_3['value'], TENTH['value'], TWELFTH_2['value'], EDM_TR['value'], STEPHEN_BIKE['value'])
    print count_status

    t.statuses.update(
	status=count_status)
except:
    pass

## Pathway Raw

try:
    count_status="%s Other Pathways\nGlenmore Park: %d\nNose Crk: %d\nLindsay: %d\nPrince's Isl: %d\nNose Hill: %d\n19th NW: %d\nParkdale: %d\n" % (fancyDate, SGLENMORE['value'], NOSECREEK_BOW['value'], LINDSAY['value'], MEMORIAL_PRINCE['value'], NOSE_HILL['value'], MEMORIAL_19['value'], PARKDALE['value'])
    print count_status

    t.statuses.update(
	status=count_status)
except:
    pass

