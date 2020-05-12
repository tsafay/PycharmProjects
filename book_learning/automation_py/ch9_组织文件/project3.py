#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/26 9:00
'项目：消除消失的编号'
'''
编写一个程序，在一个文件夹中找到所有带指定前缀的文件，如spam001.txt、spam002.txt等。并定位缺失的编号，
如存在spam001.txt、spam003.txt，但不存在spam002.txt。让程序对后面的所有后面的文件改名，消除缺失的编号。
附加挑战任务:
编写另一个程序，在一些连续编号的文件中，空出一个编号，以便加入新的文件。
'''
import os,re,shutil

# 新建连续缺失编号的文件
# os.makedirs('spam',exist_ok=True)
# folder = os.path.join(os.getcwd(),'spam')
# for i in range(1,101):
#     if i % 3 != 0:
#         txtname = 'spam' + str(i).rjust(3,'0') + '.txt'
#         filename = os.path.join(folder,txtname)
#         with open(filename, 'w') as f:
#             f.write('Hello world {}'.format(i))

regex = re.compile(r'^spam(\d{3})\.txt$')
filename = os.path.join(os.getcwd(),'spam')
files = os.listdir('spam')
filenums = []
for file in files:
    filenum = regex.search(file).group(1)
    filenums.append(filenum)

for i in range(len(filenums)):
    fileNew = 'spam' + str(i + 1).rjust(3, '0') + '.txt'
    fileOld = 'spam' + filenums[i] + '.txt'
    if int(filenums[i]) != i+1:
        print(os.path.join(filename,fileOld),
              os.path.join(filename,fileNew))
        # shutil.move(原文件，目的地文件)，尤其警惕路径是否正确
        shutil.move(os.path.join(filename,fileOld),os.path.join(filename,fileNew))



