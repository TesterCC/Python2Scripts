#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/7/18 15:44'

"""
抓网页数据经常遇到例如&gt;或者&nbsp;这种HTML转义符

将转义字符转回正常显示
"""

import HTMLParser

textd1 = "&lt;abc&gt;"

html_parser = HTMLParser.HTMLParser()

txt = html_parser.unescape(textd1)

print(txt)