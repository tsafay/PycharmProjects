# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/21 17:28

def hello():
    print('Hello')
    print('world')

hello()

def he(name):
    print('Hello',name)

he('tumo')

def getanswer(i):
    if i in range(1,11):
        return 'Ok,it\'s good.'
    else:
        return 'En····'

t = getanswer(2)
m = getanswer(23)
print(t)
print(m)


# 局部作用域不能使用其他局部作用域中的变量
def spam():
    eggs = 100
    bacon()
    print(eggs)
def bacon():
    ham = 111
    eggs = 222

spam()

#全局变量可以在局部作用域中读取
def egg():
    print(eggs)
eggs = 33
egg()
print(eggs)

def spam():
    global egg  # 全局变量
    egg = 'spam'
def bason():
    egg = 'bacon'  # 局部变量
def ham():
    print(egg)  # 全局变量

egg = 42
spam()
print(egg)

def sp():
    print(s)
s = 'da'
sp()
