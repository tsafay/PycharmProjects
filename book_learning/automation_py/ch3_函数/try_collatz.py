# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/21 19:25

def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3*num + 1

# number = input('Enter number:\n')
# enter_num = int(number)
# s = collatz(enter_num)
# i = 0
# while i >= 0:
#     i += 1
#     if s == 1:
#         print(s)
#         print('循环了', i, '次。')
#         break
#     else:
#         print(s)
#         s = collatz(s)




try:
    i = 0
    number = input('Enter a number:\n')
    enter_num = int(number)
    s = collatz(enter_num)
    while i >= 0:
        i += 1
        if s == 1:
            print(s)
            print('循环了', i, '次。')
            break
        else:
            print(s)
            s = collatz(s)
except ValueError:
    print('Enter error.try again.')
