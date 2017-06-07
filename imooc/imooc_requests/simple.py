# !/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.imooc.com/video/13089

import requests
import json


response = requests.get('http://api.github.com')


# def better_print(json_str):
#     return json.dumps(json.loads(json_str), indent=4)

print response.status_code
print response.reason
print response.headers
print response.url
print response.history
print response.cookies
print response.elapsed
print response.request
print response.request.headers
print response
print response.encoding
print response.raw.read(10)
print response.content
print response.text
print response.json()['team_url']
