#! /usr/bin/python
# -*- coding: utf-8 -*- 
import smtplib
import time
from email.message import Message
from time import sleep
import email.utils
import base64

smtpserver = 'smtp.xxx.com'   # email smtp
username = 'testercc@xxx.com'  # e-mail address
password = '*****'      # password

from_addr = 'sender@xxx.com'
to_addr = 'receiver1@xxx.com'
cc_addr = 'receiver2@xxx.com'

time = email.utils.formatdate(time.time(),True) #打印时间
mail_content = 'Already report error will run the code.'

message = Message()
message['Subject'] = 'GNum web error testing '+time
message['From'] = from_addr
message['To'] = to_addr
message['Cc'] = cc_addr
message.set_payload('This is mail content '+time+". "+mail_content)
msg = message.as_string()

sm = smtplib.SMTP(smtpserver,port=587,timeout=20)
sm.set_debuglevel(1)
sm.ehlo()
sm.starttls()
sm.ehlo()
sm.login(username, password)

try:
	sm.sendmail(from_addr, to_addr, msg)
	sleep(5)
	sm.quit()
	print 'Send E-mail successfully.'
except Exception, e:
	print str(e)
	print 'Send E-mail failed.'