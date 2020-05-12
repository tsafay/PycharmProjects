#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/7 22:12
'项目：鼠标在哪里'
'''
能够确定鼠标位置，对于建立GUI自动化脚本是很重要的。但光看屏幕很难确认鼠标坐标。
如果有一个程序在移动鼠标时随时显示坐标就会很方便。
程序任务：
 获得鼠标当前的 xy 坐标。
 当鼠标在屏幕上移动时，更新这些坐标。
程序实现：
 调用函数取得当前坐标。
 在屏幕上打印回退制服。删除以前打印的坐标。
 处理异常。让用户能按键退出。
'''
import pyautogui
print('Press CTRL-C to quit.')
try:
    while True:
        x,y = pyautogui.position()
        position = 'X:' + str(x).rjust(4) + ' ' + 'Y:' + str(y).rjust(4)
        pixecolor = pyautogui.screenshot().getpixel((x,y))
        position += ' RGBA:(' + str(pixecolor[0]).rjust(3)
        position += ', ' + str(pixecolor[1]).rjust(3)
        position += ', ' + str(pixecolor[2]).rjust(3) + ')'
        print(position,end='')
        print('\b'*len(position),end='',flush=True)

except KeyboardInterrupt:
    print('\nDone.')
