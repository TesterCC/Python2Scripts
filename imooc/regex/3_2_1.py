#!/usr/bin/env python
# coding=utf-8


# http://www.imooc.com/video/10509

import re

ma = re.match(r'[A-Z][a-z]', 'Ab')

print ma.group()

ma1 = re.match(r'[A-Z][a-z]', 'A')
print ma1

ma2 = re.match(r'[A-Z][a-z]*', 'A')
print ma2
print ma2.group()

ma3 = re.match(r'[A-Z]*[a-z]*', 'AEFSExsdsexoi')
print ma3.group()
