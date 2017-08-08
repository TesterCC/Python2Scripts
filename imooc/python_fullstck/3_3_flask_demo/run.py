#!/usr/bin/env python
# coding=utf-8

# Python 全栈案例初体验  3-3
# http://www.imooc.com/video/15375


from views import app


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999, debug=True)