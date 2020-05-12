#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/28 21:03
'项目：网站下载'
'''
编写一个程序，访问图像网站，查找一个类型的图片，然后下载所有查询图像。
可以编写一个程序，访问任何具有查找功能的网站。
'''
import requests,os,bs4,re
os.makedirs('down',exist_ok=True)
url = 'https://image.baidu.com/search/index?' \
      'tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&' \
      'fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&' \
      'istype=2&ie=utf-8&fm=result&pos=history&word='
match = input('输入关键词：')

res = requests.get(url + match)
res.encoding = res.apparent_encoding
res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text,'html.parser')
# imgUrl = soup.find_all('img')
# print(imgUrl)

# 使用正则表达式，在网页源代码中匹配图片链接
scr = re.findall('"objURL":"(.*?)"',res.text,re.S)

print('开始下载图片：')
for i in scr:
    file = '蘑菇头' + str(scr.index(i)+1) + '.jpg'
    try:
        re_scr = requests.get(i,timeout=10)
    except requests.exceptions.ConnectionError:
        print('第{}张下载失败：'.format(scr.index(i)+1))
        continue
    print('第{}张下载完成：'.format(scr.index(i)),i)
    f = open(os.path.join('down',file),'wb')
    f.write(re_scr.content)
    f.close()

'''
目前只抓取一个页面数据，下一步可优化分页抓取。
'''

