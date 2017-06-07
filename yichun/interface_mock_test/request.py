# coding:utf-8
# http://192.168.2.141:8080/api/json?pretty=true
import requests

#Get

print requests.get('http://192.168.2.141:8080/api/json?pretty=true').text

#POST with Basic Authentication
url = 'http://192.168.2.141:8080/job/CheckPythonVersion/disable'
r = requests.post(url,data={},auth=('admin','globalroam123456'))
print r.status_code
print r.headers
print r.reason