#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/25 10:23
'项目：将带有美国风格日期(MM-DD-YYY)的文件名改为欧洲风格日期(DD-MM-YYY)文件名'
'''
程序任务：
• 检查当前工作目录的所有文件名，寻找美国风格的日期。
• 如果找到，将该文件改名，交换月份和日期的位置，使之成为欧洲风格。
程序实现：
• 创建一个正则表达式，可以识别美国风格日期的文本模式。
• 调用 os.listdir()，找出工作目录中的所有文件。
• 循环遍历每个文件名，利用该正则表达式检查它是否包含日期。
• 如果它包含日期，用 shutil.move()对该文件改名。
类似程序想法：
• 为文件名添加前缀，诸如添加 spam_，将 eggs.txt 改名为 spam_eggs.txt。 
• 将欧洲风格日期的文件改名为美国风格日期。
• 删除文件名中的 0，诸如 spam0042.txt。
'''
import re,shutil,os
date_re = re.compile(r'''  # 每有一个左括号，分组编号加一
          ^(.*?)             #1 日期前的文本
          ((0|1)?\d)-        #2、3 表示月的一位或两位数字
          ((0|1|2|3)?\d)-    #4、5 表示日的一位或两位数字
          ((19|20)\d{2})     #6、7 表示年的四位数字
          (.*?)$             #8 日期后的所有文本
          ''',re.VERBOSE)

# TODO: 在工作目录中循环
for amerfilename in os.listdir('.'):
    mo = date_re.search(amerfilename)

    # TODO: 没有日期的跳过文件
    if mo == None:
        continue
# TODO: 得到原文件名的不同部分
    beforepart = mo.group(1)
    monthpart = mo.group(2)
    daypart = mo.group(4)
    yearpart = mo.group(6)
    afterpart = mo.group(8)

    # TODO: 形成欧式的文件名
    eurofilename = beforepart + daypart + '-' + monthpart + \
                   '-' + yearpart + afterpart

    # TODO: 获取完整的绝对路径
    #absworkingdir = os.path.abspath('.')
    absworkingdir = os.getcwd()
    amerfilename = os.path.join(absworkingdir,amerfilename)
    eurofilename = os.path.join(absworkingdir,eurofilename)
    # print(absworkingdir)
    # print(amerfilename)
    # print(eurofilename)

    # TODO: 重命名文件
    print('Renaming "{}" to "{}"...'.format(amerfilename,eurofilename))
    # 测试无误后取消shutil.move()注释
    shutil.move(amerfilename,eurofilename)