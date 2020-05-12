# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/23 9:34
'项目：电话号码及email地址提取'
'''
程序任务：
1、从剪贴板粘贴文本
2、找出文本中的所有电话号码及email地址
3、将他们粘贴到剪切板；
代码实现：
1、使用pyperclib模块复制和粘贴字符串
2、创建两个正则表达式：匹配电话号码及email地址；
3、将匹配的字符串整理格式，放在一个字符串中，用于粘贴
4、如果没有找到匹配，显示消息；

类似程序：识别文本的模式（并且可能用 sub()方法替换它们）有许多不同潜在的应用。
 寻找网站的 URL，它们以 http://或 https://开始。
 整理不同日期格式的日期（诸如 3/14/2015、03-14-2015 和 2015/3/14），用唯一
的标准格式替代。
 删除敏感的信息，诸如社会保险号或信用卡号。
 寻找常见打字错误，诸如单词间的多个空格、不小心重复的单词，或者句子末尾处多个感叹号。它们很烦人！！
'''
import pyperclip,re

# 电话号码的正则表达式
phoneRegex = re.compile(r'''(
            (\d{3}|\(\d{3}\))? # area code
            (\s|-|\.)?         # separator
            (\d{3})            # first 3 number
            (\s|-|\.)?         # separator
            (\d{4})            # last 4 number
            (\s*(ext|x|ext.)?\s*(\d{2,5}))?  # extension
)''',re.VERBOSE)

# email正则表达
emailRegex = re.compile(r'''(
             [a-zA-Z0-9._%+-]+    # username
             @
             [a-zA-Z0-9.-]+       # domain name
             (\.[a-zA-Z]{2,4})    # dot-something
)''',re.VERBOSE)

# 在剪切板中的字符串匹配号码及email
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phone_num = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)

for groups in emailRegex.findall((text)):
    matches.append(groups[0])

# 复制结果在剪切板
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email addresses found.')