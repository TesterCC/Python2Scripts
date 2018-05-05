#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/5 16:21'

with open('p2.txt') as f:
    urls = f.readlines()
    urls = [_url.strip() for _url in urls]  # strip \n

print(urls)
print("*" * 50)


def go_insert_img():
    for u in urls:
        if len(u.split("---------->")) == 2:   # 容错处理
            url, page = u.split("---------->")
            page = int(page)
            if page > 0:
                for i in range(page):
                    dmg_url = url.replace('.pdf', '-{}.png'.format(str(i)))
                    print(dmg_url)
                    dmg_page = i + 1
                    # dmg_page.save()   # django中要放在里面，写入一张存一次，以防写入中程序down掉
                print(dmg_page)


if __name__ == '__main__':
    go_insert_img()
