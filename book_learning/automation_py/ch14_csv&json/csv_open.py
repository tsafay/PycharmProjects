#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/5 15:35
import csv
file = open('ex.csv')
fileread = csv.reader(file)
# filelist = list(fileread)
# print(filelist)
for row in fileread:
    print('Row ' + str(fileread.line_num) + ': ' + str(row))

