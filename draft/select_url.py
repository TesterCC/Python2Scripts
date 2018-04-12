#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/11 14:55'


"""
for test select url
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# event_id = "220265179"
# event_id = "131007944"
event_id = "131007943"


with open('publish.log', 'r') as rlog:
    check_list = rlog.readlines()    # need filter \n
    check_list = ["".join(line.strip()) for line in check_list]
    # print(check_list)
    rlog.close()

if event_id in check_list:
    print("event-{0}.html had published".format(event_id))
else:
    print('Publishing succeed, write into log.')
    with open('publish.log', 'at') as log:
        log.write('{}'.format(event_id) + '\n')
    log.close()

