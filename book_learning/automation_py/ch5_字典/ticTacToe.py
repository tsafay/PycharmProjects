# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/22 10:39
board = {'top_L':' ', 'top_M':' ', 'top_R':' ',
         'mid_L':' ', 'mid_M':' ', 'mid_R':' ',
         'low_L':' ', 'low_M':' ', 'low_R':' '
         }

def printBoard(board):
    print(board['top_L'] + '|' + board['top_M'] + '|' + board['top_R'])
    print('—+—+—')
    print(board['mid_L'] + '|' + board['mid_M'] + '|' + board['mid_R'])
    print('—+—+—')
    print(board['low_L'] + '|' + board['low_M'] + '|' + board['low_R'])

turn = 'X'
for i in range(9):
    printBoard(board)
    print('Turn for ' + '\'' + turn + '\'' + ' move on which space?')
    move = input('Enter space:')
    board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(board)
