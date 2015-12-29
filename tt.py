# -*- coding:utf-8 -*-
__author__ = 'Administrator'
# import urllib.request
# path = "D:\\Download"
# url = "http://img.picuphost.com/img/upload/image/20151130/113000016301.jpeg"
# name ="D:\\download\\2.jpeg"
# #保存文件时候注意类型要匹配，如要保存的图片为jpg，则打开的文件的名称必须是jpg格式，否则会产生无效图片
# conn = urllib.request.urlopen(url)
# f = open(name,'wb')
# f.write(conn.read())
# f.close()
# print('Pic Saved!')
import whyspider
# 初始化爬虫对象
# my_spider = whyspider.WhySpider()
# # 模拟GET操作
# path="G:\PostgraduatePROJECT\Caoliu-master"
# fname='22.jpeg'
# path2 = path+'\\'+fname
# name='G:\\PostgraduatePROJECT\\Caoliu-master\\down\\22.jpeg'
# f = open(name,'wb')
# data= my_spider.send_get('http://img.picuphost.com/img/upload/image/20151130/113000016301.jpeg')
# f.write(data)
# f.close()

# # 模拟POST操作
# print my_spider.send_post('http://3.apitool.sinaapp.com/','why=PostString2333')
#
# # 模拟GET操作
# print my_spider.send_get('http://www.baidu.com/')
#
# # 切换到手机模式
# my_spider.set_mobile()
#
# # 模拟GET操作
# print my_spider.send_get('http://www.baidu.com/')
result = "fff ffff"
if not result.strip():
    print('null')
print(result)

for i in range(20):
    if i<22:
        print(i)
    elif i==14:
        break