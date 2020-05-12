# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/22 15:27
allGuests = {'Alice':{'apples':5,'pretzels':12},
             'Bob':{'sandwiches':3,'apples':2},
             'Carol':{'cups':3,'apple pies':1}
             }

def totalBrought(guest,item):
    numBroght = 0
    for v in guest.values():
        # 字典的get()方法，它有两个参数：要取得其值得键，以及如果键不存在时返回的备用值
        numBroght += v.get(item,0)
    return numBroght
print('Number of things being brought:')
print('— Apples:',totalBrought(allGuests,'apples'))
print('— Sandwiches:',str(totalBrought(allGuests,'sandwiches')))
print('— Pretzels:',str(totalBrought(allGuests,'pretzels')))

