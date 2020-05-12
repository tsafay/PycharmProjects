# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/21 18:52
'简单的猜数字程序'
import random

print('I\'m thinking a number between 1 and 20.')
answer_num = random.randrange(1,21)
i = 0
while i >= 0:
    num = input('Tank a guess number:')
    i += 1
    try:
        guess_num = int(num)
        if guess_num == answer_num:
            print('Good job,you guessed my number in',i,'times.')
            break
        elif guess_num > answer_num:
            print('Your guess is too high.')
        else:
            print('You guess is too low.')
    except ValueError:
        print('Enter value error.try again.')
        continue

