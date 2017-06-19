#!/usr/bin/env python
# coding=utf-8

'''
Python爬虫开发与项目实战  P11-13
1.3 IO编程
'''

# P12
def simple_io():
    try:
        f = open("/readme.txt", 'r')
        str = f.read()
        print(str)
    except IOError, e:
        print(e.message)
    finally:
        if f:
            f.close()

# P13
def more_simple_io():
    with open(r'/readme.txt', 'r') as fileReader:
        print fileReader.read()


def more_simple_readlines():
    with open(r'/readme.txt', 'r') as fileReader:
        # print(fileReader.readlines())
        for line in fileReader.readlines():
            print(line.strip())


def simple_write():            # attention write path
    try:
        f = open("testwrite2.txt", 'w')
        f.write("test write2")
        f.flush()
    except IOError, e:
        print(e.message)
    finally:
        if f:
            f.close()


def more_simple_write():     # attention write path
    with open(r'testwrite.txt', 'w') as fileWriter:
        fileWriter.write("test simple write1")
        # fileWriter.flush()


if __name__ == '__main__':
    # simple_io()
    # more_simple_io()
    # more_simple_readlines()
    simple_write()
    more_simple_write()




