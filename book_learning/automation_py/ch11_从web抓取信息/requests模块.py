#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/27 9:50
import requests
# requests.get()函数接受一个URL字符串下载一个网页，返回一个Response对象
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# 通过检查Response对象的status_code属性，了解网页是否请求成功，状态码为200是请求成，404失败；
print(res.status_code)
# 如果请求成功，下载的页面作为一个字符串，保存在Response对象的text属性中
s = res.text
print(len(s))
print(s[:1000])
# raise_for_status()方法如果下载成功，就什么也不做，如果失败则抛出异常；
# 一般总是在调用requests.get()之后在调用raise_for_status().确保下载成功，然后让程序继续。
res.raise_for_status()
playFile = open('requests_下载.txt','wb')  # 用‘wb’调用open()函数，以写入二进制方式打开文件
# Response对象的iter_content()方法在循环的每次迭代中，返回一段内容。
# 每段都是bytes数据类型，不过你需要指定这一段包含多少字节，作为参数传入iter_content()
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()