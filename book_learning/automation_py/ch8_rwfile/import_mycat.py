# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/23 21:27

# import mycat
# s = mycat.cat
# s1 = mycat.cat[0]
# s2 = mycat.cat[0]['name']
# print(s)
# print(s1)
# print(s2)

import os
print(os.path.splitext('p_madlibs.txt'))

with open('p_madlibs.txt') as f:
    print(f.read())
