#coding=utf-8
#-*- coding: UTF-8 -*-
import urllib
# import socket
import time
import urllib2
import os
from bs4 import BeautifulSoup

#---------------------V1.3图片板块版----------------------#
#可以过滤指定作者的作品    http://www.cl529.com/index.php    http://www.cl529.com/thread0806.php?fid=16

_img_pre = ''
_headers = {'User-Agent':'Mozilla/5.0'};
_data = ''
_pageStart = 1
_pageEnd = 2
_localUrl = 'http://www.cl529.com/'
_encode = 'gbk'

def findUrl():
    global _data
    global _headers
    global _pageStart
    global _pageEnd
    global _localUrl
    global _encode
    
    for pageNo in range(_pageStart, _pageEnd):
        url = _localUrl + 'thread0806.php?fid=16&page=' + pageNo.__str__()
        print 'Search Url:', url
        # 设置请求参数
        req = urllib2.Request(url, _data, _headers)
        # 打开网站代码
        data = urllib2.urlopen(req)
        soup = BeautifulSoup(data, from_encoding=_encode)
        
        
        trs = soup.findAll('tr', {'class':'tr3 t_one'})
        for tr in trs:
            author = tr.find('a', {'class':'bl'}).string
            url = tr.find('a', {'title':'打開新窗口'})['href'].__str__()
            # list中移除需要被过滤的作者
            # list中移除需要被过滤的作者
            if author.find('第六天') == -1 and url.find('1502') != -1:
                print '-----------------------------author:[' + author + ']-----------------------------'
                downUrl = _localUrl + url
                print 'Accept down url:[' + downUrl + ']'
                date(downUrl, author)
        
        
#         downs = soup.findAll('a', {'title':'打开新窗口'})
#         for down in downs:
#             downUrl = _localUrl + down['href'].__str__()
#             if downUrl.find('1308') == -1:
#                 print 'Except url:', downUrl
#                 continue
#             print '--------------------------------------------------------------------'
#             print 'Accept down url:', downUrl
#             date(downUrl)
            
def date(url, author):
    global _data
    global _headers
    global _encode
    # 设置超时，有的图片下不动，需要逃过去
    #socket.setdefaulttimeout(10)
    # 设置请求参数
    req = urllib2.Request(url, _data, _headers)
    # 打开网站代码
    data = urllib2.urlopen(req)
    time.sleep(3)
    soup = BeautifulSoup(data, from_encoding = _encode)
    # 按照URL地址的最终目录数创建文件夹
    url = url[-12:]
    title = soup.title.string.replace('  草榴社區  - powered by phpwind.net','') + '+' + url
    title = title.replace('/','-').replace(':','-')
    title = '[' + author + ']' + title
#     print title
    new_path = os.path.join(os.path.abspath("./down/"), title).decode('utf-8')
    if not os.path.isdir(new_path):
        try:
            os.makedirs(new_path)
        except:
            print '.......................  Except! :(  .......................'
        imgs = soup.findAll('img', {'style':'cursor:pointer'})
        down(imgs, new_path)
    else:
        print ':::::::This url:[[' + url + ']] is downed!:::::::'

def down(imgs, new_path):
    global _img_pre
    # 遍历地址列表，保存图片
    i = 0
    j = 0
    for img in imgs:
        # 这个处理链接异常
        img = img['src'].__str__()
        if len(img) < 100:
            # 因为保存的是<imag src....>的格式，需要重http://格式引用
#             print '--------------------------------------------------------------------'
            print "Image url:", img
            # 如果超时了，就输出time out
            try:
                if img[-30:] == _img_pre:
                    print "[Repeat IMGURL]:" + img
#                     print '--------------------------------------------------------------------'
                    continue
                i += 1
                imgName = i.__str__() + img[-7:]
                local = os.path.join(new_path, imgName)
                # 这个是保存函数，第一个参数是地址，第二个是保存的文件名，让地址的倒数8位，当做文件名
                class AppURLopener(urllib.FancyURLopener):
                    version = "Mozilla/5.0"
                urllib._urlopener = AppURLopener()
                urllib.urlretrieve(img, local)
                j += 1
                print 'Success download image[ ' + imgName + ' ]to ' + new_path[-11:]
#                 print '--------------------------------------------------------------------'
                _img_pre = img[-30:]
            except:
                print 'Time out or download fail!'
                i -= 1
    print 'Success down NUM[' + j.__str__() + ']'

def main():
    findUrl()
    print '***************************【END】***************************'
    #date()
if __name__ == '__main__':
    main()



