#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/4 20:29
'项目：从电子表格中读取数据'
'''
2010年美国人口普查，计算人口总数，及每个县的普查区数量。
程序任务：
• 从 Excel 电子表格中读取数据。
• 计算每个县中普查区的数目。
• 计算每个县的总人口。
• 打印结果。
程序实现：
• 用 openpyxl 模块打开 Excel 文档并读取单元格。
• 计算所有普查区和人口数据，将它保存到一个数据结构中。
• 利用 pprint 模块，将该数据结构写入一个扩展名为.py 的文本文件。
'''

import openpyxl,pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('popudata.xlsx')
sheet = wb['Population']
countydata = {}
row_num = sheet.max_row

# TODO: 填写每个县的人口和地区countydata
print('Reading rows...')
for row in range(2,row_num+1):
    # 电子表格中的每一行都由普查数据
    state = sheet['B'+str(row)].value
    country = sheet['C'+str(row)].value
    population = sheet['D'+str(row)].value

    # 确保每个州的键存在
    countydata.setdefault(state,{})

    # 确保该州的县的键存在
    countydata[state].setdefault(country,{'tracts':0,'pop':0})

    # 每行都代表一个人口普查区，因此增加1
    countydata[state][country]['tracts'] += 1

    # 在人口普查区域中，按人口增加县的人口
    countydata[state][country]['pop'] += int(population)

# TODO: 打开新的文本文件，并将countydata内容写入
print('Writing result...')
resultfile = open('census2010.py','w')
resultfile.write('alldata = ' + pprint.pformat(countydata))
resultfile.close()
print('Done!')
