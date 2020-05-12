#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/8 15:44
import pyautogui
# 获取屏幕截图
im = pyautogui.screenshot()
im.save('screen.png')
# 获取图片在屏幕截图的位置
print(pyautogui.locateOnScreen('screen2.png'))

#pyautogui.click(pyautogui.center((909,1036,31,30)))
