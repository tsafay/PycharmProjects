#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/29 10:43
import requests
import re
import time
from bs4 import BeautifulSoup

def get_ip():
    '''批量获取代理IP地址'''
    '''完整ip地址{'HTTP':'ip:port'}'''
    ip_list = []
    for page in range(1,5):
        '''分页获取代理IP地址'''
        print('正在抓取第{}页IP:'.format(page))
        url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
        headers = {'User-Agent':
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                    '(KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

        '''单页面获取代理IP地址'''
        res = requests.get(url,headers=headers)
        html = res.text
        soup = BeautifulSoup(html,'lxml')
        elems = soup.select('tr')

        for i in range(len(elems)):
            # 使用正则表达式分组匹配ip及端口（PORT）数据
            ip_dic = {}
            ip = re.search(r'(data-title="IP">)(.*\d)',str(elems[i]))
            port = re.search(r'(data-title="PORT">)(.*\d)',str(elems[i]))
            if ip == None and port==None:
                continue
            ip_dic['HTTP'] = ip.group(2) + ':' + port.group(2)
            print('HTTP:' + ip.group(2) + ':' + port.group(2))
            ip_list.append(ip_dic)
        time.sleep(1)
    return ip_list

def check_ip(ips):
    '''检查代理IP是否正常'''
    url = 'https://www.baidu.com/'
    headers = {'User-Agent':
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    for ip in ips:
        try:
            res = requests.get(url,headers = headers,proxies=ip,timeout=0.5)
            if res.status_code == 200:
                print(ip,'正常！')
        except Exception as err:
            print(ip,err)

ip = get_ip()
check_ip(ip)


