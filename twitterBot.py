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

SEVEN_NB="http://www.eco-public.com/api/h7q239dd/data/periode/101017181/?begin=" + yesterday + "&end=" + yesterday + "&step=4"
PB_NB="http://www.eco-public.com/api/h7q239dd/data/periode/101018487/?begin=" + yesterday + "&end=" + yesterday + "&step=4"
SEVEN_SB="http://www.eco-public.com/api/h7q239dd/data/periode/102017181/?begin=" + yesterday + "&end=" + yesterday + "&step=4"
PB_SB="http://www.eco-public.com/api/h7q239dd/data/periode/102018487/?begin=" + yesterday + "&end=" + yesterday + "&step=4"

# 1 = Ped, 2 = Bike, 3 = Car
STEPHEN="http://www.eco-public.com/api/h7q239dd/data/periode/102017165/?begin=" + yesterday + "&end=" + yesterday + "&step=4"

# Peace Bridge
response = urllib2.urlopen(PB_NB)
json_data = response.read()
nb = json.loads(json_data)[0]['comptage']

response = urllib2.urlopen(PB_SB)
json_data = response.read()
sb = json.loads(json_data)[0]['comptage']

total = nb + sb

count_status="%d trips on the Peace Bridge yesterday.\n\n%d NB, %d SB\n#yycbike" % (total, nb, sb)
print count_status

t.statuses.update(
	status=count_status)

# 7th Street

response = urllib2.urlopen(SEVEN_NB)
json_data = response.read()
nb = json.loads(json_data)[0]['comptage']

response = urllib2.urlopen(SEVEN_SB)
json_data = response.read()
sb = json.loads(json_data)[0]['comptage']

total = nb + sb

count_status="%d trips on 7th Street yesterday.\n\n%d NB, %d SB\n#yycbike" % (total, nb, sb)
print count_status

t.statuses.update(
	status=count_status)

# Stephen Ave

response = urllib2.urlopen(STEPHEN)
json_data = response.read()
total = json.loads(json_data)[0]['comptage']

count_status="%d trips on Stephen Ave. yesterday.\n\n#yycbike" % (total)
print count_status

t.statuses.update(
	status=count_status)
