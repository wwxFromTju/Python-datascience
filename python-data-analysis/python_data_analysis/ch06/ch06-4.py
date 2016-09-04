#!/usr/bin/env python
# encoding=utf-8

import csv

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 手工处理分隔符
# 主要是处理一些异常的情况

# 用来定义csv.Dialect的子类来指定新格式
class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ','
    quotechar = '"'
    quoting = csv.QUOTE_ALL


print ord('"')
# 下面的命令在ipython中运行
# !cat ex7.csv
# 对于单字符分隔符文件,可以直接使用Python内置的csv模块
f = open('ex7.csv')
reader = csv.reader(f)
# 迭代出list
for line in reader:
    print line

# 对数据格式进行处理
lines = list(csv.reader(open('ex7.csv')))
header, values = lines[0], lines[1:]
data_dcit = {h: v for h, v in zip(header, zip(*values))}
print data_dcit

# 使用自己定义的csv格式
f = open('ex7.csv')
reader = csv.reader(f, dialect=my_dialect)
for line in reader:
    print line

# 也可以直接指定相应属性
f = open('just|.csv')
reader = csv.reader(f, delimiter='|')
for line in reader:
    print line

# csv选项
# delimiter 用于指定分隔符字段单字符字符串,默认为 ","
# lineterminator 用于写操作的行结束符, 默认为"\r\n" 读操作会忽略这个选项,可是识别跨平台
# quotechar 用于带特殊字符(如分隔符)的字段的引用符号。默认为'"'
# quoting 用于约定, csv.QUOTE_ALL(引用所有字段), csv.QUOTE_MINIMAL(只引用带有诸如分隔符之类的特殊字符的的字段)csv.QUOTE_NONNUMERIC/csv.QUOTE_NON(不引用)
# skipinitialspace 忽略分隔符后面的空白符, 默认为False
# doublequote 如何处理字段内的引用符号。如果True,则双写。
# escapechar 对分隔符进行转义的字符串

# 要手工输出分隔符文件,可以使用csv.writer
# 接受一个打开且可写的文件对象,以及跟csv.reader相同的那些语支和格式化选项
with open('mydata.csv', 'w') as f:
    writer = csv.writer(f, dialect=my_dialect)
    writer.writerow(('one', 'two', 'three'))
    writer.writerow(('1', '2', '3'))
    writer.writerow(('4', '5', '6'))
    writer.writerow(('7', '8', '9'))
