# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/21 20:17
catname = []
while True:
    name = input('Enter the name of cat ' + str(len(catname)+1) + ':')
    if name == '':
        break
    catname += [name]
print('The name of cat are:')
for i in range(len(catname)):
    print(i,':',catname[i])