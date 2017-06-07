#!/usr/bin/env python
#coding=utf-8

import jenkins

server = jenkins.Jenkins('http://192.168.2.141:8080/')
print server.jobs_count()