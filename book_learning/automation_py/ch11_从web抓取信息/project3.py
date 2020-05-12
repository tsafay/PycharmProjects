#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/29 9:59
'2048'
'''
2048 是一个简单的游戏，通过箭头向上、下、左、右移动滑块，让滑块合并。
实际上，你可以通过一遍一遍的重复“上、右、下、左”模式，获得相当高的分数。
编写一个程序，打开 https://gabrielecirulli.github.io/2048/上的游戏，
不断发送上、右、下、左按键，自动玩游戏。
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')
time.sleep(5)
for i in range(100):
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.LEFT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.RIGHT)
print('Done.')

