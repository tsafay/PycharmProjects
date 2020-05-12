#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/8 17:08
'项目：即时通信机器人'
import pyautogui,time,sys

time.sleep(2)

try:
    print('Locating the position...')
    pyautogui.click(pyautogui.locateOnScreen('wuyu.png'))
except TypeError:
    print('Fail to finding the postion.')
    sys.exit()

print('Reading for sending...')
pyautogui.typewrite('Hello world!')

print('You have 5 seconds to check before sending the message.\nPress '
      'CTRL-C to quit.')

try:
    time.sleep(5)
    pyautogui.press('enter')
except KeyboardInterrupt:
    print('Message has been failed send.')
print('Message has benn sent.')

