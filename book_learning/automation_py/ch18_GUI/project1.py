#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/8 16:41
'项目：看起来很忙！'
'''
编写脚本，每隔10s动一下鼠标
'''
import pyautogui,time
try:
    while True:
        time.sleep(5)
        pyautogui.moveRel(50,0,duration=0.5)
        pyautogui.moveRel(-50,0,duration=0.5)

except KeyboardInterrupt:
    print('Done.')
