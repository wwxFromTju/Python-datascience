#!/usr/bin/env python
# encoding=utf-8

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# 排序和排名

# Series
obj = Series(range(4), index=['d', 'a', 'b', 'c'])
# 没有排序
# print obj
# 通过index进行排序
# print obj.sort_index()
# 通过values值来进行排序
# print obj.sort_values()
# print obj.order()
# 如果NaN在index上,那么针对index排序会将NaN排在前面
obj_nan_index = Series(range(4), index=['d', np.nan, 'b', np.nan])
# print obj_nan_index
# print obj_nan_index.sort_index()
# 如果NaN在values中,会将NaN放在后面
obj_nan_values = Series([3, 2, 5, np.nan, 0, 10])
# print obj_nan_values
# print obj_nan_values.order()
# print obj_nan_values.sort_values()

# DataFrame
frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
                  columns=['d', 'a', 'b', 'c'])
# 没有排序
# print frame
# 默认通过index的索引排序
# print frame.sort_index()
# 设置通过columns来排序
# print frame.sort_index(axis=1)
# 默认是升序的,可以设置降序
# print frame.sort_index(axis=1, ascending=False)

# 在DataFrame中,如果希望通过一个或多个列中的值进行排序,可以传入给by
frame_by = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
# print frame_by
# print frame_by.sort_index(by='b')
# 先排a,再排b
# print frame_by.sort_index(by=['a', 'b'])

# ranking

# ranking, 会设置一个对应的排名值
obj_rank = Series([7, -5, 7, 4, 2, 0, 4])
# 为各组进行一个平均排名
# 第一列为对应的索引,第二列为对应的排名值,可以通过排名值大小比较
# print obj_rank.rank()
# 可以设置值第一次出现的位置来设置排名值
# print obj_rank.rank(method='first')
# 可以降序排列
# print obj_rank.rank(ascending=False, method='max')

# DataFrame上可以进行行或者列的计算排名
frame = DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1], 'c': [-2, 5, 8, -2.5]})
# print frame
# print frame.rank(axis=1)

# rank时用来破坏平级关系的method
# average 默认 为每个值分配平均排名
# min 使用整个分组的最小排名
# max 使用整个分组的最大排名
# first 按值在原始数据中出现的顺序分配排名

# 带重复值的轴索引
obj_recur = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
# print obj_recur
# 判断索引是否是唯一的
# print obj_recur.index.is_unique
# 对于重复的索引,访问索引返回的是一个Series,如果不是单独的索引,那么返回的是一个标量
# print obj_recur['a']
# print obj_recur['c']
# 对于DataFrame也是一样
df_recur = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
# print df_recur
# print df_recur.ix['b']
