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

#Installations

# Peace Bridge
PB_NB={'installation':"peacebridge", 'direction':"north", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101018487/"}
PB_SB={'installation':"peacebridge", 'direction':"south", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102018487/"}

SEVEN_NB={'installation':"sevenst", 'direction':"north", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101017181/"}
SEVEN_SB={'installation':"sevenst", 'direction':"south", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102017181/"}

STEPHEN_CAR={'installation':"stephenave", 'direction':"car", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/103017165/"}
STEPHEN_BIKE={'installation':"stephenave", 'direction':"bike", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/102017165"}
# Not available due to calibration issues - https://twitter.com/DaleCalkins/status/589087591078580224
#STEPHEN_PED={'installation':"stephenave", 'direction':"ped", 'url':"http://www.eco-public.com/api/h7q239dd/data/periode/101017165"}

for i in [ PB_NB, PB_SB, SEVEN_NB, SEVEN_SB, STEPHEN_CAR, STEPHEN_BIKE ]:
    # Specify yesterday to download
    url=i['url'] + "?begin=" + yesterday + "&end=" + yesterday + "&step=2"
    print 'Loading ' + i['installation'] + ' ' + i['direction'] + '...'
    response = urllib2.urlopen(url)
    json_data = response.read()
    datapoints = json.loads(json_data)
    for datapoint in datapoints:
        if datapoint['comptage'] is None:
            continue
        metric_string = i['installation'] + '.' + i['direction'] + '.trips ' + str(datapoint['comptage']) + ' ' + str(datapoint['timestamp']/1000)
        metriclog.write(metric_string + "\n")
        graphitesend.send(i['installation'] + '.' + i['direction'] + '.trips', datapoint['comptage'], datapoint['timestamp']/1000)

# OUTPUT FORMAT:
# <metric path> <metric value> <metric timestamp>
# yycbike.peacebridge.north.trips 5 123456789 

metriclog.close()

print 'Done.'

