#! /usr/bin/python
# :set tabstop=4 shiftwidth=4 expandtab

# statsLoad.py - downloads EcoCounter data and sends to Graphite. Additionally saves as a separate file for easier importing later.

import json
import graphitesend
import urllib2
from datetime import date, timedelta

graphitesend.init(graphite_server='localhost',prefix='yycbike',system_name='')
metriclog = open('/home/ubuntu/metriclog.log', 'a')

# Get numbers from Eco Public
# Watch out for timezones - this script fails to function past 5 PM MST.

yesterday = date.today() - timedelta(1)
yesterday = yesterday.strftime('%Y%m%d')

# Manual date - uncomment
#yesterday = date(2014,04,24).strftime('%Y%m%d')
#today = date(2015,07,04).strftime('%Y%m%d')

#Installations

# Peace Bridge
PB_NB={'installation':"peacebridge", 'direction':"north", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/103013817/"}
PB_SB={'installation':"peacebridge", 'direction':"south", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/104013817/"}

PB_PED_NB={'installation':"yycwalk.peacebridge", 'direction':"north", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101013817/"}
PB_PED_SB={'installation':"yycwalk.peacebridge", 'direction':"south", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102013817/"}

SEVEN_NB={'installation':"sevenst", 'direction':"north", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101017181/"}
SEVEN_SB={'installation':"sevenst", 'direction':"south", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102017181/"}

STEPHEN_CAR={'installation':"stephenave", 'direction':"car", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/103020207/"}
STEPHEN_BIKE={'installation':"stephenave", 'direction':"bike", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102020207/"}
STEPHEN_PED={'installation':"stephenave", 'direction':"ped", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101020207"}

FIFTH_5_NB={'installation':"fifth.fifth", 'direction':"north", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102022540/"}
FIFTH_5_SB={'installation':"fifth.fifth", 'direction':"south", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101022540/"}
FIFTH_10_NB={'installation':"fifth.tenth", 'direction':"north", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101020095/"}
FIFTH_10_SB={'installation':"fifth.tenth", 'direction':"south", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102020095/"}
FIFTH_15_NB={'installation':"fifth.fifteenth", 'direction':"north", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101022541/"}
FIFTH_15_SB={'installation':"fifth.fifteenth", 'direction':"south", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102022541/"}

TWELFTH_8_EB={'installation':"twelfth.eighthsw", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101022581/"}
TWELFTH_8_WB={'installation':"twelfth.eighthsw", 'direction':"westbound", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102022581/"}
TWELFTH_2_EB={'installation':"twelfth.secondsw", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101022580/"}
TWELFTH_2_WB={'installation':"twelfth.secondsw", 'direction':"westbound", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102022580/"}
TWELFTH_3_EB={'installation':"twelfth.thirdse", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102022582/"}
TWELFTH_3_WB={'installation':"twelfth.thirdse", 'direction':"westbound", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101022582/"}

NINTH_4_EB={'installation':"ninth.fourthse", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101023675/"}
NINTH_4_WB={'installation':"ninth.fourthse", 'direction':"westbound", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102023675/"}

EIGHTH_8_EB={'installation':"eighth.eighthsw", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101024297/"}
EIGHTH_8_WB={'installation':"eighth.eighthsw", 'direction':"westbound", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102024297/"}

EIGHTH_3_EB={'installation':"eighth.thirdsw", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101024406/"}
EIGHTH_3_WB={'installation':"eighth.thirdsw", 'direction':"westbound", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102024406/"}

for i in [ PB_NB, PB_SB, PB_PED_NB, PB_PED_SB, SEVEN_NB, SEVEN_SB, STEPHEN_CAR, STEPHEN_BIKE, FIFTH_5_NB, FIFTH_5_SB, FIFTH_10_NB, FIFTH_10_SB, FIFTH_15_NB, FIFTH_15_SB, TWELFTH_8_EB, TWELFTH_8_WB, TWELFTH_2_EB, TWELFTH_2_WB, TWELFTH_3_EB, TWELFTH_3_WB, NINTH_4_EB, NINTH_4_WB, EIGHTH_8_EB, EIGHTH_8_WB, EIGHTH_3_EB, EIGHTH_3_WB ]:
    # Specify yesterday to download
    url=i['url'] + "?begin=" + yesterday + "&end=" + yesterday + "&step=2"
    dailyurl=i['url'] + "?begin=" + yesterday + "&end=" + yesterday + "&step=4"
    print 'Loading ' + i['installation'] + ' ' + i['direction'] + '...'
    # 15 minute counts
    response = urllib2.urlopen(url)
    json_data = response.read()
    datapoints = json.loads(json_data)
    for datapoint in datapoints:
        if datapoint['comptage'] is None:
            continue
        metric_string = i['installation'] + '.' + i['direction'] + '.trips ' + str(datapoint['comptage']) + ' ' + str(datapoint['timestamp']/1000)
        metriclog.write(metric_string + "\n")
        graphitesend.send(i['installation'] + '.' + i['direction'] + '.trips', datapoint['comptage'], datapoint['timestamp']/1000)
	
    # Daily counts
    response = urllib2.urlopen(dailyurl)
    json_data = response.read()
    datapoints = json.loads(json_data)
    for datapoint in datapoints:
        if datapoint['comptage'] is None:
            continue
	# Set daily time forward
	datapoint['timestamp'] += 14400000
        metric_string = 'daily.' + i['installation'] + '.' + i['direction'] + '.trips ' + str(datapoint['comptage']) + ' ' + str(datapoint['timestamp']/1000)
        graphitesend.send('daily.' + i['installation'] + '.' + i['direction'] + '.trips', datapoint['comptage'], datapoint['timestamp']/1000)

# OUTPUT FORMAT:
# <metric path> <metric value> <metric timestamp>
# yycbike.peacebridge.north.trips 5 123456789 

metriclog.close()

print 'Done.'

