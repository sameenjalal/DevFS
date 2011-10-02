#!/usr/bin/python

import urllib2
import urllib

#from io import BytesIO
import io
import gzip
import time
import ssl
import cookielib
import sys
import getpass

TWITTER_MAX = 140
arg1 = sys.arg[1]
arg2 = sys.arg[2]

headers = {'Accept': 'application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
'User-Agent': 'Mozilla/5.0',
'Accept-Encoding': 'gzip,deflate,sdch',
'Accept-Language': 'en-US,en;q=0.8',
'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Proxy-Connection' : 'keep-alive'
}

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
req2 = urllib2.Request("https://twitter.com/login", headers=headers)
response2 = opener.open(req2)
cj.extract_cookies(response2,req2)



buf = BytesIO(response2.read())
unziped = gzip.GzipFile(mode = 'rb', fileobj = buf )
login_html = unziped.read().decode('utf-8')
login_html_lines = login_html.split('\n')

for i in range(len(login_html_lines)-1):
	if(login_html_lines[i].find("<form action=\"https:") != -1):
		authenticity_token = login_html_lines[i].split("value=")[1].split(" ")[0].strip("\"")

headers['Referer'] = 'https://twitter.com/login'
headers['Cache-Control'] = 'max-age=0'
headers['Origin'] = 'https://twitter.com'
headers['Content-Type'] = 'application/x-www-form-urlencoded'



USERNAME = arg1
PASSWORD = arg2
uname = urllib.quote(USERNAME)
pword = urllib.quote(PASSWORD)

url_vars1 = 'authenticity_token=' + authenticity_token + '&authenticity_token=' + authenticity_token + '&return_to_ssl=&redirect_after_login=&session%5Busername_or_email%5D=' + uname + '&session%5Bpassword%5D=' + pword + '&commit=Sign+In'



content_length = len(url_vars1)
headers['Content-Length'] = str(content_length)
url1 = 'https://twitter.com/sessions'

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
req3 = urllib2.Request(url1, data=url_vars1, headers=headers)
response3 = opener.open(req3)
cj.extract_cookies(response3,req3)


buf2 = BytesIO(response3.read())
unziped2 = gzip.GzipFile(mode = 'rb', fileobj = buf2 )
html2 = unziped2.read().decode('utf-8')
html_lines2 = html2.split('\n')

page3 = str(response3.info()).split('\n')
post_authenticity_token = ''

for i in html_lines2:
	if(i.find("<input id=\"password\"") != -1 ):
		sys.exit("\nBad username and/or password.\n")

for i in html_lines2:
        if(i.find('false},"postAuthenticityToken":') != -1):
                post_authenticity_token = i.split('false},"postAuthenticityToken":')[1].split(',"deciderFeatures"')[0].strip('"')

headers = {
'Host': 'api.twitter.com',
'Origin': 'https://api.twitter.com',
'Accept-Language': 'en-US,en;q=0.8',
'Proxy-Connection': 'keep-alive',
'Accept': 'application/json, text/javascript, */*',
'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.44 Safari/534.13',
'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'X-Requested-With': 'XMLHttpRequest',
'X-PHX' : 'true',
'Referer': 'https://api.twitter.com/reciever.html',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip,deflate,sdch'
}

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
try:
	while(True):
		message = "Does this work?"
		message_proper = urllib.quote(message)
		url_vars2 = 'include_entities=true&status=' + message_proper + '&post_authenticity_token=' + post_authenticity_token
		req = urllib2.Request('https://api.twitter.com/1/statuses/update.json', url_vars2, headers)
		response = opener.open(req)

except KeyboardInterrupt:
	sys.exit("\nHave a good day.\n")
else:
	sys.exit("\nSomething bad happened.\n")
