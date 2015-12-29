# coding: utf-8
__author__ = 'Administrator'
import os
import urllib2
import urllib
import whyspider
os.chdir(r'd:\ftp')
url='http://www.cl547.com/url.php?u=http://www______rmdown______com/link______php?hash=15338e3d7ef10c9cf6b79bf98639202d53adb0e466a&z'
# data = urllib2.request.urlopen(url).read()
# with open('9b8900c771aedcd4e63e274a4de44a93.torrent', 'wb') as f:
#     f.write(data)
#     f.close()
response = urllib2.urlopen(url)
print response
my_spider = whyspider.WhySpider()
quist=my_spider.send_get(url)
print(quist)

res=urllib2.urlopen(url).read()
print(res)