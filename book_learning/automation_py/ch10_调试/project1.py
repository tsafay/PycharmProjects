#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/26 22:25
'项目：调试硬币抛掷'
'''
下面的程序是一个简单的猜抛硬币的游戏，玩家有两次猜测机会。但程序中有一些缺陷，找出问题，让程序正常运行。
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
'''
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
guess_answer = ['tails','heads']
toss = random.randint(0, 1) # 0 is tails, 1 is heads
print(guess_answer[toss])
if guess_answer[toss] == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if guess_answer[toss] == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')