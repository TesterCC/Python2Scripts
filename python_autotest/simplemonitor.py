#!/usr/bin/env python
# coding=utf-8

# http://blog.csdn.net/powerccna/article/details/8298352

import time
import telnetoperate


remote_server = telnetoperate.TelnetAction("192.168.23.235", "#", "user", "passwd123")
#get cpu information
cpu = remote_server.get_output("sar 1 1 |tail -1")
memory = remote_server.get_output("top | head -5 |grep -i memory")
io = remote_server.get_output("iostat -x 1 2|grep -v '^$' |grep -vi 'dev'")