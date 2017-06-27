#!/usr/bin/env python
# coding=utf-8


def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1

if __name__ == '__main__':
    f = fab(5)
    print(f.next())
    print(f.next())
    print(f.next())
    print(f.next())
    print(f.next())
    # print(f.next())