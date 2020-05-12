#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/24 21:15
'''
zipfile模块：利用模块函数，python可以创建打开（或解压）zip文件。
'''

# 读取zip文件
import zipfile,os
example = zipfile.ZipFile('aaa.zip') # 返回zipfile对象
spam = example.namelist() # 返回zip文件中包含的所有文件和文件夹的字符串列表
print(spam)

# namelist()方法返回的字符串列表可以传递给zipfile对象的getinfo()方法，返回关于特定的zipinfo对象
spaminfo = example.getinfo('aaa/python.doc')
print(spaminfo.file_size,spaminfo.compress_size)  # 返回字节数：分别表示原文件大小及压缩后文件大小

print('Compressed file is {}x smaller.'\
      .format(round(spaminfo.file_size/spaminfo.compress_size,2)))
example.close()

# 从zip文件中解压
'''
ZipFile 对象的 extractall()方法从 ZIP 文件中解压缩所有文件和文件夹，放到当前工作目录中。
'''
a = os.getcwd()
b = os.path.dirname(a)

# ex_zip = zipfile.ZipFile('aaa.zip')
# 全部解压，默认解压到当前文件夹，可传入文件目录保存解压文件，如果传入的文件夹不存在会被创建
# ex_zip.extractall()
# 解压单个文件，默认解压到当前文件夹，可传入文件目录保存解压文件；返回值是被压缩后文件的绝对路径
# ex_zip.extract('aaa/python.doc')
# ex_zip.close()

# 创建和添加到zip文件
'''
要创建zip文件，必须以’写入/添加模式‘打开新的zipfile对象，即传入’w/a‘作为第二参数
向zipfile对象使用write()方法：第一个参数为字符串，表示要添加的文件名，
第二个参数为’压缩类型‘参数，可以设置为zipfile.ZIP_DEFLATED
'''
new_zip = zipfile.ZipFile('new.zip','w')
new_zip.write('mp.txt',compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()