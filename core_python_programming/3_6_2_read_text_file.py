# coding: utf-8
# !/usr/bin/env python

'makeTextFile.py -- create text file -- P53-54'

# get filename
fname = raw_input('Enter filename: ')
print "Try to find file, please wait..."

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError, e:
    print "The file open error: ", e
else:
    print "Find file, output ..."
    print
    # display contents to the screen
    for eachLine in fobj:
        print eachLine
    fobj.close()
