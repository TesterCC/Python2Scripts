#!/usr/bin/env python
# coding=utf-8

# Python大法之从HELL0 MOMO到编写POC(一)(二)
# https://bbs.ichunqiu.com/thread-26074-1-1.html

# one line version
print('\n'.join([''.join([('TEST'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))


# multi line version

content = []

for y in range(30, -30, -1):

        for x in range(-30, 30):

                subcontent = []

                if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0:

                        subcontent.append('LOVE'[(x-y) % 4])

                else:

                        subcontent.append(' ')

                content.append(''.join(subcontent))

        content.append('\n')

print ''.join(content)