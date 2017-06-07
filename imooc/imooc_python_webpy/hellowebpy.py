#!/usr/bin/env python
# coding: utf-8

import web
        
urls = (  # 匹配顺序从上到下，建议匹配范围小的在上，匹配范围大的在下
    '/index', 'index',    # 精确匹配
    '/blog/\d+', 'blog',  # 模糊匹配  不带组
    '/(.*)', 'hello',     # regexp, method name  ,  匹配范围大的放后面
)
app = web.application(urls, globals())


class index:

    def GET(self):
        return 'index  mothed'


class blog:

    def GET(self):
        return 'blog get method'

    def POST(self):
        return 'blog post method'


class hello:

    def GET(self, name):
        if not name: 
            name = 'World'
        # return 'Hello, ' + name + '! -lyx'
        # return '<html>hello</html>'
        return open(r'1.html', 'r').read()

if __name__ == "__main__":
    app.run()