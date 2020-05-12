#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/25 20:35
'项目：选择性拷贝'
'''
编写一个程序，遍历一个目录树，查找特定扩展名文件，不论这些文件在哪里，将他们拷贝到一个新的文件夹中。
程序实现：
1、使用os.walk()函数遍历目录树
2、在目录树中查找特定的拓展名文件；
3、使用shutil模块的copy()函数将查找的文件拷贝到新的文件夹中；
'''
import shutil,os
def expandCopy(file):
    for foldername,subfoldernames,filenames in os.walk(file):
        print('当前查询文件夹是',foldername)
        # print('拷贝文件：')
        backup_path = 'F:\\test_backup\\backup'
        for filename in filenames:
            if os.path.basename(filename).endswith('.py'):
                print(os.path.basename(filename))
                print('Moving',filename,'to',backup_path + '...')
                shutil.copy(os.path.join(foldername,filename),backup_path)
    print('Done.')

expandCopy(r'F:\PycharmProjects\book_learning\concise_py')
