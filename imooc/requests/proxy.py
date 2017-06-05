# coding:utf-8
# !/usr/bin/env python

# http://www.imooc.com/video/13093

import requests


proxies = {'http': 'socks5://127.0.0.1:1080', 'https': 'socks5://127.0.0.1:1080'}
url = 'https://www.facebook.com'
url2 = 'https://www.baidu.com'

response = requests.get(url, proxies=proxies, timeout=10)   # need use proxies

response2 = requests.get(url2, timeout=10)   # don't use proxies

print response.status_code
print response2.status_code
