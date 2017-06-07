#!/usr/bin/env python
# coding: utf-8

import web
import MySQLdb
import MySQLdb.cursors


render = web.template.render('templates')

urls = (  # 匹配顺序从上到下，建议匹配范围小的在上，匹配范围大的在下
    '/article', 'article',
    '/index', 'index',    # 精确匹配
    '/blog/\d+', 'blog',  # 模糊匹配  不带组
    '/(.*)', 'hello',     # regexp, method name  ,  匹配范围大的放后面
)
app = web.application(urls, globals())


class index:
    def GET(self):
        query = web.input()     # 请求参数获取
        # return query
        # return web.seeother('/article')   # jump to /article
        return web.seeother('https://www.baidu.com')    # jump to baidu

class blog:
    def POST(self):
        data = web.input()
        return data

    def GET(self):
        return web.ctx.env    # 请求头获取


class hello:
    def GET(self, name):
        return render.hello2(name)    # /templates/hello2.html   模版文件读取


class article:
    def GET(self):
        conn = MySQLdb.connect(host='localhost', user='root', passwd='yanxi76543210', db='test', port=3306, cursorclass=MySQLdb.cursors.DictCursor)  #  Notice: port 3306 don't user "'"
        cur = conn.cursor()
        cur.execute('select * from msg')
        r = cur.fetchall()
        cur.close()
        conn.close()
        print r
        return render.article(r)

if __name__ == "__main__":
    app.run()