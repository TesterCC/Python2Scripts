# coding: utf-8
# !/usr/bin/python
# http://blog.csdn.net/pfm685757/article/details/50162567

from Tkinter import *
root = Tk()
root.title("hello world")
root.geometry('200x100')                 #是x 不是*
root.resizable(width=False, height=True) #宽不可变, 高可变,默认为True, windows下有效，mac下无效
root.mainloop()