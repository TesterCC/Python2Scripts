# !/usr/bin/env python
# coding:utf-8

import requests

def send_http_request_through_exec(url, method):
    if method not in ["get","post","put","delete","head","optinos"]:
        raise StandardError("Cant not support this method : %s" % method)

    _response = None
    _request_api_string = "_response = requests.%s('%s')" % (method, url)
    exec _request_api_string

    return _response


if __name__ == '__main__':
    url = "http://ip.taobao.com/service/getIpInfo.php?ip=183.250.26.144"

    _response = send_http_request_through_exec(url,'get')
    print _response.status_code