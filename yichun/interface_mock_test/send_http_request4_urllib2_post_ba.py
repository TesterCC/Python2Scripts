# coding:utf-8
"""
demo4 -- use urllib2 post

urllib2标准解决方案--Basic Authentication

"""
import urllib2
# Create an OpenerDirector with support for Basic HTTP Authentication...
auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='Test',
                          uri='http://localhost/testlink/',
                          user='admin',
                          passwd='admin')
opener = urllib2.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
urllib2.install_opener(opener)
urllib2.urlopen('http://localhost/testlink/index.php?caller=login')