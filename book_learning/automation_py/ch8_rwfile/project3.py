#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/24 15:17
'正则表达式查找'
'''
编写一个程序，打开文件夹中所有的.txt文件，查找匹配用户提供的正则表达式的所有行。结果应该打印到屏幕上。
'''
import re,os
while True:
    regex = input('Enter match:')
    match = re.compile(regex)
    filename = input('Enter path:')
    if os.path.exists(filename):
        if os.path.isfile(filename):
            fileExpand = os.path.basename(filename)
            expand = os.path.splitext(fileExpand)[1]
            if expand == '.txt':
                text = open(filename,encoding='utf-8').read()
                open(filename).close()
                print(os.path.basename(filename) + ':')
                text_all = match.findall(text)
                if len(text_all) == 0:
                    print(None)
                for i in text_all:
                    print(i)
                break
            else:
                print('It\'s not txt file.')
                continue
        else:
            file_list = os.listdir(filename)
            print(len(file_list))
            for file in file_list:
                while os.path.splitext(file)[1] == '.txt':
                    text = open(file,encoding='utf-8').read()
                    open(file).close()
                    print(os.path.basename(file) + ':')
                    text_all = match.findall(text)
                    if len(text_all) == 0:
                        print(None)
                    for i in text_all:
                        print(i)
                    break
            break
    else:
        print('Path file does not exist! ')
        continue


