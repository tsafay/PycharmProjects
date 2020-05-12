#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/26 20:13
def boxPrint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol*width)  # 打印width遍symbol
    # 循环打印
    for i in range(height-2):
        print(symbol + (' '*(width-2))+symbol)
    print(symbol*width)  # 打印width遍symbol

for sym,w,h in (('*',4,4),('0',20,5),('x',1,2),('zz',3,3)):
    try:
        boxPrint(sym,w,h)
    except Exception as err:
        print('An exception happened:',str(err))