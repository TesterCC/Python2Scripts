# coding: utf-8

from peewee import *

db = SqliteDatabase('posts.db')

class Post(Model):
    title = CharField(unique=True)  #char类型字段
    content = TextField()

    class Meta:
        database = db