#!/usr/bin/env python
# coding=utf-8

# python正则表达式语法（二）
# http://www.imooc.com/video/10509


import re


# ma = re.match(r'[A-Z][a-z]', "Aa")   # Success
# ma = re.match(r'[A-Z][a-z]', "A")    # Failed
# ma = re.match(r'[A-Z][a-z]*', "A")     # Success
# ma = re.match(r'[A-Z][a-z]*', "Aaskdjalsjdfl")     # Success display all
# ma = re.match(r'[A-Z][a-z]*', "1Aaskdjalsjdfl")     # Failed
ma = re.match(r'[A-Z][a-z]*', "Aa33skdjalsjdfl")     # Success  just Aa

print(ma.group())
print(ma.group(0))