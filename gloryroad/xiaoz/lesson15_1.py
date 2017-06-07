#coding:utf-8

'''
Created on 2016年3月16日

@author: PavilionLYX
'''

import urllib

url='https://www.gnum.com/'

fp = urllib.urlopen(url)
# print fp.read() #返回全部
print fp.readline() #返回一行
print "=================================="
print fp.readlines() #返回全部到一行
print "=================================="
print fp.info() #返回一个httplib.HTTPMessage对象，表示远程服务器返回的头信息
print "=================================="
print fp.getcode()  #返回Http状态码
print "=================================="
print fp.geturl() #返回请求的url

print "=================================="
filename = urllib.urlretrieve(url)
print type(filename)
print filename  #临时存放

print "=================================="
filename2 = urllib.urlretrieve(url,r'E:\workspace\PythonDemo\gloryroadpythondemo\gnumhomepage.html')
filename3 = urllib.urlretrieve(url,'E:\workspace\PythonDemo\gloryroadpythondemo\gnumhomepage2.html')

urllib.urlcleanup()
print "===finish clear==="

url2=r'http://www.baidu.com/!@#/'
print urllib.quote(url2)
print urllib.quote_plus(url2) #这个连/符号也会解码

#encode
"===encode==="
print urllib.unquote(urllib.quote(url2))
print urllib.unquote_plus(urllib.quote_plus(url2))

