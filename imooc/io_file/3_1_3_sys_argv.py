#!/usr/bin/env python
#coding=utf-8

# 3.文件属性及OS模块使用
# http://www.imooc.com/video/8043


import sys


if __name__ == "__main__":
    print("argv length : %d" % len(sys.argv))
    for arg in sys.argv:
        print(arg)


# run in terminal command : python 3_1_3_sys_argv.py 0 1 2

