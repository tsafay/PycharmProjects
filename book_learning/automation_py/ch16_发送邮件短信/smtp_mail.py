#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/6 21:04
import smtplib
from email.mime.text import MIMEText
from email.header import Header
qq = smtplib.SMTP('smtp.qq.com',587)
qq.ehlo()
qq.starttls()
qq.login('287672785@qq.com','olyaolmuvloycaig')
text = '但是客户大客户达：' \
          '沙鲁克汗大量客户端加发哈客户烦死了开发哈市' \
          '法力回复拉客户发GV没收到两个环节上单联开关你发发送到看，方面数量将发生实到。大数据发大水' \
          '大领盒饭飞机奥斯卡了；大家啊大酒店咯啊福建省立刻发哈市而今天weIoTUR诶得分。'
# message = MIMEText(text,'plain','utf-8')
# message['Subject'] = Header('打哈萨克','utf-8').encode()
# qq.sendmail('287672785@qq.com','982803587@qq.com',message.as_string())
text1 = 'Subject:Long time no see\n\nDear name,\nWould you rember me after so long time,my sister?\nI\'m tito,are you ok?'
message = """From: From Person 
To: To Person 
Subject: SMTP e-mail test

This is a test e-mail message.
"""
qq.sendmail('287672785@qq.com','982803587@qq.com',text1)

qq.quit()