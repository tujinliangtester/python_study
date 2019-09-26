from urllib.request import urlopen,Request
from http.client import  HTTPResponse
url='http://www.bing.com'
ua='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'

# req=Request(url,headers={'User-agent':ua})
req=Request(url)
req.add_header('User-agent',ua)

response=urlopen(url)

print(response.closed)

with response:
    print(type(response))
    print(response.status)
    print(response._method)
    print(response.read())
    print(response.geturl())
    print(response.info())

print(response.closed)