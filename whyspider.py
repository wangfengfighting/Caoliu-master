# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：whyspider.py
#   版本：0.2
#   作者：why
#   日期：2014-04-18
#   语言：Python 2.7.5
#
#   版本列表：
#   0.1：添加GET和POST
#   0.2：添加模拟头的功能
#---------------------------------------

import urllib  
import urllib2
import cookielib
import re
import string
import time

class WhySpider:
    
    # 初始化爬虫  
    def __init__(self):
        self.cookie_jar = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie_jar))
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0'}

    # 发送GET请求
    def send_get(self,get_url):
        result = ""
        #time1= time.time()
        #while time.time()-time1>10:
        try:
            my_request = urllib2.Request(url = get_url, headers = self.headers)
            result = self.opener.open(my_request).read()
        except Exception,e:
            print "Exception : ",e

        #response = urllib2.urlopen('http://ipoock.com/img/g4/201512242250036siyu.jpeg', timeout=100)
        return result

    # 发送POST请求
    def send_post(self,post_url,post_data):
        result = ""
        try:
            my_request = urllib2.Request(url = post_url,data = post_data, headers = self.headers)
            result = self.opener.open(my_request).read()
        except Exception,e:
            print "Exception : ",e
        return result

    # 模拟电脑
    def set_computer(self):
        user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0'
        self.headers = { 'User-Agent' : user_agent }    
        
    # 模拟手机
    def set_mobile(self):
        user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25'
        self.headers = { 'User-Agent' : user_agent }    
