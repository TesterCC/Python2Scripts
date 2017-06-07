# coding=utf-8
import re
from robobrowser import RoboBrowser

"""
https://testerhome.com/topics/1801
pip install robobrowser
"""
# 访问python selenium自动化测试班的页面

url = 'http://itest.info/courses/2'
b = RoboBrowser(history=True)
b.open(url)

# 获取这个班的名称--python selenium自动化测试班
class_name = b.select('.headline h2')
print class_name[0].text

# 获取这个班的描述--独一无二的超低价培训-口碑之选
class_desc = b.select('.tag-box')
print class_desc[0].text

# 获取开班的时间--**第五期报名截止2015年1月17日，开课时间1月17日
class_time = b.select('h4')
print class_time[0].text

# 获取授课老师信息--虫师
teacher = b.select('.thumbnail-style h3')
print teacher[0].text

# 获取报名方式--**课程咨询请联系QQ：12079456
qq = b.find(text=re.compile('QQ'))
print qq

# 获取selenium进阶群的群号--**技术交流+selenium 进阶群：189116036
qq_group = b.find(text=re.compile('\+selenium'))
print qq_group