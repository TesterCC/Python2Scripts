# coding: utf-8
# !/usr/bin/python
# http://blog.csdn.net/pfm685757/article/details/50162567

from Tkinter import *

root = Tk()
root.title("QA Testing Toolkit")
root.geometry()

def print_item(event):
    print lb.get(lb.curselection)

var = StringVar()

lb = Listbox(root, listvariable = var)
list_item = [1,2,3,4]  # contents of control is 1234
for item in list_item:
    lb.insert(END,item)
lb.delete(2,4)  # now,contents of control is 13

var.set(('a','ab','c','d')) #重新设置了，这时控件的内容就编程var的内容了

print var.get()
lb.bind('<ButtonRelease-1>',print_item)
lb.pack()

root.mainloop()




def print_item(event):
    print lb.get(lb.curselection())