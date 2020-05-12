#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/8 15:30
import pyautogui,time
time.sleep(5)
pyautogui.click()
dis = 200
while dis > 0:
    pyautogui.dragRel(dis,0,duration=0.5)
    dis -= 8
    pyautogui.dragRel(0,dis,duration=0.5)
    pyautogui.dragRel(-dis,0,duration=0.5)
    dis -= 8
    pyautogui.dragRel(0,-dis,duration=0.5)
