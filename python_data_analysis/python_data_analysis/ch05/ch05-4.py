#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# reindex,创建一个适应新索引的对象
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
# print obj
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
# print obj2
# reindex的同时设定如果新index没有值,则用fill_value来填充
# print obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)

# 时间序列是有序的值, 重新索引的时候可能需要做一些插值处理, 使用method选项既可达到此目的
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
# print obj3.reindex(range(6))
# print obj3.reindex(range(6), method='ffill')
# print obj3.reindex(range(6), method='bfill')
# 其他的method:
# ffill 或 pad 前向填充
# bfill 或 backfill 后向填充

temp_index = ['a', 'b', 'c', 'd']

# reindex 可以修改(行)索引,列
frame = DataFrame(np.arange(9).reshape((3,3)), index=['a', 'c', 'd'],
                  columns=['Ohio', 'Texas', 'California'])
# print frame
frame2 = frame.reindex(temp_index)
# print frame2
# 使用columns关键字可以重新索引列
states = ['Texas', 'Utah', 'California']
# print frame.reindex(columns=states)
# 可以同时对行和列进行重新索引, 但是插值只能按照运用(即轴0)
# print frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill', columns=states)

# 可以使用ix的标签索引功能,重新索引任务可以变得简洁
# 选出temp_index行和states列
print frame.ix[temp_index, states]

# reindex函数的参数
# index 用来做的新索引, index实例或其他序列型的Python数据结构.index会被完全使用,就像没有复制过一样
# method 指明插值的方式
# fill_value 在重新索引的时候,可以引入缺失时填充的替代值
# limit 前向,后向填充时候的最大填充量
# level 在multiindex的指定级上匹配简单索引, 否则选择其子集
# copy 默认为True, 无论如何都复制, 如果设置False,那么相等就不复制
