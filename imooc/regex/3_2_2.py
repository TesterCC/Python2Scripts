#!/usr/bin/env python
#coding=utf-8

# http://www.imooc.com/video/10509

import re

ma = re.match(r'[_a-zA-Z]+[_\w]*','10')
print ma

ma2 = re.match(r'[_a-zA-Z]+[_\w]*','_ht22')
print ma2.group()
