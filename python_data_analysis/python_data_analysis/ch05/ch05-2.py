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
# 如果传入指定的列没有相应的数据,那么会以NaN填充,比如下面的debt
frame_columns_without = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                                  index=['one', 'two', 'three', 'four', 'five'])
# print frame_columns_without
# 对应的列标签
# print frame_columns_without.columns

# 2种方式访问对应columns,一种是类似dict的方式,一种是类似class属性的方式
# print frame_columns_without['state']
# print frame_columns_without.year

# 可以通过ix来访问对应的行
# print frame_columns_without.ix['three']

# 列可以通过赋值的方式进行修改
frame_columns_without['debt'] = 16.5
# print frame_columns_without
frame_columns_without['debt'] = np.arange(5.)
# print frame_columns_without

# 将列表或数组赋值给某个列时,其长度必须和DataFrame的长度匹配
# 如果赋值的是Series,那么会精确匹配DataFrame的索引,同时空位被填上缺失值
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame_columns_without['debt'] = val
print frame_columns_without

# 为不存在的值赋值会创建出一个新列
frame_columns_without['estern'] = frame_columns_without.state == 'Ohio'
# print frame_columns_without