# #coding=utf-8
# #-*- coding: UTF-8 -*-
# import urllib
# # import socket
# import time
# import urllib2
# import os
# from bs4 import BeautifulSoup
# 
# #---------------------V1.2下载优化版----------------------#
# #可以过滤指定作者的作品
# 
# _img_pre = ''
# _headers = {'User-Agent':'Mozilla/5.0'};
# _data = ''
# _pageStart = 1
# _pageEnd = 2
# _localUrl = 'http://www.t66y.com/'
# _encode = 'gbk'
# 
# def findUrl():
#     global _data
#     global _headers
#     global _pageStart
#     global _pageEnd
#     global _localUrl
#     global _encode
#     
#     for pageNo in range(_pageStart, _pageEnd):
#         url = _localUrl + 'thread0806.php?fid=2&page=' + pageNo.__str__()
#         print 'Search Url:', url
#         # 设置请求参数
#         req = urllib2.Request(url, _data, _headers)
#         # 打开网站代码
#         data = urllib2.urlopen(req)
#         soup = BeautifulSoup(data, from_encoding=_encode)
#         
#         
#         trs = soup.findAll('tr', {'class':'tr3 t_one'})
#         for tr in trs:
#             author = tr.find('a', {'class':'bl'}).string
#             url = tr.find('a', {'title':'打開新窗口'})['href'].__str__()
#             # list中移除需要被过滤的作者
#             # list中移除需要被过滤的作者
#             if author.find('第六天') == -1 and url.find('1412') != -1:
#                 print '-----------------------------author:[' + author + ']-----------------------------'
#                 downUrl = _localUrl + url
#                 print 'Accept down url:[' + downUrl + ']'
#                 date(downUrl, author)
#         
#         
# #         downs = soup.findAll('a', {'title':'打开新窗口'})
# #         for down in downs:
# #             downUrl = _localUrl + down['href'].__str__()
# #             if downUrl.find('1308') == -1:
# #                 print 'Except url:', downUrl
# #                 continue
# #             print '--------------------------------------------------------------------'
# #             print 'Accept down url:', downUrl
# #             date(downUrl)
#             
# def date(url, author):
#     global _data
#     global _headers
#     global _encode
#     # 设置超时，有的图片下不动，需要逃过去
#     #socket.setdefaulttimeout(10)
#     # 设置请求参数
#     req = urllib2.Request(url, _data, _headers)
#     # 打开网站代码
#     data = urllib2.urlopen(req)
#     time.sleep(3)
#     soup = BeautifulSoup(data, from_encoding = _encode)
#     # 按照URL地址的最终目录数创建文件夹
#     url = url[-12:]
#     title = soup.title.string.replace('  草榴社區  - powered by phpwind.net','') + '+' + url
#     title = title.replace('/','-').replace(':','-')
#     title = '[' + author + ']' + title
# #     print title
#     new_path = os.path.join(os.path.abspath("./down/"), title).decode('utf-8')
#     if not os.path.isdir(new_path):
#         try:
#             os.makedirs(new_path)
#         except:
#             print '.......................  Except! :(  .......................'
#         imgs = soup.findAll('img', {'style':'cursor:pointer'})
#         down(imgs, new_path)
#     else:
#         print ':::::::This url:[[' + url + ']] is downed!:::::::'
# 
# def down(imgs, new_path):
#     global _img_pre
#     # 遍历地址列表，保存图片
#     i = 0
#     j = 0
#     for img in imgs:
#         # 这个处理链接异常
#         img = img['src'].__str__()
#         if len(img) < 100:
#             # 因为保存的是<imag src....>的格式，需要重http://格式引用
# #             print '--------------------------------------------------------------------'
#             print "Image url:", img
#             # 如果超时了，就输出time out
#             try:
#                 if img[-30:] == _img_pre:
#                     print "[Repeat IMGURL]:" + img
# #                     print '--------------------------------------------------------------------'
#                     continue
#                 i += 1
#                 imgName = i.__str__() + img[-7:]
#                 local = os.path.join(new_path, imgName)
#                 # 这个是保存函数，第一个参数是地址，第二个是保存的文件名，让地址的倒数8位，当做文件名
#                 class AppURLopener(urllib.FancyURLopener):
#                     version = "Mozilla/5.0"
#                 urllib._urlopener = AppURLopener()
#                 urllib.urlretrieve(img, local)
#                 j += 1
#                 print 'Success download image[ ' + imgName + ' ]to ' + new_path[-11:]
# #                 print '--------------------------------------------------------------------'
#                 _img_pre = img[-30:]
#             except:
#                 print 'Time out or download fail!'
#                 i -= 1
#     print 'Success down NUM[' + j.__str__() + ']'
# 
# def main():
#     findUrl()
#     print '***************************【END】***************************'
#     #date()
# if __name__ == '__main__':
#     main()


