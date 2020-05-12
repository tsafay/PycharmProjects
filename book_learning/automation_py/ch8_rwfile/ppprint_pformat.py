# -*- coding: utf-8 -*-
# @Author  : leejufe    
# @Date    : 2020/4/23 21:24
'使用pprint.pformat()函数保存变量'
'''
假定有一个字典，保存在一个变量中，你希望可以保存这个变量和内容，便于以后使用；
pprint.pformat()函数将提供一个字符串，可以写入.py文件。该文件将成为私有的模块；
当需要时，可以导入使用它。
import_mycat
'''
import pprint
cat = [{'name': 'Zophie', 'desc': 'chubby'},
       {'name': 'Pooka', 'desc': 'fluffy'}
      ]
print(pprint.pformat(cat))
fileObj = open('mycat.py','w')
fileObj.write('cat = ' + pprint.pformat(cat) + '\n')
fileObj.close()