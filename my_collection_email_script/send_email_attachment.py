#! /usr/bin/python
# -*- coding:utf8 -*-
# cannot use in China

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

#variable
sender_smtpserver = 'smtp.xxx.com'   # email smtp
sender_username = 'testercc@xxx.com'  # e-mail address
sender_password = '*****'      # password

#创建一个带附件的实例
msg = MIMEMultipart()

txt = MIMEText("这是中文的邮件内容哦",'plain','utf8')
msg.attach(txt)

# 附件构造可封装在一个method里
#构造附件1
att1 = MIMEText(open('D:\\emailtest\\emailtest.rar', 'rb').read(), 'base64', 'utf8')  # Here is attachment path
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="emailtest.rar"'# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
msg.attach(att1)

#构造附件2
att2 = MIMEText(open('D:\\emailtest\\UAT_Phase2_issue.txt', 'rb').read(), 'base64', 'utf8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="UAT_Phase2_issue.txt"'
msg.attach(att2)

#构造附件3
att3 = MIMEText(open('D:\\emailtest\\companyIP.png', 'rb').read(), 'base64', 'utf8')
att3["Content-Type"] = 'application/octet-stream'
att3["Content-Disposition"] = 'attachment; filename="companyIP.png"'
msg.attach(att3)

#加邮件头
msg['to'] = 'testerlyx@foxmail.com'
msg['from'] = 'testerlyx@foxmail.com'
msg['subject'] = 'Testing - python e-mail send attachment'
 
#发送邮件
try:
    server = smtplib.SMTP()
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    server.connect(sender_smtpserver)
    server.starttls()
    server.login(sender_username, sender_password) #username为sender e-mail，password为sender pwd
    server.sendmail(msg['from'], msg['to'], msg.as_string())
    server.quit()
    print 'Send E-mail successfully.'
except Exception, e:
    print str(e)
    print 'Send E-mail failed.'
