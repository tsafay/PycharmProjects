#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/6 9:05
'项目：超级秒表'
'''
简单的秒表程序：
程序需要：
 记录从按下回车键开始，每次按键的时间，每次按键都是一个新的“单圈”。
 打印圈数、总时间和单圈时间。
程序任务：
 在程序开始时，通过调用 time.time()得到当前时间，将它保存为一个时间戳。在每个单圈开始时也一样。
 记录圈数，每次用户按下回车键时加1。 
 用时间戳相减，得到计算流逝的时间。
 处理 KeyboardInterrupt 异常，这样用户可以按 Ctrl-C 退出。
'''
import time
print('ENTER to begin,ENTER to stop.Press "CTRL—F2" to quit.')
input()
print('Started.')
starttime = time.time()
lasttime = starttime
lapnum = 1

try:
    while True:
        input()
        laptime = round(time.time()-lasttime,2)  # 每圈时长
        totaltime = round(time.time()-starttime,2) # 总计时长
        print('LAP - %s: %s (%s)' %(lapnum,laptime,totaltime),end='')
        lapnum += 1
        lasttime = time.time()
except KeyboardInterrupt:
    print('\nDone.')