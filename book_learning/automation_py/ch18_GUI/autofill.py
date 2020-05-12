#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/8 16:36
'项目：自动填表'
'''
程序任务：
 点击表单的第一个文本字段。
 遍历表单，在每个输入栏键入信息。
 点击 Submit 按钮。
 用下一组数据重复这个过程。
程序实现：
 调用 pyautogui.click() 函数，点击表单和 Submit 按钮。
 调用 pyautogui.typewrite() 函数，在输入栏输入文本。
 处理 KeyboardInterrupt 异常，这样用户能按 Ctrl-C 键退出。
'''
import pyautogui,time
