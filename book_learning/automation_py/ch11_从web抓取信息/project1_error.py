#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/28 20:30
'项目：命令行邮件程序'
'''
编写一个程序，通过命令行接受电子邮件地址和文本字符串。然后利用 selenium登录到你的邮件账号，
将该字符串作为邮件，发送到提供的地址（你也许希望为这个程序建立一个独立的邮件账号）。
这是为程序添加通知功能的一种好方法。你也可以编写类似的程序，从Facebook 或 Twitter 账号发送消息。
失败！！！！！！！！！
'''
from selenium import webdriver
import time,sys
driver = webdriver.Chrome()
driver.get('https://mail.126.com/')
time.sleep(2)

# 选择用户名登录密码登录方式
driver.find_element_by_id('lbNormal').click()
time.sleep(2)

# 跳转到iframe
iframe = driver.find_elements_by_tag_name('iframe')[0]
driver.switch_to.frame(iframe)

# 输入用户名及密码
username = driver.find_element_by_name('emile')
password = driver.find_element_by_name('password')
username.send_keys('******')
password.send_keys('*********')

# 点击登录
driver.find_element_by_id('dologgin').click()
time.sleep(2)
#勾选“是我在使用，不再提示”
#driver.find_element_by_id("ismyphonebox").click()
#点击登陆
#driver.find_element_by_xpath("//*[@class='u-btn u-btn-middle3 f-ib bgcolor f-fl']").click()
#从frame中切回主文档
driver.switch_to.default_content()

time.sleep(2)
#点击“写信”
driver.find_element_by_id("_mail_component_24_24").click()
time.sleep(2)
#填写收件人
receiver=driver.find_element_by_xpath("//div[contains(@id,'_mail_emailinput')]/input")
receiver.send_keys("*******@163.com")
time.sleep(2)
#填写主题
title=driver.find_element_by_xpath("//input[contains(@id,'_subjectInput')]")
title.send_keys("命令行邮件程序")

#跳转到iframe
#iframe = driver.find_elements_by_tag_name("iframe")[2]
iframe=driver.find_element_by_xpath("//iframe[@class='APP-editor-iframe']")
driver.switch_to.frame(iframe)
#开始编写邮件内容
write_body=driver.find_element_by_xpath("/html/body")
write_body.send_keys("天空飘来五个字，那都不是事儿")
#跳出frame
driver.switch_to.default_content()
time.sleep(2)
#点击发送按钮
driver.find_element_by_xpath("//*[@class='jp0']/div/span[@class='nui-btn-text']").click()
time.sleep(2)
driver.close()
