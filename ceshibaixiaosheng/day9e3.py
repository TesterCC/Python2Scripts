# !/usr/bin/env python
# coding:utf-8

# http://bblove.me/2015/05/23/python-requests-login-csdn-blog/

import requests

# 使用beautifulsoup来处理获取的html内容，这个库需要安装，还是使用pip install beautifulsoup4来安装

from bs4 import BeautifulSoup as bs  # 使用beautifulsoup来处理获取的html内容，这个库需要安装，还是使用pip install beautifulsoup4来安装

import time
import os

from cookielib import LWPCookieJar


def toJson(str):
    '''
    提取lt流水号，将数据化为一个字典
    '''

    soup = bs(str)
    tt={}
    for inp in soup.form.find_all('input'):
        if inp.get('name') != None:
            tt[inp.get('name')] = inp.get('value')
    return tt

# cookie setting
s = requests.Session()
s.cookies = LWPCookieJar('cookiejar')
header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}
if not os.path.exists('cookiejar'):
    print "there is no cookie,setting"
    r = s.get("http://passport.csdn.net/account/login")
    soup = toJson(r.text)
    # payload ={'username':'jackroyal','password':'123456','lt':soup["lt"],'execution':'e1s1','_eventId':'submit'}
    payload ={'username':'detective_ling','password':'-D.L.00.01-','lt':soup["lt"],'execution':'e1s1','_eventId':'submit'}


    print payload
    r = s.post("http://passport.csdn.net/account/login",data=payload,headers=header)
    s.cookies.save(ignore_discard=True)

    print r.text
else:
    print "cookie exists,restore"
    s.cookies.load(ignore_discard=True)


# r = s.get("https://passport.csdn.net/content/loginbox/loginapi.js")
r = s.get("http://write.blog.csdn.net/postlist",headers=header)
print r.text
