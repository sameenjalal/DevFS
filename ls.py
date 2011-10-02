# o_auth stuff
# import w/e
# cloudmine integration

import sys
sys.path.append("/home/samjalal/sameenjalal.com/DevFS/requests-0.6.1")
import requests
import simplejson as json

username = sys.argv[1]
if len(sys.argv)<2:
    sys.argv[2] = 10

count = sys.argv[2]

var = "http://twitter.com/status/user_timeline/" + username + ".json?count=" + str(count)

r=requests.get(var)

random_thing = json.loads(r.content)
x=0
#while (x < count):
ran_string=random_thing[1]['created_at']
print(ran_string[4:16]+" " +random_thing[1]['text'])


