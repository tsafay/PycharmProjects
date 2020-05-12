#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/6 10:12
import threading,time

# 主线程
print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')

# 次线程  调用takeANap函数
threadobj = threading.Thread(target=takeANap)
threadobj.start()

print('End of program.')