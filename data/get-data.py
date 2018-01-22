from ir_webstats import constants as ct
from ir_webstats.client import iRWebStats
from ir_webstats.util import clean
from collections import OrderedDict
import json


user = ''
password = ''
irw = iRWebStats()
irw.login(user, password)
if irw.logged:
    print(
        "Logged in successfully")
if not irw.logged:
    print (
        "Couldn't log in to iRacing Membersite. Please check your credentials")
    exit()
    
# Get last race stats of user
r = irw.lastrace_stats()

print("\n")

# Parse lastrace_stats, get Subsession ID
#Get session data / grab ID / insert to Array / Reverse array list
session_data = []
for race in r:
    session_data.insert(0, race["subsessionID"])
session_data.reverse()
latest_session = session_data[0]
latest_session = str(latest_session)
s = irw.event_results(latest_session)

#print(s)

#dump data to file for JSON reading later
with open('race-data.json', 'w') as outfile:
    json.dump(s, outfile)

print("Latest race data created")