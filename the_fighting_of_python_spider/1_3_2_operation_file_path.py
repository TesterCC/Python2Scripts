#!/usr/bin/env python
# coding=utf-8

'''
Python爬虫开发与项目实战  P14
1.3.2 操作文件和目录
'''

import os, shutil

PATH = os.getcwd()
print(PATH)    # get current python script path

print(os.path.isfile(PATH))    # False  是否是一个文件
print(os.path.isdir(PATH))     # True   是否是一个目录
print(os.path.isabs(PATH))     # True   是否是绝对路径
print(os.path.exists(PATH))    # True   是否存在

# os.remove("testwrite.txt")   # delete file
# os.removedirs(r"D:\test")    # delete empty dirs

# 分离一个文件的目录名和文件名
sep = os.path.split(r"D:\testercc_github_code\Python2Scripts\the_fighting_of_python_spider\testwrite2.txt")
print(sep)

# 分离出扩展名
filename = "D:\testercc_github_code\Python2Scripts\the_fighting_of_python_spider\testwrite2.txt"
filename2 = "/test.doc"

print(os.path.splitext(filename)[1])    # 提取扩展名
print(os.path.splitext(filename2)[1])

filepath = os.getcwd()
print(os.path.dirname(filepath))     # get path name
print(os.path.basename(filepath))    # get file name, 所在文件夹name

# get environment set
print(os.getenv("JAVA_HOME"))

# set environment
# os.putenv("TEST_HOME", "ABC")

# 获取当前平台使用的行终止符
print(os.linesep)    # don't display in PyCharm
print(os.name)     # Windows - nt, Linux/Unix - posix


#os.rename("testwrite2.txt", "testwrite3.txt")   # rename file

# os.makedirs(r"c:\test1\test2")    # create multi-level dirs

# os.mkdir("test0")   # create a dir

print(os.stat(filename))  # get file attribution  # WindowsError:[Error123]表示:文件名、目录名或卷标语法不正确


