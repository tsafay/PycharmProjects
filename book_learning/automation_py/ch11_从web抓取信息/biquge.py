#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/28 10:42
import requests, re, bs4, os
os.makedirs('story',exist_ok=True)
url = 'https://www.52bqg.com/book_127354/'
res = requests.get(url)  # 获取主页
res.encoding = 'gbk'   # 设定编码
res.raise_for_status()

# 解析HTML，返回BeautifulSoup对象
soup = bs4.BeautifulSoup(res.text,'html.parser')
titles = soup.select('#list a')  # 返回Tag对象列表，表示一个html元素的方式
print(titles)

# 获取小说目录
for i in range(len(titles)):
    title = titles[i].getText()  # getText()方法提取Tag列表元素字符串
    # 获取小说每一章节的href
    titleUrl = url + titles[i].get('href')  # 获取Tag列表元素href
    print('{} 正在写入'.format(title[:4]))
    f = open(os.path.join('story',title+'.txt'),'w')

    # 解析小说章节HTML
    res = requests.get(titleUrl)
    res.encoding = 'gbk'
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#content')
    texts = elems[0].getText()
    contents = re.findall(r'\S+',texts)
    del contents[:2]
    print(''.join(contents)[:20]+'...')
    for content in contents:
        content += '\n'
        f.write(content)
    f.close()

# url = 'https://www.52bqg.com/book_127354/49479963.html'  # starting url
# os.makedirs('天下第九', exist_ok=True)  # store comics in ./xkcd
# res = requests.get(url=url)
# res.encoding = res.apparent_encoding
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text,'html.parser')
# elems = soup.select('#content')
# texts = elems[0].getText()
# print(texts)
#
# conts = re.findall(r'\S+',texts)
# del conts[13:16]
# print(conts)
# f = open('zzz.txt','w')
# for i in conts:
#     if i != '':
#         i += '\n'
#     f.write(i)
# f.close()

