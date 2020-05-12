# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/21 20:45
'逗号代码'
'''
以一个列表作为参数，返回一个字符串。该字符串包含所有列表元素，并以逗号隔开，
且最后一个列表元素前插入and
'''

# def comma(test):
#     strs = ''
#     for i in range(len(test)):
#         if i == len(test) - 1:
#             strs += 'and ' + test[i]
#         elif i < len(test) - 1:
#             strs += test[i] + ','
#         else:
#             strs += test[i]
#     return strs

def comma(test):
    a = test.pop()
    a = 'and ' + a
    test.append(a)
    b = ','.join(test)
    return b


spam = ['apples','bananas','tofu','dog']
s = comma(spam)
print(s)

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
       ]

for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x],end=' ')
    print('')

# grid_x = []
# for row in range(len(grid[0])):
#     grid2 = []
#     for column in range(len(grid)):
#         grid2.append(grid[column][row])
#     grid_x.append(grid2)
# for i in grid_x:
#     print(i)


# g1 = list(map(list,zip(*grid)))
# for s in g1:
#     print(s)
