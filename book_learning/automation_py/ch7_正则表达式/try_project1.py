# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/23 11:11
'强口令检测'
'''
使用正则表达式写一个函数，确保传入的口令是强口令；
长度不低于8个字符，同时包含大小写字符以及最少一个数字；
'''
import re
def strongPassword(word):
    regex1 = re.compile(r'[a-z]+')
    regex2 = re.compile(r'[A-Z]+')
    regex3 = re.compile(r'\d+')
    if regex1.search(word) is None:
        print('请最少输入一个小写字母。',word)
        return False
    if regex2.search(word) is None:
        print('请最少输入一个大写字母。',word)
        return False
    if regex3.search(word) is None:
        print('请最少输入一个数字。',word)
        return False
    if len(word) < 8:
        print('请输入最少8个字符。',word)
        return False
    return True

while True:
    text = input('Enter your password:')
    password = strongPassword(text)
    if password:
        print('密码符合要求，',text)
        break
    else:
        continue




