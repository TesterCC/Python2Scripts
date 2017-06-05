#!/usr/bin/python
# coding:utf-8
#cannot run in mac
from ctypes import *
libc=CDLL("libc.so.6")
message_string = "Hello world!\n"
libc.printf("Testing:%s",message_string)