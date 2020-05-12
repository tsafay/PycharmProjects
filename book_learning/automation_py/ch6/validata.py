# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/22 16:12
while True:
    age = input('Enter your age:')
    if age.isdecimal():  # isX字符串：如果字符串只包含数字且非空，返回True；
        break
    print('Please enter a number for your age.')

while True:
    password = input('Select a new password(letters and number only):')
    if password.isalnum(): # 字符串如只包含数字和字母，且非空，则返回True
        break
    print('Password can only have letters and numbers.')
