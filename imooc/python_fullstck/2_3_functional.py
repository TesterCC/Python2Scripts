#!/usr/bin/env python
# coding=utf-8

# Python 全栈案例初体验  2-3
# http://www.imooc.com/video/15369

# custom function


def hi(name=''):
    print 'Hello, {}'.format(name)
    return None


if __name__ == '__main__':
    hi()
    hi('everyone')
