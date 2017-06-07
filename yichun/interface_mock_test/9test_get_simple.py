# coding: utf-8
import json

#序列化 python dict -> json
d={'key':'value'}
j = json.dumps(d)
print type(d)
print type(j)

#反序列化   json -> python 
print json.loads(j)