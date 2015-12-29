# coding: utf-8
__author__ = 'Administrator'
import re
import os
from bs4 import BeautifulSoup
import urllib
import urllib2
def getHtml(url):
        html = urllib.urlopen(url)
        scode = html.read()
        return scode
def getImage(source):
        #images = re.findall(r'input src=.*?img.picuphost.com/img/upload/image/.*?\.jpeg type="image"',source)
        #images = re.findall(r'input src="(.*\.jpeg)" type=',source)
        re2 = r'input src=.*?/.*?\.jp.g'
        imgre = re.compile(re2)
        images = re.findall(imgre,source)
        #print(images)
        x = 0
        pic=[]
        for i in images:
                picurl=i.replace("input src='",'')
                pic.append(picurl)
                #print(picurl)

                #print(picurl,type(picurl))
                # save_path = "c://downloads"
                # fileName = save_path + "\\{0}.jpg".format(str(x))
                # imgData = urllib2.urlopen(picurl).read()
                x+=1
        return pic
def getImage2(source):
        re2=r'src="http://.+?.jpeg"'
        imgre = re.compile(re2)
        images = re.findall(imgre,source)
        return images
def saveImg(imageURL):
    file=0
    for i in imageURL:

        urllib.urlretrieve(i)
        print(i)
        file+=1
if __name__=='__main__':
    #source=getHtml('http://www.cl529.com/htm_data/16/1512/1775897.html')
    source=getHtml('http://www.cl547.com/htm_data/16/1512/1767606.html')
    pic=getImage(source)
    #print(pic)
    #saveImg(pic)

    #input src="http://ipoock.com/img/g4/20151222040151e4u6a.jpeg" type="image"

    # t="input src='http://img.picuphost.com/img/upload/image/20151130/113000016301.jpeg"
    # url=t.replace("input src='",'')
    # print(url,type(url))

# source=getHtml('http://www.cl529.com/htm_data/16/1512/1775897.html')
# print(source)
# print getImage2(source)
# #src='http://img.picuphost.com/img/upload/image/20151130/113000016308.jpeg'
# x=re.findall(r'input src=.*?img.picuphost.com/img/upload/image/.*?\.jpeg',source)
# #x=re.findall(r'src=.*?img.picuphost.com/img/upload/image/.\d*?\.jpeg',source)
# for i in x:
#     print(i)
