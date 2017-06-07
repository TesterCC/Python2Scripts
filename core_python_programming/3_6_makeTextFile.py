# coding: utf-8
# !/usr/bin/env python

'makeTextFile.py -- create text file --P52 原版有错误'
''

import os
ls = os.linesep  # 给os.linesep属性

# get filename -- not in book
fname = raw_input("Enter filename:")

while True:
    if os.path.exists(fname):
        print "ERROR: '%s' already exists" % fname
    else:
        break

# get file content(text) lines
all = []
print "\nEnter lines ('.' by itself to quit).\n"

#loop until user terminates input
while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

#write lines to file with proper line-ending
fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print 'DONE!'