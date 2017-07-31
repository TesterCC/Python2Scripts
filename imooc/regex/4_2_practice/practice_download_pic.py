#!/usr/bin/env python
# coding=utf-8

# http://www.imooc.com/video/10512
# python正则表达式练习

'''
抓取网页中的图片到本地：
1.抓取网页
2.获取图片地址
3.抓取图片内容并保存到本地
'''


import urllib2       # python3 need "import urllib.request"
import re

target_url = "http://www.imooc.com/course/list"
req = urllib2.urlopen(target_url)
buf = req.read()
# print(buf)


# picture url -- http://img.mukewang.com/549bda090001c53e06000338-240-135.jpg

# list_url = re.findall(r'src=.+\.jpg', buf)
list_url = re.findall(r'http:.+?\.jpg', buf)    # change to start with http:
# print(list_url)

# downlaod pics and save in local host
i = 0
for url in set(list_url):
    try:
        f = open("./4_2_practice/"+str(i)+'.jpg', 'w')   # 指定目录
        req = urllib2.urlopen(url)
        buf = req.read()
        f.write(buf)
        print("Finish downlaod picture: " + str(i+1))    # for debug, can comment
        i += 1
    except Exception, e:
        print(e.message)


# debug code -- need delete repetition
# i = 0
# # print(set(list_url))
# for url in set(list_url):
#     print(str(i)+"--"+url)
#     i += 1




