# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/22 21:03
'不用正则表达式查找文本'
''' 000-000-0000 '''
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 123-456-1122 tomorrow,' + \
          '666-345-5678 is my office.' + \
          'Then,if all not called,you can use 000-222-4574.'
for i in range(len(message)):
    if isPhoneNumber(message[i:i+12]):
        print('Phone number:',message[i:i+12])
print('Done')
