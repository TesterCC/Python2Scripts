#!/usr/bin/env python
#coding=utf-8

# 3.文件属性及OS模块使用
# http://www.imooc.com/video/8043

f = open('imooc.txt')

print("文件描述>>>%d" % f.fileno())
print("打开方式>>>%s" % f.mode)
print("是否关闭>>>%s" % f.closed)
print("编码类型>>>%s" % f.encoding)

# 其他的看官方文档





