# coding: utf-8
__author__ = 'Administrator'
from DecodeHTML import *
import whyspider
import getAllPageLink
import re
import os
from bs4 import BeautifulSoup
import urllib
import urllib2
def getHtml(urlnumber):
    url= 'http://www.cl547.com/thread0806.php?fid=16&search=&page={0}'.format(str(urlnumber))
    print url
    html = urllib.urlopen(url)
    scode = html.read()
    return scode
def getPagelink(source):
        images = re.findall(r'<a href="htm_data/.*?\.html',source)
        allLink=[]
        for i in images:
            link=i.split('"')[-1]
            allLink.append('http://www.cl547.com/'+link)
        filteralllink=allLink[14:]
        return filteralllink
if __name__=='__main__':
    my_spider = whyspider.WhySpider()
    allLink=getPagelink(getHtml(3))
    for i in allLink:
        print type(i),i
        source=getHtml(i)
        picurl=getImage(source)
        print(picurl)
        for url in picurl:
            print(url)
            finame=url.split('/')[-1]
            name='G:\\PostgraduatePROJECT\\Caoliu-master\\down\\{0}'.format(finame)
            f = open(name,'wb')
            data= my_spider.send_get(url)
            f.write(data)
            f.close()
            print('have down ******')