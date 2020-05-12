#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/24 14:15
'项目：疯狂填词'
'''
创建一个疯狂填词（Mad Libs）程序，它将读入文本文件，并让用户在该文本文件中出现 
ADJECTIVE、NOUN、ADVERB 或 VERB 等单词的地方，加上他们自己的文本。
结果应该打印到屏幕上，并保存为一个新的文本文件。
'''
import re,os
# text = '''
# The ADJECTIVE panda walked to the NOUN and then VERB.
# A nearby VERB was unaffected by these events.
# '''
file = os.getcwd()
filename = os.path.join(file,'p_madlibs.txt')
f = open(filename)
text = f.read()
f.close()
print(text)

# regex1 = re.compile(r'ADJECTIVE')
# regex2 = re.compile(r'NOUN')
# regex3 = re.compile(r'ADVERB')
# regex4 = re.compile(r'VERB')
# ADJECTIVE = input('Enter ADJECTIVE:')
# text1 = regex1.sub(ADJECTIVE,text)
# NOUN = input('Enter NOUN:')
# text2 = regex2.sub(NOUN,text1)
# ADVERB = input('Enter ADVERB:')
# text3 = regex3.sub(ADVERB,text2)
# VERB = input('Enter VERB:')
# text4 = regex4.sub(VERB,text3)
text_re = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
text_f = text_re.findall(text)
print(text_f)
for libs in text_f:
    lib = input('Enter {}:'.format(libs))
    text = text_re.sub(lib,text,1)

f1 = open('p_madlibs.txt','a')
f1.write(text)
f1.close()
print(text)







