#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/24 20:58
'遍历目录树'
'''
os.walk(path)函数，可以再for循环中使用，返回三个值:
1．当前文件夹名称的字符串。
2．当前文件夹中子文件夹的字符串的列表。
3．当前文件夹中文件的字符串的列表。
类似程序：
你可以在其他程序中遍历一个目录树，将文件添加到压缩的 ZIP 归档文件中。例如，你可以编程做下面的事情：
• 遍历一个目录树，将特定扩展名的文件归档，诸如.txt 或.py，并排除其他文件。
• 遍历一个目录树，将除.txt 和.py 文件以外的其他文件归档。
• 在一个目录树中查找文件夹，它包含的文件数最多，或者使用的磁盘空间最大。
'''
import os
f = os.getcwd()
print(f)
f1 = os.path.dirname(f)
print(f1)
# os.walk()返回当前文件夹名称、子文件列表、文件名文件列表
for foldername,subfolders,filenames in os.walk(f1):
    print('The current folder is',foldername)

    for subfolder in subfolders:
        print('SUBFOLDER OF',foldername,':',subfolder)
    for filename in filenames:
        print('FILE INSIDE',foldername,':',filename)
    print('··· ···')
