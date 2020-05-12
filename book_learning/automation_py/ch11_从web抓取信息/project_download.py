#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/28 9:58
'项目：下载所有XKCD漫画'
'''
程序任务：
• 加载主页；
• 保存该页的漫画图片；
• 转入前一张漫画的链接；
• 重复直到第一张漫画。
程序实现：
• 利用 requests 模块下载页面。
• 利用 Beautiful Soup 找到页面中漫画图像的 URL。
• 利用 iter_content()下载漫画图像，并保存到硬盘。
• 找到前一张漫画的链接 URL，然后重复。
'''
import requests,bs4,os
url = 'http://xkcd.com'
os.makedirs('Download',exist_ok=True)
while not url.endswith('#'):
    # TODO: 下载页面
    print('Download page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'lxml')

    # TODO: 查找文件的url
    comicElems = soup.select('#comic img')
    print(len(comicElems))
#     if comicElems == []:
#         print('Could not find comic image.')
#     else:
#         comicUrl = 'http:'+comicElems[0].get('src')
#
#         # TODO: 下载文件
#         print('Downloading image %s...' %(comicUrl))
#         res = requests.get(comicUrl)
#         res.raise_for_status()
#
#     #   TODO：保存文件
#         imageFile = open(os.path.join('Download',os.path.basename(comicUrl)),'wb')
#         for chunk in res.iter_content(100000):
#             imageFile.write(chunk)
#         imageFile.close()
#
#     # TODO：获取上一个按钮的url
#     preLink = soup.select('a[rel="prev"]')[0]
#     url = 'http://xkcd.com' + preLink.get('href')
#
# print('Done.')
