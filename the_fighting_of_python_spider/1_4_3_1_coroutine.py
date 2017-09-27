#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/26 23:57'

'''
Python爬虫开发与项目实战
1.4.3 协程
1 gevent的使用流程  P26
'''

from gevent import monkey; monkey.patch_all()
import gevent
import urllib2


def run_task(url):
    print('Visit --> %s' % url)
    try:
        response = urllib2.urlopen(url)
        data = response.read()
        print('%d bytes received from %s.' % (len(data), url))
    except Exception, e:
        print(e)

if __name__ == '__main__':
    urls = ['https://www.python.org/',
            'https://www.yahoo.com/',
            'https://github.com/']
    greenlets = [gevent.spawn(run_task, url) for url in urls]
    gevent.joinall(greenlets)      # Wait for the `greenlets` to finish.
