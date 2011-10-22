import sys
import urllib2

arg1 = sys.argv[1]
arg2 = sys.argv[2]

dict_headers= {}

# HEADERS
dict_headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
dict_headers["Accept-Charset"] = ":ISO-8859-1,utf-8;q=0.7,*;q=0.3"
dict_headers["Accept-Encoding"] = "gzip,deflate,sdch"
dict_headers["Accept-Language"] = "en-US,en;q=0.8"
#dict_headers["Cache-Control"] = "max-age=0"
#dict_headers["Connection"] = "keep-alive"
dict_headers["Content-Type"] = "application/x-www-form-urlencoded"
dict_headers["Cookie"] = "guest_id=v1%3A1309235540650345; js=1; k=10.35.19.120.1317517659359703; original_referer=ZLhHHTiegr%2BUxdELy7AFpRY8L5POVoY7FM0SNxcA5L7LmfUGIP85LXpR1mv3%2BPQTbPMIOPoyeIo1jveE%2F%2FY8U9j9RZq2CIgFb1HQ8QWwgG6prY3BW6NJudRKN0othUvuML7MZ3ATqRM%3D; twll=l%3D1317529067; __utma=43838368.2062142153.1306895221.1317523394.1317527782.9; __utmb=43838368.12.10.1317527782; __utmc=43838368; __utmz=43838368.1317527782.9.8.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=twitter; __utmv=43838368.lang%3A%20en; _twitter_sess=BAh7CjoPY3JlYXRlZF9hdGwrCPu63MIyAToVaW5fbmV3X3VzZXJfZmxvdzA6%250ADGNzcmZfaWQiJTkyMzFhOWYwYjc5MTY4MGYzMDVmYzQ3ZDQ1Y2I5NmJlIgpm%250AbGFzaElDOidBY3Rpb25Db250cm9sbGVyOjpGbGFzaDo6Rmxhc2hIYXNoewAG%250AOgpAdXNlZHsAOgdpZCIlN2ZhOWQ4OWFkNDJhNTYwMGIzMDNhMjVjMTI0MTQ1%250AZjg%253D--d58d708077874aff5d134d2684cfd489f1a012c5"
dict_headers["Host"] = "twitter.com"
dict_headers["Origin"] = "http://twitter.com"
dict_headers["Referer"] = "http://twitter.com/"
dict_headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.187 Safari/535.1"

# DATA
user = "session%5Busername_or_email%5D=" + arg1
password = "session%5Bpassword%5D" + arg2
extra = urllib2.quote("scribe_log=[\"{\"event_name\":\"web:front:login_callout:form:login_click\",\"noob_level\":null,\"internal_referer\":null,\"user_id\":0,\"page\":\"front\",\"_category_\":\"client_event\",\"ts\":1317529268186}\"]")

url_data = user + "&" + password + "&" + extra

r= urllib2.Request(url="https://twitter.com/sessions?phx=1?",data=url_data, headers=dict_headers)
response = urllib2.urlopen(r)
#print type( (str)(response.read()) )
#print response
print urllib2.urlopen(url="http://twitter.com/#!/samjalal").read()

#buf = BytesIO(
