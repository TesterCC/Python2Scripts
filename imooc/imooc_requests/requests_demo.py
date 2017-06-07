# -*- coding: utf-8 -*-

import requests

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'

def use_simple_requests():
    response = requests.get(URL_IP)
    print '>>>>Response Headers:'
    print response.headers
    print '>>>>Response Body:'
    print response.text

def use_params_requests():
    # Build param request
    parsms = {'param1': 'hello', 'param2': 'world'}
    # Send requeset
    response = requests.get(URL_IP, params=parsms)
    # Handle the response
    print '>>>>Response Headers:'
    print response.headers
    print '>>>>Status Code:'
    print response.status_code, response.reason   # 含义OK
    # print response.reason
    print '>>>>Response Body:'
    print response.json()

if __name__ == '__main__':
    print '>>>Use simple requests:'
    use_simple_requests()
    print "======================================="
    print '>>>Use params requests:'
    use_params_requests()