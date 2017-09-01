#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/9/1 14:19'

# http://www.jianshu.com/p/15eb2a39ffe0
# python爬虫的最佳实践(三)--真实的网络解析demo


from bs4 import BeautifulSoup
import requests


def detailOper(url):
   web_data = requests.get(url)
   soup = BeautifulSoup(web_data.text, 'lxml')
   # titles1 = soup.select('div.list > ul > li > div > p.infoBox > a')
   titles = soup.select('div.list-wrap js-post > ul > li > a > div.t')

   # prices1 = soup.select('div.list > ul > li > div > p.priType-s > span > i')
   prices = soup.select('div.list-wrap js-post > ul > li > a > div.t-price > p')
   # 定位有问题，没住区到数据
   for title, price in zip(titles, prices):
       data = {
           'title': title.get_text(),
           'detailHerf': title.get('href'),
           'price': price.get_text().replace(u"万", '').replace(' ', '')
       }
       print(data)


def start():
    urls = ['http://www.guazi.com/tj/buy/o{}/'.format(str(i)) for i in range(1, 30, 1)]
    for url in urls:
        print(url)
        detailOper(url)


if __name__ == '__main__':
    start()
