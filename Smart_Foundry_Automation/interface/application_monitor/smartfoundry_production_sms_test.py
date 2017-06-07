# coding:utf-8
# www.smartfoundry.io   yanxipostpaid   6582409001  to callee 8613551856640
import requests

try:
    r = requests.get('https://api.smartfoundry.io:8443/tropo/sessions?action=create&token=547a525379696a486a64456f62774d597566474371757655676b7651636258486a516d71686a73724d625477')
    print "SmartFoundry Production return status code : %s " % r.status_code
except Exception,e:
    print "SmartFoundry Production return status code : %s " % r.status_code
    print Exception, ":", e
