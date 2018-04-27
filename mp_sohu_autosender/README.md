## 目前单线程执行

运行方式参考main
按分类自动化生成xxx.log,需要手动定期删除，建议1周1删除。
需要安装phantomjs

- self.send_times = 3   设置每个账号的发帖数
- self.interval_time = 10   # 单账户发帖间隔时间，单位秒
- "https://mp.sohu.com/v3/news/publish"   正式发布请用此接口
- "https://mp.sohu.com/v3/news/draft"   默认用draft接口
- 运行参考main