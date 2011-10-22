# o_auth stuff
# import w/e
# cloudmine integration

import sys
sys.path.append("/home/samjalal/sameenjalal.com/DevFS/requests-0.6.1")
import requests
import simplejson as json

username = sys.argv[1]
if len(sys.argv) < 2:
    count = 10
else:
	count = sys.argv[2]

var = "http://twitter.com/status/user_timeline/" + username + ".json?count=" + str(count)

r=requests.get(var)
random_thing = json.loads(r.content)
x=0
#print '\033[1;46mHighlighted Cyan like Caribbean\033[1;m'
#while (x < sys.argv[2]):
for x in random_thing:
    ran_string=x['created_at']
    print(ran_string[4:16]+" " +'\033[1;46m'+x['text']+'\033[1;m')
    
print
