#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/29 10:20
'项目：链接验证'
'''
编写一个程序，对给定的网页 URL，下载该页面所有链接的页面。
程序应该标记出所有具有 404“Not Found”状态码的页面，将它们作为坏链接输出。
'''
import requests,bs4
url = 'https://www.scut.edu.cn/new/'
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'lxml')
elems = soup.select('a[href]')
print(elems)
print('在网页{}，共有{}个<a href="">.'.format(url,len(elems)))

for i in range(len(elems)):
    hrefUrl = elems[i].get('href')
    if not hrefUrl.startswith('http:') or hrefUrl.startswith('https:'):
        continue
    try:
        res_href = requests.get(hrefUrl,timeout=0.2)
        if res_href.status_code == 404:
            print('找不到网页{}，404 NOT FOUND...'.format(hrefUrl))
    except requests.exceptions.Timeout:
        print('网页请求超时...')

