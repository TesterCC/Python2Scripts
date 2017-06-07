#-*- coding:utf-8 -*-#
'''
Created on 2015年11月10日

@author: PavilionLYX
'''
def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')  #prefix--DEBUG    f.__name__ -- test()
def test():
    pass
print test()