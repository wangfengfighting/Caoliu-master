# coding: utf-8
__author__ = 'Administrator'
from DecodeHTML import *
import whyspider
import getAllPageLink
import os
import time
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
            #print(picurl,'-------')
            if len(picurl)>0:
                print('开始下载......')
                #print((picurl))
                num=0
                for urlindex in range(len(picurl)):
                    url=picurl[urlindex]
                    print(url)
                    finame=url.split('/')[-1]
                    filepath='J:\\caoliu\\{0}'.format(sinlink.split('/')[-1])
                    #print(filepath)
                    if os.path.isdir(filepath):
                        pass
                    else:
                        os.mkdir(filepath)
                    name=filepath+'\\'+finame
                    f = open(name,'wb')
                    data= my_spider.send_get(url)
                    print('get data')
                    if not data.strip():
                        print('NULL'+'剩余'+str(len(picurl)-urlindex))
                        print('结束空')
                    else:
                        print('开始-----')
                        f.write(data)
                        f.close()
                        print('下载了'+str(num)+'剩余'+str(len(picurl)-urlindex))

                    num+=1
                    time.sleep(5)
                    print('结束这一轮')


if __name__=='__main__':
    downall()

