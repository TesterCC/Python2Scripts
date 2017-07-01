#!/usr/bin/env python
# coding=utf-8
# 使用fork方式实现多进程 P17

import os


def testfork():
    print "Current Process (%s) start ..." % (os.getpid())
    pid = os.fork()
    if pid < 0:
        print "Error in fork."
    elif pid == 0:
        print 'I am child process (%s) and my parent process is (%s)' % (os.getpid(), os.getppid())
    else:
        print '(%s) created a child process (%s).' % (os.getpid(), pid)

if __name__ == '__main__':
    testfork()