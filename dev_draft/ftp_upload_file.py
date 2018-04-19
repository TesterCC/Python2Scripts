#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/19 22:28'

import os
from ftplib import FTP

"""
Connect to Ubuntu in Terminal: 
ftp -P 2121 172.16.150.160
"""


def ftpconnect():

    ftp_server = '172.16.150.160'

    ftp = FTP()
    ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
    ftp.connect(ftp_server, 2121)
    ftp.login('testftp', 'testftp123')    # 登录，如果匿名登录则用空串代替即可

    return ftp


def uploadfile(ftp, localpath, remotedir="/home/testftp"):
    filename = os.path.basename(localpath)
    print(filename)
    remotepath = os.path.join(remotedir, filename)
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR' + remotepath, fp)  # upload file
    ftp.set_debuglevel(0)    # 0: no debugging output (default)
    fp.close()     # close file



ftp = ftpconnect()
fp = os.popen("ls *.jpg")
lines = fp.readlines()
for line in lines:
    print(line.strip())
    uploadfile(ftp, line.strip())
fp.close()



