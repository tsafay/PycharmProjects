#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/5 20:35
'项目：从csv文件中删除表头'
'''
假设有几百个csv文件要删除第一行：
程序任务：
• 找出当前工作目录中的所有 CSV 文件。
• 读取每个文件的全部内容。
• 跳过第一行，将内容写入一个新的 CSV 文件。
程序实现：
• 循环遍历从 os.listdir()得到的文件列表，跳过非 CSV 文件。
• 创建一个 CSV Reader 对象，读取该文件的内容，利用 line_num 属性确定要跳过哪一行。
• 创建一个 CSV Writer 对象，将读入的数据写入新文件。
'''
import csv,os
os.makedirs('remove',exist_ok=True)
for csvfilename in os.listdir('.'):
    if not csvfilename.endswith('.csv'):
        continue
    print('Removing header from ' + csvfilename + '...')

    # TODO：读取csv文件第一行
    csvrows = []
    csvfile = open(csvfilename)
    csvread = csv.reader(csvfile)
    for row in csvread:
        if csvread.line_num == 1:
            continue
        csvrows.append(row)
    csvfile.close()

    # TODO: 写入新的csv文件；
    csvnew = open(os.path.join('remove',csvfilename),'w',newline='')
    csvwrite = csv.writer(csvnew)
    for row in csvrows:
        csvwrite.writerow(row)
    csvnew.close()