#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/5 14:47
'项目：文本文件到电子表格'
'''

'''
import openpyxl,os
wb = openpyxl.Workbook()
sheet = wb.active

for txt in os.listdir('story'):
    f = open('story\\'+txt,encoding='gbk')
    text = f.readlines()
    for j in range(os.listdir('story').index(txt)+1, len(os.listdir('story'))+1):
        for i in range(1,len(text)+1):
            sheet.cell(row=i,column=j).value = text[i-1]
wb.save('storytxt.xlsx')