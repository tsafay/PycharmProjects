#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/24 18:09
'''
send2trash模块：安全删除文件，将文件或文件夹发送到回收站，而不是永久删除
'''
import send2trash
baconFile = open('text1.txt','a')
baconFile.write('aaaaaaaaaaaaa')
baconFile.close()
send2trash.send2trash('text1.txt')

