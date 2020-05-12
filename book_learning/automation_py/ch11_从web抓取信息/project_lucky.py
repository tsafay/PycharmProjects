#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/27 15:02
'项目：“I’m Feeling Lucky” Google查找'
'''
在网上搜索一个主题时，都不会只看一个结果，通常会看前几个不同单位链接，在新的选项卡打开。
通常步骤：打开浏览器，输入查找主题，依次点击链接。
如果只要在命令行中查找主题，就能让计算机自动打开浏览器，并在新的选项卡中显示前几项的查询结果。
程序任务：
• 从命令行参数中获取查询关键字。
• 取得查询结果页面。
• 为每个结果打开一个浏览器选项卡。
程序实现：
• 从 sys.argv 中读取命令行参数。
• 用 requests 模块取得查询结果页面。
• 找到每个查询结果的链接。
• 调用 webbrowser.open()函数打开 Web 浏览器。
'''
import requests,webbrowser,bs4
match = input('输入查找内容：')
print('Logging...')
# head ={'User-Agent' :'Mozilla/5.0 '
#                      '(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
#                      '(KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
h = {'Host':'www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) '
                  'Gecko/20100101 Firefox/75.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd='
               'python%E5%BF%AB%E9%80%9F%E4%B8%8A%E6%89%8B%E5%88%A0%E9%99%A4%E4%B8%8'
               'D%E9%9C%80%E8%A6%81%E7%9A%84%E6%96%87%E4%BB%B6',
    'Connection': 'keep-alive',
    'Cookie': 'BAIDUID=E3E4B23AE224BF090875CF7CC8BD76EC:FG=1; '
              'BIDUPSID=E3E4B23AE224BF0984F65A7600682CB7; PSTM=1588067057; '
              'BD_UPN=13314752; H_PS_PSSID=1454_21096_31593_31270_31464_31229_30823_31163; '
              'H_PS_645EC=cae6VaKnZ2ZWMmYyx1aaBiU9iJ7RYZ0%2BPFP3nfqCXRyszhm%2BJ1sxgqP%2BIso; '
              'BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=3'
     }
res = requests.get('https://www.baidu.com/s?wd=' + match,headers = h)
res.encoding = res.apparent_encoding
res.raise_for_status()

# TODO:检索顶部搜索链接
soup = bs4.BeautifulSoup(res.text,features='lxml')

# TODO:打开每个浏览器结果的选项卡
linkElems = soup.select('.t a')
#print(linkElems)

for i in range(len(linkElems)):
    print(linkElems[i].get('href'))
    #print(linkElems[i].get('href'))
    #webbrowser.open(linkElems[i].get('href'))