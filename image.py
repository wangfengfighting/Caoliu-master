#coding=utf-8
#-*- coding: UTF-8 -*-
import urllib
import socket
import urllib2
import re
 
def date():
    # 页码开始
    pageUp = 1
    # 页码结束
    pageDown = 2
    for pageNo in range(pageUp, pageDown):
        # 引号内的为网址
        #url = 'http://www.cl529.com/thread0806.php?fid=16&page-' + pageNo.__str__()
        url = "http://www.cl529.com/htm_data/16/1512/1775897.html"
        print url
        # 设置超时，有的图片下不动，需要逃过去
        socket.setdefaulttimeout(6)
        # 打开网站代码
        data = urllib2.urlopen(url).read()
        # 下面两句是正则表达式匹配网站源代码的图片(jpg和gif),还有png的没写，可以合并成一句话
        jpg_url = '<img src="http://.+\.jpg'
        # 保存匹配的图片http地址
        tuples = re.findall(jpg_url, data)
        down(tuples)
        print "第 ", pageNo, " 页执行完毕"

def down(tuples):
    # 遍历地址列表，保存图片
    for i in tuples:
        # 这个处理链接异常
        if len(i) < 100:
            # 因为保存的是<imag src....>的格式，需要重http://格式引用
            print i[10:]
            # 如果超时了，就输出time out
            try:
                temp = urllib2.urlopen(i[10:])
                # 这个是保存函数，第一个参数是地址，第二个是保存的文件名，让地址的倒数8位，当做文件名
                urllib.urlretrieve(i[10:], i[-8:])
                print(i[-8:])
            except:
                print 'time out'


if __name__ == '__main__':
    date()






















#gif_url = '<img src="http://.+\.gif'
#gif_tuples = re.findall(gif_url, data)
# for j in gif_tuples:
#     if len(j) < 100:
#         print j[10:]
#         try:
#             gif = urllib2.urlopen(j[10:])
#             urllib.urlretrieve(j[10:], j[-8:])
#         except:
#             print 'time out'