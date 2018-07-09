#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/7/9 14:57'

"""
for backup project website critical logs

key words: sponsor post data
/data/web/xxxx/website/log
.tar.gz save more space than .zip
"""

import os
import time


def backup_logs(source, target_dir):
    print(">>>Daily website debug.log backup start...")

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    os.system("cd {}".format(source[0]))

    target_dir = target_dir + os.sep

    now_time = time.strftime("%Y%m%d_%H%M%S")

    target = target_dir + now_time + '.tar.gz'
    print("target: {}".format(target))

    command = 'tar zcPf {0} debug.*'.format(target, ''.join(source))   # 要先切换到source目录，否则会报错
    print("Run command: \n{}".format(command))

    # 运行备份
    print("Running result:")
    if os.system(command) == 0:
        print('Successful backup to', target)
    else:
        print('Backup FAILED, please confirm it.')

    print(">>>Daily website debug.log backup end...")


def main():
    # 要备份的文件所在的目录
    source = ['/Users/TesterCC/Development/python_workspace/Python_Network/dev_draft/backup_log/log']

    # 备份文件必须存储在一个主备份目录中
    target_dir = '/Users/TesterCC/Development/python_workspace/Python_Network/dev_draft/backup_log/backup_logs'

    backup_logs(source, target_dir)


if __name__ == '__main__':
    main()
