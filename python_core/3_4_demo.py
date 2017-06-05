# /usr/bin/env python

"this is a test module"

import sys
import os

debug = True

class FooClass (object):
    "Foo class"
    pass

def test():
    "test function"
    foo = FooClass()

    if debug:
        print 'ran test()'

if __name__ == '__main__':
    test()