#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/24 9:47
'项目：多重剪切板'
'''
程序任务：
• 针对要检查的关键字，提供命令行参数。
• 如果参数是 save，那么将剪贴板的内容保存到关键字。
• 如果参数是 list，就将所有的关键字拷贝到剪贴板。
• 否则，就将关键词对应的文本拷贝到剪贴板。
程序实现：
• 从 sys.argv 读取命令行参数。
• 读写剪贴板。
• 保存并加载 shelf 文件
'''
import shelve,pyperclip,sys
mcbShelve = shelve.open('mcb')
# TODO:保存粘贴板内容
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelve[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelve[sys.argv[2]]
elif len(sys.argv) == 2:
    # TODO:列出关键字并加载内容
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelve.keys())))
    elif sys.argv[1] in mcbShelve:
        pyperclip.copy(mcbShelve[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        mcbShelve.clear()
        print('All data have been delete.')

mcbShelve.close()

