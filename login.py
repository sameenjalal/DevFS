import sys
import urllib2

arg1 = sys.argv[1]
arg2 = sys.argv[2]

dict = {}

# HEADERS
dict["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
dict["Accept-Charset"] = ":ISO-8859-1,utf-8;q=0.7,*;q=0.3"
dict["Accept-Encoding"] = "gzip,deflate,sdch"
dict["Accept-Language"] = "en-US,en;q=0.8"
dict["Cache-Control"] = "max-age=0"
dict["Connection"] = "keep-alive"
dict["Content-Length"] = "427"
dict["Content-Type"] = "application/x-www-form-urlencoded"
dict["Cookie"] = "guest_id=v1%3A1309235540650345; js=1; k=10.35.19.120.1317517659359703; original_referer=ZLhHHTiegr%2BUxdELy7AFpRY8L5POVoY7FM0SNxcA5L7LmfUGIP85LXpR1mv3%2BPQTbPMIOPoyeIo1jveE%2F%2FY8U9j9RZq2CIgFb1HQ8QWwgG6prY3BW6NJudRKN0othUvuML7MZ3ATqRM%3D; twll=l%3D1317529067; __utma=43838368.2062142153.1306895221.1317523394.1317527782.9; __utmb=43838368.12.10.1317527782; __utmc=43838368; __utmz=43838368.1317527782.9.8.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=twitter; __utmv=43838368.lang%3A%20en; _twitter_sess=BAh7CjoPY3JlYXRlZF9hdGwrCPu63MIyAToVaW5fbmV3X3VzZXJfZmxvdzA6%250ADGNzcmZfaWQiJTkyMzFhOWYwYjc5MTY4MGYzMDVmYzQ3ZDQ1Y2I5NmJlIgpm%250AbGFzaElDOidBY3Rpb25Db250cm9sbGVyOjpGbGFzaDo6Rmxhc2hIYXNoewAG%250AOgpAdXNlZHsAOgdpZCIlN2ZhOWQ4OWFkNDJhNTYwMGIzMDNhMjVjMTI0MTQ1%250AZjg%253D--d58d708077874aff5d134d2684cfd489f1a012c5"
dict["Host"] = "twitter.com"
dict["Origin"] = "http://twitter.com"
dict["Referer"] = "http://twitter.com/"
dict["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.187 Safari/535.1"

# DATA
user = "session%5Busername_or_email%5D=samjalal"
password = "session%5Bpassword%5D=akash123"
extra = "scribe_log=[\"{\"event_name\":\"web:front:login_callout:form:login_click\",\"noob_level\":null,\"internal_referer\":null,\"user_id\":0,\"page\":\"front\",\"_category_\":\"client_event\",\"ts\":1317529268186}\"]"

url_data = user + "&" + password + "&" + extra

response = urllib2.Request(url="https://twitter.com/sessions?phx=1?",data=url_data, headers=dict)
print response
