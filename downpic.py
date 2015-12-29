# coding: utf-8
__author__ = 'Administrator'
from DecodeHTML import *
import whyspider
import getAllPageLink
import os
def begindown():
    my_spider = whyspider.WhySpider()
    source=getHtml('http://www.cl529.com/htm_data/16/1512/1775897.html')
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

def downall():
    my_spider = whyspider.WhySpider()
    for page in range(1,130):
        allLink=getAllPageLink.getPagelink(getAllPageLink.getHtml(page))
        for sinlink in allLink:#sinlink 每个连接下的网页
            #print('begin down ',sinlink)
            source=getHtml(sinlink)
            #print(source)
            picurl=getImage(source)
            print(picurl,'-------')
            if len(picurl)>0:
                print((picurl))
                for url in picurl:
                    finame=url.split('/')[-1]
                    filepath='D:\\caoliu\\{0}'.format(sinlink.split('/')[-1])
                    print(filepath)
                    if os.path.isdir(filepath):
                        pass
                    else:
                        os.mkdir(filepath)
                    name=filepath+'\\'+finame
                    f = open(name,'wb')
                    data= my_spider.send_get(url)
                    f.write(data)
                    f.close()


if __name__=='__main__':
    downall()

