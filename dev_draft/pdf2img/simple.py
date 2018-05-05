#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/3 10:49'

"""
use Wand for pdf to images
http://docs.wand-py.org/en/latest/

Install:
pip install Wand -i https://pypi.douban.com/simple/

install other lib which needed

ref:
https://blog.csdn.net/wwj_748/article/details/78135879?utm_source=tuicool&utm_medium=referral

Python2 with error, but python3 passed
"""

from wand.image import Image


def convert_pdf_to_jpg(filename):
    with Image(filename=filename) as img:
        print('total pages = ', len(img.sequence))

        with img.convert('jpeg') as converted:
            converted.save(filename='image/page.jpeg')


if __name__ == '__main__':
    convert_pdf_to_jpg("test.pdf")
