#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/25 16:40
# ! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

#!/usr/bin/python
# -*- coding: UTF-8 -*-
# backupToZip - Copies an entire folder and its contents into a ZIP file whose filename increments
import zipfile,os

def backupToZip(folder):  #folder参数为需要备份的文件夹的路径
    folder=os.path.abspath(folder)  #返回一个绝对路径
    number=1
    while 1:
        #os.path.basename():返回path最后的文件名
        #创建一个zip文件名
        zipPath='F:\\'  #定义zip文件存储路径
        zipFileName=zipPath+os.path.basename(folder)+'_'+str(number)+'.zip'
        #用于寻找一个还没使用过的zip文件名，如果存在则继续寻找，如果不存在则停止寻找，并得到一个之前不存在的zip文件名
        #os.path.exists()：判断括号里的文件/文件路径是否存在
        if not os.path.exists(zipFileName):
            break
        number+=1
    #创建zip文件
    print('Creating %s...' %(zipFileName))
    #创建一个zip文件，文件名为zipFileName，’w'表示压缩
    backupZip=zipfile.ZipFile(zipFileName,'w')
    #os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下，
    #每次迭代中，它将返回这次迭代当前的文件夹名称、 这个文件夹中的子文件夹，
    # 以及这个文件夹中的文件名
    #参考链接：https://www.runoob.com/python/os-walk.html
    for foldername,subfolders,filenames in os.walk(folder):
        print('Adding files in %s...' %(foldername))
        #将文件夹名写入zip
        #如果向 ZipFile 对象的 write()方法传入一个路径，Python 就会压缩该路径所指的文件，将它加到 ZIP 文件中。write()方法的第一个参数是一个字符串，代表要添加的文件名
        backupZip.write(foldername) #将需备份的文件夹的各层文件夹（从最外层到最内层）放入zip
        #循环遍历，将每一个文件写入zip
        for filename in filenames:
            # 保证之前生成的zip文件不会被添加到新的zip文件中
            newBase=os.path.basename(folder)+'_' #获取需备份的文件夹的文件名
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            #将各层文件夹内的文件按照路径映射关系写入zip
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
    print('Done')

backupToZip(os.path.dirname(os.getcwd()))  #调用函数，参数为文件夹路径字符串，此路径及文件夹需真实存在，否则会返回一个空的zip文件