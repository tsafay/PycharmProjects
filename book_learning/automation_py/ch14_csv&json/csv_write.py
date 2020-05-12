#！python3
# -*- coding: utf-8 -*-
# @Author  : lee 
# @Date    : 2020/5/5 20:16
import csv
outfile = open('out.csv','w',newline='')
# csv默认逗号分隔单元格，可使用delimiter及lineterminator参数来分隔单元格和设置行距
outwrite = csv.writer(outfile,delimiter='\t',lineterminator='\n\n')
outwrite.writerow(['spam','eggs','bacon','ham'])
outwrite.writerow(['Hello','world','bac','hanm'])
outwrite.writerow([1,343,65,788])
outfile.close()
