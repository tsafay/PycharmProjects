#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/26 20:27
'取得反向跟踪字符串'
import traceback
try:
    raise Exception('This is the error message.')
except:
    errfile = open('errorinfo.txt','w')
    #traceback模块format_exc()方法获取异常的信息
    errfile.write(traceback.format_exc())
    errfile.close()
    print('The traceback info was written to errorinfo.txt')
