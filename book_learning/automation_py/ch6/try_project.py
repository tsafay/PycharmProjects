# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/22 20:29
'要求列表格式化,每列右对齐'
'''输出：
  apples Alice dogs
 oranges Bob   cats
cherries Carol moose
  banana David goose
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']
             ]

def printTable(test):
    # 求每个内层列表最长字符串的长度
    colWidth = [0]*len(test)
    for i in range(len(colWidth)):
        colWidth[i] = len(sorted(test[i],key=(lambda x: len(x)))[-1])

    # 转置打印列表
    for x in range(len(test[0])):
        for y in range(len(test)):
            print(test[y][x].ljust(colWidth[y]),end=' ')
        print()

printTable(tableData)