# coding:utf-8
# !/usr/bin/env python
# http://www.cnblogs.com/kaituorensheng/archive/2012/08/14/2638935.html
# http://www.chuanyuebook.com/study_day?courseid=3&day=8&openid=oybJvwqmQsdB2T-P7DjAwTsvNNIU

import os
import os.path

rootdir = "/Users/TesterCC/Documents/20150720-notes"     # 指明被遍历的文件夹

for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for dirname in dirnames:    #输出文件夹信息
        print "parent is : " + parent
        print "dirname is : " + dirname

    for filename in filenames:    #输出文件信息
        print "parent is : " + parent
        print "filename is : " + filename

        print "The full name of the file is:\n" + os.path.join(parent,filename)  #输出文件路径信息
