#!/usr/bin/env python
# coding=utf-8

# http://www.imooc.com/video/10509

import re

ma = re.match(r'[_a-zA-Z]+[_\w]*', '10')     # + 匹配一次或无限次
print ma     # None

ma2 = re.match(r'[_a-zA-Z]+[_\w]*', '_ht22')    # Success
# ma2 = re.match(r'[_a-zA-Z]+[_\w]*', 'thisht22')   # Success
# ma2 = re.match(r'[_a-zA-Z]+[_\w]*', '[ht22')    # Failed
print ma2.group()


