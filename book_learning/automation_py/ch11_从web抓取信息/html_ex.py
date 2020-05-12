#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/27 14:40
import requests,bs4

examfile = open('example.html')
exansoup = bs4.BeautifulSoup(examfile.read(),features='lxml')

# 以下将带有id=‘author’的元素，从html中找出来；
# select()返回一个Tag对象的列表，其中包含所有带有id=‘author’的元素；
elems = exansoup.select('#author')
print(elems)
print(elems[0])
print(str(elems[0]))
print(elems[0].getText()) # 在该元素上调用getText()方法，返回该元素文本，或是内部的html
print(elems[0].attrs)  # attrs返回一个字典，包含该元素的属性'id'，以及id 属性的值'author'。

# 也可以从BeautifulSoup对象中找出<p>元素，
pele = exansoup.select('p')
print('\n',pele)
for x in pele:
    print(str(x) + ':\n' + x.getText())


