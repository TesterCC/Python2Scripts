#!/usr/bin/env python
#coding=utf-8
'''
http://python-jenkins.readthedocs.io/en/latest/examples.html
http://python-jenkins.readthedocs.io/en/latest/api.html
'''

import jenkins

server = jenkins.Jenkins('http://192.168.2.141:8080/', username='admin', password='globalroam123456')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))




