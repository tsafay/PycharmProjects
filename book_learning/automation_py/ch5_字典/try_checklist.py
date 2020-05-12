# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/22 15:47
stuff = {'rope': 1, 'torch': 6,
         'gold coin': 42, 'dagger': 1,
         'arrow': 12,'knife':3
         }

def checklist(s):
    print('Inventory:')
    number = 0
    for k,v in s.items():
        print(k,v)
        number += v
    print('Total number of items:',number)

checklist(stuff)

loot = ['gold coin','dagger','gold coin','ruby','gold coin']
inv = {'gold coin':42,'rope':1}

def addToInventory(inventory,addItem):
    for va in addItem:
        inventory.setdefault(va,0)
        inventory[va] += 1
    return inventory

adddic = addToInventory(inv,loot)
checklist(adddic)
