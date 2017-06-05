# coding:utf-8
# !/usr/bin/env python


import requests


def download_image():
    """
    demo: download image *.jpg
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    url = "http://image.lxway.com/upload/0/b2/0b2b7eb5ce674e66c6a728e85afae0f3_thumb.jpg"
    response = requests.get(url, headers=headers, stream=True)
    # print response.status_code, response.reason
    # print response.headers
    # print response.content
    with open('demo.jpg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)

# download_image()

def download_image_improved():
    """
    demo: download image improved
    """
    # fake headers infomation
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    # set url
    url = "http://image.lxway.com/upload/0/b2/0b2b7eb5ce674e66c6a728e85afae0f3_thumb.jpg"
    response = requests.get(url, headers=headers, stream=True)

    from contextlib import closing
    with closing(requests.get(url, headers=headers, stream=True)) as response:
        # open file
        with open('demo1.jpg', 'wb') as fd:
            # 128/write
            for chunk in response.iter_content(128):
                fd.write(chunk)


download_image_improved()