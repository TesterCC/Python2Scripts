#!/usr/bin/env python
# coding=utf-8

# Python 全栈案例初体验  2-4
# http://www.imooc.com/video/15370


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(port=9999)