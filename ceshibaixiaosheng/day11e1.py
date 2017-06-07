# coding: utf-8

import re

if __name__ == '__main__':
    json_src_line = '{"code":0,"data":{"country":"中国"}}'

    pattern = re.compile(r'\D+\w\D:\d')
    match = pattern.match(json_src_line)

    if match:
        print match.group()