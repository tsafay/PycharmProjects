#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/25 21:48
'项目：删除不需要的文件'
'''
编写一个程序，遍历目录树，查找特别大的文件或文件夹，比如超过100M的文件，将这些文件打印到屏幕上；
获取文件大小可使用os.path.getsize()
'''
import os
def getSize(file):

    absfile = os.path.abspath(file)

    file_size = 0

    for foldername,subfolders,filenames in os.walk(absfile):
        # print('当前文件目录：',foldername)
        # if len(subfolders) != 0:
        #     for subfolder in subfolders:
        #         newpath = os.path.join(foldername,subfolder)
        #         for i in os.listdir(newpath):
        #             i_size = os.path.getsize(os.path.join(newpath,i))
        #             # print(i,':',str(round(i_size/1024,2))+'KB')
        #             print(i, ':', str(i_size) + 'KB')
        #             sub_size += i_size
        #         # print('子文件夹'+subfolder,':',str(round(sub_size/1048,2))+'KB')
        #         print('子文件夹' + subfolder, ':', str(sub_size) + 'KB')
        #     # print('当前文件夹总计：',str(round(sub_size/1048,2))+'KB')
        #     print('当前文件夹总计：', str(sub_size) + 'KB')
        sub_size = 0
        for filename in filenames:
            filename_size = os.path.getsize(os.path.join(foldername,filename))
            # print(filename,':',str(round(filename_size/1024,2))+'KB')
            #print(filename, ':', str(filename_size) + 'KB')
            file_size += filename_size
            #print('此目录内文件'+filename,':',str(round(sub_size/1048,2))+'KB')
            sub_size += filename_size
        print('此目录内文件' + foldername, '字节为:', str(sub_size) + 'KB')
    # print('此目录内文件总计：\n', str(round((sub_size+file_size) / 1048, 2)) + 'KB')
    print('查找目录内文件总计：\n', str(file_size) + 'KB')

file = os.path.dirname(os.getcwd())
getSize(file)

