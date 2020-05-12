# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/22 16:26
'字符串对齐'

def printPicnic(itemDict,leftWidth,rightWidth):
    print('PICNIC ITEMS'.center(leftWidth+rightWidth,'-'))
    for k,v in itemDict.items():
        print(k.ljust(leftWidth,'·') + str(v).rjust(rightWidth))

picnic = {'sandwich':4,'apples':8,'cups':13,'cookies':100}
printPicnic(picnic,20,6)
