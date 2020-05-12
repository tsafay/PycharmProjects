# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/23 20:44
import os,shelve
m = os.getcwd()  # 获取当前文件夹目录
filename = os.path.join(m,'hello.txt')  # 补全hello.txt路径
fileHello = open(filename,encoding='utf-8')
file = fileHello.read()
print(file)
fileHello.close()

# shelve模块，可以将python程序中的变量保存到二进制的shelf文件中
shelf = shelve.open('shelf')
cats = ['pooka','simon','zophie']
shelf['cats'] = cats
print(shelf['cats'])
# shelf值就像字典一样，也有keys()及values()方法
for k,v in shelf.items():
    print(k)
    for i in v:
        print(i)
shelf.close()






