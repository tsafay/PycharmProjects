# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/22 10:04
message = 'It was a bright cold day in April,and the' + \
          'clocks were striking thirteen.'
count = {}
for char in message:
    # 如果char值在字典中不存在就在字典中创建；如果存在，则返回键的值
    count.setdefault(char,0)
    #count[char] = count[char] + 1
    count[char] += 1
print(message)
for k,v in count.items():
    print(k,v)
