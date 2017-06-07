# coding:utf-8
"""
demo1 -- use httplib
"""
import httplib

http_client = None

http_client = httplib.HTTPConnection('192.168.2.141',8080,timeout=30)
http_client.request('GET','/api/json?pretty=true')

response = http_client.getresponse()
print response.status
print response.read()