#---------------------V1.0----------------------#
# #coding=utf-8
# #-*- coding: UTF-8 -*-
# import urllib
# import socket
# import urllib2
# import os
# from bs4 import BeautifulSoup
# 
# _img_pre = ''
# _headers = {'User-Agent':'Mozilla/5.0'};
# _data = ''
# _pageStart = 1
# _pageEnd = 2
# _localUrl = 'http://www.t66y.com/'
# 
# def findUrl():
#     global _data
#     global _headers
#     global _pageStart
#     global _pageEnd
#     global _localUrl
#     
#     for pageNo in range(_pageStart, _pageEnd):
#         url = _localUrl + 'thread0806.php?fid=2&page=' + pageNo.__str__()
#         print 'Search Url:', url
#         # 设置请求参数
#         req = urllib2.Request(url, _data, _headers)
#         # 打开网站代码
#         data = urllib2.urlopen(req)
#         soup = BeautifulSoup(data, from_encoding='gb2312')
#         downs = soup.findAll('a', {'title':'打开新窗口'})
#         for down in downs:
#             downUrl = _localUrl + down['href'].__str__()
#             if downUrl.find('1308') == -1:
#                 print 'Except url:', downUrl
#                 continue
#             print '--------------------------------------------------------------------'
#             print 'Accept down url:', downUrl
#             date(downUrl)
#             
# def date(url):
#     global _data
#     global _headers
#     # 引号内的为网址
#     print url
#     # 按照URL地址的最终目录数创建文件夹
#     new_path = os.path.join(os.path.abspath("./"), url[-11:])
#     if not os.path.isdir(new_path):
#         os.makedirs(new_path)
#     # 设置超时，有的图片下不动，需要逃过去
#     #socket.setdefaulttimeout(10)
#     # 设置请求参数
#     req = urllib2.Request(url, _data, _headers)
#     # 打开网站代码
#     data = urllib2.urlopen(req)
#     soup = BeautifulSoup(data, from_encoding='gb2312')
#     imgs = soup.findAll('img', {'style':'cursor:pointer'})
#     down(imgs, new_path)
# 
# def down(imgs, new_path):
#     global _img_pre
#     # 遍历地址列表，保存图片
#     i = 0
#     j = 0
#     for img in imgs:
#         # 这个处理链接异常
#         img = img['src'].__str__()
#         if len(img) < 100:
#             # 因为保存的是<imag src....>的格式，需要重http://格式引用
#             print '--------------------------------------------------------------------'
#             print "Image url:", img
#             # 如果超时了，就输出time out
#             try:
#                 if img[-30:] == _img_pre:
#                     print "图片地址重复，不必下载"
#                     print '--------------------------------------------------------------------'
#                     continue
#                 i += 1
#                 imgName = i.__str__() + img[-7:]
#                 local = os.path.join(new_path, imgName)
#                 # 这个是保存函数，第一个参数是地址，第二个是保存的文件名，让地址的倒数8位，当做文件名
#                 class AppURLopener(urllib.FancyURLopener):
#                     version = "Mozilla/5.0"
#                 urllib._urlopener = AppURLopener()
#                 urllib.urlretrieve(img, local)
#                 j += 1
#                 print 'Success download image[ ' + imgName + ' ]to ' + new_path[-11:]
#                 print '--------------------------------------------------------------------'
#                 _img_pre = img[-30:]
#             except:
#                 print 'Time out or download fail!'
#                 i -= 1
#     print 'Success down NUM[' + j.__str__() + ']'
# 
# def main():
#     findUrl()
#     #date()
# if __name__ == '__main__':
#     main()







#---------------------V0.1----------------------#
#                 data = urllib2.urlopen(img)
#                 jpg = data.read()
#                 fp = open(local, 'wb')
#                 fp.write(jpg)
#                 fp.close()

# def date():
#     global _data
#     global _headers
#     # 页码开始
#     pageUp = 947597
#     # 页码结束
#     pageDown = 947598
#     for pageNo in range(pageUp, pageDown):
#         # 引号内的为网址
#         url = 'http://1024go.tk/htm_data/2/1308/' + pageNo.__str__() + '.html'
#         print url
#         # 按照URL地址的最终目录数创建文件夹
#         new_path = os.path.join(os.path.abspath("./"), pageNo.__str__() + '.html')
#         if not os.path.isdir(new_path):
#             os.makedirs(new_path)
#         # 设置超时，有的图片下不动，需要逃过去
#         #socket.setdefaulttimeout(10)
#         # 设置请求参数
#         req = urllib2.Request(url, _data, _headers)
#         # 打开网站代码
#         data = urllib2.urlopen(req)
#         soup = BeautifulSoup(data, from_encoding='gb2312')
#         imgs = soup.findAll('img', {'style':'cursor:pointer'})
#         down(imgs, new_path)
