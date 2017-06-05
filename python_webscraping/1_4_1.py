#!/usr/bin/env python
# coding:utf-8

# 用Python写网络爬虫 P10 2.7.x

import urllib2


def download(url, num_retries=2):
    print '[+]Start to download target. Downloading...\n', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Downlaod error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx Http errors
                return download(url, num_retries-1)
    return html


# print download("https://www.gnum.com")
print download("http://httpstat.us/500")
