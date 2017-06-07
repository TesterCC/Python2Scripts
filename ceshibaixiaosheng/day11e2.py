#!/usr/bin/env python
# coding: utf-8

# 错误

import re


json_src_line = 'io=8192.0MB, bw=24407KB/s, iops=6101 , runt=343698msec'

pattern = re.compile("iops=(\d+)")
print pattern.match(json_src_line)
