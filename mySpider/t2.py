from urllib import parse
from urllib.request import Request,urlopen
#

ua='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'


# base_url='http://cn.bing.com/search'
# dic={'q':'马哥教育'}
# u=parse.urlencode(dic)
# print(u)
# url='{}?{}'.format(base_url,u)
# print(url)
# url_source=parse.unquote(url)
# print(url_source)
#
# from urllib.request import urlopen,Request
# ua='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
#
# req=Request(url,headers={
#     'User-agent':ua
# })
#
# with urlopen(req) as res:
#     print(res.status)
#     print(res.info)
#     with open('d:/bing.html','wb+') as f:
#         f.write(res.read())
#         f.flush()



url='http://httpbin.org/'#非常著名的网站，可以测试各种http
url=url+'post'
import simplejson
req=Request(url,headers={
    'User-agent':ua
})
data={'name':'张三%￥￥$@@','age':6}
data_encode=parse.urlencode(data)
print(data_encode)
res=urlopen(req,data=data_encode.encode())
with res:
    text=res.read()
    print(text)
    d=simplejson.loads(text)
    print(d)
    print(type(d))