# coding: utf-8

from model import *

db.connect()

#查询一条数据
post = Post.get(Post.id == 1)
print post.id
print post.title
print post.content

print "========================================="

#查询多条数据
posts = Post.select()
for post in posts:
    print post.id
    print post.title
    print post.content
