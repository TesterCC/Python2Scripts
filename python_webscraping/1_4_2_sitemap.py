#!/usr/bin/env python
# coding:utf-8
# 用Python写网络爬虫 P12
# http://example.webscraping.com/sitemap.xml
import re
import urllib2


def download(url, user_agent='wswp', num_retries=2):
    print 'Downloading: ', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Downloading error: ', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                return download(url, user_agent, num_retries-1)
    return html


def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)
        # scrape html here
        # ...

if __name__ == '__main__':
    # TARGET_URL = "http://example.webscraping.com/sitemap.xml"   # 官方地址已无相关文件
    TARGET_URL = "http://www.cnfol.com/Sitemap/sitemap.xml"  # can use
    crawl_sitemap(TARGET_URL)