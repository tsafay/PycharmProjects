#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/6 17:45
import threading,time

def do_one():
    print('One: ' + time.strftime('%H:%M:%S'))
    time.sleep(5)
    print('One: ' + time.strftime('%H:%M:%S') + '\n')

def do_two():
    print('Two: ' + time.strftime('%H:%M:%S'))
    time.sleep(10)
    print('Two: ' + time.strftime('%H:%M:%S') + '\n')

tsk = []
thread1 = threading.Thread(target=do_one)
thread1.start()
tsk.append(thread1)

thread2 = threading.Thread(target=do_two)
thread2.start()
tsk.append(thread2)

print('START of join:' + time.strftime('%H:%M:%S'))
for ts in tsk:
    ts.join()
print('END of join:' + time.strftime('%H:%M:%S'))