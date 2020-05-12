#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/4/26 20:35
'日志模块调试'
'''
1、首先导入logging模块；
2、然后编辑：logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
   # level参数还可以设置为INFO、WARNING、ERROR、CRITICAL。
3、使用logging模块函数：logging.debug(str)、logging.info(str)      
    logging.warning(str)、logging.error(str)、logging.critical(str)  

4、日志级别：
    DEBUG     # 最低级别，用于细节，通常只有在诊断问题时使用；
    INFO      # 用于记录程序一般性事件，或确认一切工作正常；
    WARNING   # 表示可能出现的问题，它不会阻止程序工作，但将来可能会；
    ERROR     # 用于记录错误，它导致程序做某事失败；
    CRITICAL  # 最高级别，表示程序致命错误，导致或将导致程序完全停止工作；
'''
import logging
logging.basicConfig(filename='programlog.txt',level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program.')
logging.info('Program is working!')
def factorial(n):
    logging.debug('Start of factorial(%s)' %(n))
    total = 1
    for i in range(1,n+1):
        total *= i
        logging.debug('While i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End os factorial(%s)' %(n))
    return total
print(factorial(5))
logging.debug('End of program.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred')
logging.critical('The program is unable to recover.')

# 禁用日志
'''
在调试完成之后，可能希望日志消息不要在出现在屏幕上。logging.disable()函数禁用日志消息。
向logging.disable()传入要禁用的日志级别，他就会禁用该级别及以下级别的所有日志消息；
如果想禁用所有日志消息，只要在程序中添加logging.disable(logging.CRITICAL)
'''

# 将日志记录到文件
'''
在logging.basicConfig()函数传入filename关键字参数，日志消息会记录到文件中，不会显示在屏幕上。
logging.basicConfig(filename='filename',level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

'''

