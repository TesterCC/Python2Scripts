#!/usr/bin/python
# coding:utf-8

import traceback
import logging

from imooc.crawler.baike_spider import url_manager,html_downloader,\
    html_parser,html_outputer
from bs4 import BeautifulSoup
import re



class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'Craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 15:
                    break

                count += 1

            except Exception, e:
                print "Craw Failed! Exception Reason:", e
                # print stack info method 1  , need import traceback
                # msg = traceback.format_exc()
                # print msg

                # method 2, import logging
                logging.exception(e)

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.htm"  # success
    # root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

