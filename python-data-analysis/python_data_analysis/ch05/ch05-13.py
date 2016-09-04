#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 层次化索引 hierarchical indexing
data = Series(np.random.rand(10),
              index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                     [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
# print data
# print data.index
# print data['b']
# print data['b': 'c']
# print data.ix[['b', 'd']]
# print data[:, 2]

# 可以使用unstack方法重新安排到一个DataFrame中
# index为外层的属性, colunms为内层的属性
# print data.unstack()
# stack为unstack的逆
# print data.unstack().stack()

# 对于DataFrame每条轴都可以有分层索引
# 如果index或columns中为list中嵌套list的话, 那么在list中连续相同的可以合并
frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', "Colorado"],
                           ['Green', 'Red', 'Green']])
# print frame
# 指定index或columns的names
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
# print frame
print frame['Ohio']
print frame['Ohio']['Green']
print frame.ix['a']
print frame.ix['a']

# 可以单独创建MultiIndex然后复用
print pd.MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorade'], ['Green', 'Red', 'Green']],
                                names=['state', 'color'])

