# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/23 16:25
'strip()的正则表达式'
'''
写一个函数，它接受一个字符串，做的事情与strip()字符串方法一样；
如果只传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符；
否则，函数的第二个参数指定的字符从该字符串中去除；
'''

import re
def stripFun(text,strs=''):
    if len(strs) == 0:
        regex = re.compile(r'\s*(.*)\s*')
        return regex.sub(r'\1',text)
    else:
        regex = re.compile(r''+strs+'*')
        return regex.sub('',text)

s = '  adadad  adada       '
print(s)
p = stripFun(s)
print(p)

ss = 'asdasdafsdagdafgdafgdagd'
print('\n' + ss)
pp = stripFun(ss,'da')
print(pp)
