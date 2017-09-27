#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/26 23:57'

'''
Python爬虫开发与项目实战
1.4.3 协程
2 当拥有动态数量的greenlet需要进行并发管理（限制并发数时，可使用池）  
使用gevent中的pool对象  P27
'''

from gevent import monkey
monkey.patch_all()

from gevent.pool import Pool

import urllib2


def run_task(url):
    print('Visit --> %s' % url)
    try:
        response = urllib2.urlopen(url)
        data = response.read()
        print('%d bytes received from %s.' % (len(data), url))
    except Exception, e:
        print(e)

    return 'url:%s ---> finish' % url


if __name__ == '__main__':
    pool = Pool(3)      # 先访问前3个
    urls = ['https://www.baidu.com/',
            'https://www.yahoo.com/',
            'https://github.com/',
            'http://dict.youdao.com/',
            'http://www.imooc.com/']
    results = pool.map(run_task, urls)
    print(results)





