#!/usr/bin/env python
# encoding=utf-8

import pandas as pdf
import numpy as np
from pandas import Series, DataFrame

# dataframe是一个表格型的数据结构
# 包含一组有序的列,每列的类型可以不同
# 可以有行索引,列索引, 可以看成Series组成的字典(共用同一个索引)
# 其中数据是以一个或者多个二维块存放

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevda'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# 默认方法,会自动加上索引
frame = DataFrame(data)
#print frame
# 可以指定列序列,这样DataFrame的列就会按照指定的顺序进行排列
frame_columns_order = DataFrame(data, columns=['year', 'state', 'pop'])
# print frame_columns_order
# [

