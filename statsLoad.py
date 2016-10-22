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
PB_NB={'installation':"peacebridge", 'direction':"north", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103013817/"}
PB_SB={'installation':"peacebridge", 'direction':"south", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/104013817/"}

PB_PED_NB={'installation':"yycwalk.peacebridge", 'direction':"north", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101013817/"}
PB_PED_SB={'installation':"yycwalk.peacebridge", 'direction':"south", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102013817/"}

SEVEN_NB={'installation':"sevenst", 'direction':"north", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101017181/"}
SEVEN_SB={'installation':"sevenst", 'direction':"south", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102017181/"}

STEPHEN_CAR={'installation':"stephenave", 'direction':"car", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103020207/"}
STEPHEN_BIKE={'installation':"stephenave", 'direction':"bike", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102020207/"}
STEPHEN_PED={'installation':"stephenave", 'direction':"ped", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101020207"}

FIFTH_5_NB={'installation':"fifth.fifth", 'direction':"north", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102022540/"}
FIFTH_5_SB={'installation':"fifth.fifth", 'direction':"south", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101022540/"}
FIFTH_10_NB={'installation':"fifth.tenth", 'direction':"north", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101020095/"}
FIFTH_10_SB={'installation':"fifth.tenth", 'direction':"south", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102020095/"}
FIFTH_15_NB={'installation':"fifth.fifteenth", 'direction':"north", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101022541/"}
FIFTH_15_SB={'installation':"fifth.fifteenth", 'direction':"south", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102022541/"}

TWELFTH_8_EB={'installation':"twelfth.eighthsw", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101022581/"}
TWELFTH_8_WB={'installation':"twelfth.eighthsw", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102022581/"}
TWELFTH_2_EB={'installation':"twelfth.secondsw", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101022580/"}
TWELFTH_2_WB={'installation':"twelfth.secondsw", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102022580/"}
TWELFTH_3_EB={'installation':"twelfth.thirdse", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102022582/"}
TWELFTH_3_WB={'installation':"twelfth.thirdse", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101022582/"}

NINTH_4_EB={'installation':"ninth.fourthse", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101030452/"}
NINTH_4_WB={'installation':"ninth.fourthse", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102030452/"}

EIGHTH_8_EB={'installation':"eighth.eighthsw", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101024297/"}
EIGHTH_8_WB={'installation':"eighth.eighthsw", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102024297/"}

EIGHTH_3_EB={'installation':"eighth.thirdsw", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101030768/"}
EIGHTH_3_WB={'installation':"eighth.thirdsw", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102030768/"}

RIVERWALK_PED_EB={'installation':"yycwalk.riverwalk", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102128044/"}
RIVERWALK_PED_WB={'installation':"yycwalk.riverwalk", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101128044/"}
RIVERWALK_EB={'installation':"riverwalk.bike", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/104128044/"}
RIVERWALK_WB={'installation':"riverwalk.bike", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103128044/"}

NOSECREEK_BOW_PED_NB={'installation':"yycwalk.nosebow", 'direction':"northbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102128045/"}
NOSECREEK_BOW_PED_SB={'installation':"yycwalk.nosebow", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101128045/"}
NOSECREEK_BOW_NB={'installation':"nosebow.bike", 'direction':"northbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/104128045/"}
NOSECREEK_BOW_SB={'installation':"nosebow.bike", 'direction':"southbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103128045/"}

MEMORIAL_PRINCE_PED_EB={'installation':"yycwalk.memorialprinces", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102128046/"}
MEMORIAL_PRINCE_PED_WB={'installation':"yycwalk.memorialprinces", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101128046/"}
MEMORIAL_PRINCE_EB={'installation':"memorialprinces.bike", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/104128046/"}
MEMORIAL_PRINCE_WB={'installation':"memorialprinces.bike", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103128046/"}

MEMORIAL_19_PED_EB={'installation':"yycwalk.memorialnineteen", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101128047/"}
MEMORIAL_19_PED_WB={'installation':"yycwalk.memorialnineteen", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102128047/"}
MEMORIAL_19_EB={'installation':"memorialnineteen.bike", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103128047/"}
MEMORIAL_19_WB={'installation':"memorialnineteen.bike", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/104128047/"}

LINDSAY_PED_NB={'installation':"yycwalk.lindsay", 'direction':"northbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102128048/"}
LINDSAY_PED_SB={'installation':"yycwalk.lindsay", 'direction':"southbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101128048/"}
LINDSAY_NB={'installation':"lindsay.bike", 'direction':"northbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/104128048/"}
LINDSAY_SB={'installation':"lindsay.bike", 'direction':"southbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103128048/"}

TENTH_NB={'installation':"tenthst", 'direction':"northbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102020661/"}
TENTH_SB={'installation':"tenthst", 'direction':"southbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101020661/"}

SBOW_10_PED_EB={'installation':"yycwalk.sbowten", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102030402/"}
SBOW_10_PED_WB={'installation':"yycwalk.sbowten", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101030402/"}
SBOW_10_EB={'installation':"sbowten.bike", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/104030402/"}
SBOW_10_WB={'installation':"sbowten.bike", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103030402/"}

WET_PED_EB={'installation':"yycwalk.wet", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101130911/"}
WET_PED_WB={'installation':"yycwalk.wet", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102130911/"}
WET_EB={'installation':"wet.bike", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103130911/"}
WET_WB={'installation':"wet.bike", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/104130911/"}

EDM_NB={'installation':"edmtr", 'direction':"northbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102033550/"}
EDM_SB={'installation':"edmtr", 'direction':"southbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101033550/"}

NOSE_HILL_PED_SB={'installation':"yycwalk.nosehill", 'direction':"southbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101134303/"}
NOSE_HILL_PED_NB={'installation':"yycwalk.nosehill", 'direction':"northbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102134303/"}
NOSE_HILL_SB={'installation':"nosehill.bike", 'direction':"southbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103134303/"}
NOSE_HILL_NB={'installation':"nosehill.bike", 'direction':"northbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103134303/"}

PARKDALE_PED_EB={'installation':"yycwalk.parkdale", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101134305/"}
PARKDALE_PED_WB={'installation':"yycwalk.parkdale", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102134305/"}
PARKDALE_EB={'installation':"parkdale.bike", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103134305/"}
PARKDALE_WB={'installation':"parkdale.bike", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103134305/"}

NGLENMORE_PED_EB={'installation':"yycwalk.nglenmore", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101134306/"}
NGLENMORE_PED_WB={'installation':"yycwalk.nglenmore", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102134306/"}
NGLENMORE_EB={'installation':"nglenmore.bike", 'direction':"eastbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103134306/"}
NGLENMORE_WB={'installation':"nglenmore.bike", 'direction':"westbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103134306/"}

SGLENMORE_PED_NB={'installation':"yycwalk.sglenmore", 'direction':"northbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101134304/"}
SGLENMORE_PED_SB={'installation':"yycwalk.sglenmore", 'direction':"southbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102134304/"}
SGLENMORE_NB={'installation':"sglenmore.bike", 'direction':"northbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103134304/"}
SGLENMORE_SB={'installation':"sglenmore.bike", 'direction':"southbound", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/103134304/"}

for i in [ PB_NB, PB_SB, PB_PED_NB, PB_PED_SB, SEVEN_NB, SEVEN_SB, STEPHEN_PED, STEPHEN_CAR, STEPHEN_BIKE, FIFTH_5_NB, FIFTH_5_SB, FIFTH_10_NB, FIFTH_10_SB, FIFTH_15_NB, FIFTH_15_SB, TWELFTH_8_EB, TWELFTH_8_WB, TWELFTH_2_EB, TWELFTH_2_WB, TWELFTH_3_EB, TWELFTH_3_WB, NINTH_4_EB, NINTH_4_WB, EIGHTH_8_EB, EIGHTH_8_WB, EIGHTH_3_EB, EIGHTH_3_WB, RIVERWALK_PED_EB, RIVERWALK_PED_WB, RIVERWALK_EB, RIVERWALK_WB, NOSECREEK_BOW_PED_NB, NOSECREEK_BOW_PED_SB, NOSECREEK_BOW_NB, NOSECREEK_BOW_SB, MEMORIAL_PRINCE_PED_EB, MEMORIAL_PRINCE_PED_WB, MEMORIAL_PRINCE_EB, MEMORIAL_PRINCE_WB, MEMORIAL_19_PED_EB, MEMORIAL_19_PED_WB, MEMORIAL_19_EB, MEMORIAL_19_WB, LINDSAY_PED_NB, LINDSAY_PED_SB, LINDSAY_NB, LINDSAY_SB, TENTH_NB, TENTH_SB, SBOW_10_PED_EB, SBOW_10_PED_WB, SBOW_10_EB, SBOW_10_WB, WET_PED_EB, WET_PED_WB, WET_EB, WET_WB, EDM_NB, EDM_SB, NOSE_HILL_PED_NB, NOSE_HILL_PED_SB, NOSE_HILL_NB, NOSE_HILL_SB, PARKDALE_PED_EB, PARKDALE_PED_WB, PARKDALE_EB, PARKDALE_WB, NGLENMORE_PED_EB, NGLENMORE_PED_WB, NGLENMORE_EB, NGLENMORE_WB, SGLENMORE_PED_NB, SGLENMORE_PED_SB, SGLENMORE_NB, SGLENMORE_SB ]:
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

