#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/27 18:53
import requests,bs4,sys,webbrowser
print('It is  searching...')
match = input('输入关键词：')
res=requests.get('https://so.csdn.net/so/search/s.do?q='+ match)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,'lxml')
linkElems=soup.select('.limit_width a')
print(str(len(linkElems))+' Found!')
numOpen=min(5,len(linkElems))
for i in range(numOpen):
      webbrowser.open(linkElems[i].get('href'))
      print(str(linkElems[i].get('href')))
