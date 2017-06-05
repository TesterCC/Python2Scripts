#! /usr/bin/env python
# -*- coding: utf-8 -*-


def bubble_sort(l):
    length = len(l)
    for i in xrange(length-1, 0, -1):
        for j in xrange(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]


if __name__ == "__main__":
    l1 = [3, 1, 2, 4, 9, 8, 6, 7, 5]
    print l1
    bubble_sort(l1)
    print l1