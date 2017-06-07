# coding: utf-8

# day5
# 代码还可以优化重构，比如查询地址可以直接读取

# http://ip.taobao.com/instructions.php
# http://ip.taobao.com/service/getIpInfo.php?ip=119.28.48.227
# 1. 请求接口（GET）：
# /service/getIpInfo.php?ip=[ip地址字串]
# 2. 响应信息：
# （json格式的）国家 、省（自治区或直辖市）、市（县）、运营商
# 3. 返回数据格式：
# {"code":0,"data":{"ip":"210.75.225.254","country":"\u4e2d\u56fd","area":"\u534e\u5317",
# "region":"\u5317\u4eac\u5e02","city":"\u5317\u4eac\u5e02","county":"","isp":"\u7535\u4fe1",
# "country_id":"86","area_id":"100000","region_id":"110000","city_id":"110000",
# "county_id":"-1","isp_id":"100017"}}
# 其中code的值的含义为，0：成功，1：失败。

# testerhome -- 119.28.48.227
# local company -- 125.71.88.239
# proxy -- 119.9.108.181

import json
import requests


# http://cn.python-requests.org/zh_CN/latest/user/quickstart.html#id3
url = 'http://ip.taobao.com/service/getIpInfo.php'
target_ip = '125.71.88.239'
payload = {'ip': target_ip}
r = requests.get(url, params=payload)

flag_code = r.json()['code']  # 0 is valid, 1 is in valid.

print r.url
print "Content Type: %s" % r.headers['content-type']
print "Status Code: %s " % r.status_code
print "Encoding: %s" % r.encoding

# print r.text
print r.content  # string

dict_response = json.loads(r.content)  # str r.content to dict
print "Response Type: %s" % type(dict_response)

print "==================================================================="

# custom exception 自定义异常
class InvalidIPException(Exception):
    def __init__(self, flag_code, code):
        Exception.__init__(self)
        self.flag_code = flag_code
        self.code = code


try:
    if flag_code == 1:
        raise InvalidIPException(flag_code, 1)
except InvalidIPException, e:
    print "Invalid IP Error!"
finally:
    print "End of try-catch-finally."





# if r.status_code == 200:
#     print "Request Success. -- 请求成功"
#     if flag_code == 0:
#             print "IP is valid."
#             # print "return code: %s" % dict_response['code']
#             print dict_response['data']['ip']   # 数字和英文其实可以不用转码
#             print dict_response['data']['isp'].encode("utf-8")
#             print dict_response['data']['country_id'].encode("utf-8")  # CN
#             print dict_response['data']['area'].encode("utf-8")  # ASCII可以转成正常中文显示
#             print dict_response['data']['region'].encode("utf-8")
#             print dict_response['data']['city'].encode("utf-8")
#     else:
#         print "IP is invalid , please check your input IP."
# else:
#     print "Request Failed. -- 请求失败"










