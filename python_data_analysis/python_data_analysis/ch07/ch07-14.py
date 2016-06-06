#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 字符串操作

val = 'a,b, gudio'
# split拆分
print val.split(',')

# 注意到空白符号问题,采用strip
# strip前后去掉, rstrip去掉右边, lstrip去掉左边
pieces = [x.strip() for x in val.split(',')]
print pieces
print '   x  x   '.lstrip()
print '   x  x   '.rstrip()
print '   x  x   '.strip()

first, second, third = pieces
# 可以使用加法拼接
print first + '::' + second + '::' + third
# join方法效率更高,更pythonic
print '::'.join(pieces)

# 通过in来进行子串判断
print 'gudio' in val
# 也可以通过index,find来判断是否在里面
print val.index(',')
print val.find('a')
# 注意find的不在返回-1
print val.find(':')
# 注意index的不在则是异常
# print val.index(':')

# 用replace替换字符
print val
print val.replace(',', '::')
print val.replace(',', '')

# count返回字符串在出现的次数
print val.count(',')

# endswith判断结尾
print val.endswith('io')

# startswith判断开头
print val.startswith('a,')

# rfind 寻找字符串, find是返回串的第一个字符串, rfind是返回最后一个
print val.find(',')
print val.rfind(',')

# lower转换为小写
print 'WWX'.lower()

# upper转换为大写
print 'wwx'.upper()

