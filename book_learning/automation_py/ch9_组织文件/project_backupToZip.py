#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/25 16:10
'项目：讲一个文件夹备份到一个zip文件'
'''
假定在做一个项目，它的文件保存在文件夹中。你担心工作会丢失，所以希望为整个项目文件夹创建一个zip文件备份；
你希望保存不同版本，每次保存zip文件名都会有所变化，如backup1.zip、backup2.zip···
'''
import os,zipfile

def backupToZip(folder):
    '将文件夹全部内容备份到zip文件中'
    folder = os.path.abspath(folder)  # 保证文件路径是绝对路径
    num = 1
    while True:
        zipPath = 'F:\\test_backup\\backup\\'
        zipFilename =zipPath + os.path.basename(folder) + '_' + str(num) + '.zip'
        if not os.path.exists(zipFilename):
            break
        num += 1

    # TODO: 创建zip文件
    print('Creating {} ...'.format(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename,'w')

    # TODO: 年里问个文件夹树，并压缩每个文件夹中的文件
    # os.walk()返回当前文件夹名称、子文件列表、文件名文件列表
    for foldername,subfolders,filenames in os.walk(folder):
        print('Adding files in {}...'.format(foldername))
        # 将文件夹写入zip文件，如果传入的是一个路径；
        # python将会压缩该路径指定的文件，将它放入zip文件中
        backupZip.write(foldername)
        # 遍历每一个文件
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
    print('Done')


backupToZip('mp.txt')
