#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# numpy.searchsorted: 在有序数组中查找元素
# searchsorted是在一个有序数组上执行二分查找的数组方法
# 所以先查找, 然后再插入能保持有序
arr = np.array([0, 1, 7, 12, 15])
print arr.searchsorted(9)
1
# 查找一组数
print arr.searchsorted([0, 8, 11, 16])

# 默认返回第一个(左侧匹配的值)
arr = np.array([0, 0, 0, 1, 1, 1, 1])
print arr.searchsorted([0, 1])
# 指定匹配最后一个, 即最右边的下一个
print arr.searchsorted([0, 1], side='right')

# 一个表示面元边界的数组, 我们可以用数据数组拆分开
data = np.floor(np.random.uniform(0, 10000, size=50))
bins = np.array([0, 100, 1000, 5000, 10000])
print data
# 得到各个所属区间的编号, 其中1表示[0, 100)
labels = bins.searchsorted(data)
print labels
# 通过groupby使用结果, 来对结果拆分
print Series(data).groupby(labels).mean()

# Numpy的digitize函数也可以计算面元编号
print np.digitize(data, bins)

