# coding: utf-8

import requests

class CaseFailureException(Exception):
    pass

class CaseErrorException(Exception):
    pass

class ConnectionError(Exception):
    pass

class ConnectTimeout(Exception):
    pass


def send_request(request_url):
    try:
        resp = requests.get(request_url)

        resp_json = resp.json()

        if resp_json['code'] != 0:
            raise CaseFailureException("Case failure!")
    except ConnectionError:
        raise CaseErrorException("Connect timeout: connect to server time!")
    except ConnectTimeout:
        raise CaseErrorException("Connect error: cann not connect to server!")


if __name__ == '__main__':
    # 183.250.26.144
    try:
        for i in range(0,20):
            last_ip_value = 134 + i
            url = "http://ip.taobao.com/service/getIpInfo.php?ip=183.250.26.%s" % str(last_ip_value)
            send_request(url)

        print "Case pass"
    except CaseFailureException:
        print "Case failure"
    except CaseErrorException:
        print "Case error"
    except ConnectionError:
        print "Connect error"
    except ConnectTimeout:
        print "Conncet timeout"