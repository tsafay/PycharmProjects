# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/22 9:34
birthdays = {'alice':'12-01','timi':'10-23','joe':'04-15'}
while True:
    name = input('Enter your name[enter q to quit]:')
    if name == 'q':
        break
    if name in birthdays:
        print(name+'\'s birthday is',birthdays[name],'.')
    else:
        print('There do\'nt have birthday information for',name)
        birthday = input('Please enter ' + name + ' birthday:')
        birthdays[name] = birthday
        print('Ok,i\'m known',name+'\'birthday.')
