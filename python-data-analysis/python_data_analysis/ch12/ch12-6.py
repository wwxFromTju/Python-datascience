#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 元素的重复操作: tile和repeat
# 由于Numpy有广播(broadcasting), 所以很少需要对数组进行重复(replicate)

# 对数组进行重复以产生更大数组的工具, 主要是repeat/tile这两个函数
# repeat会将数组中的各个元素重复一定次数, 从而产生一个更大的数组:
arr = np.arange(3)
print arr
print arr.repeat(3)
# 可以指定不同元素重复不同次数
print arr.repeat([2, 3, 4])
# 对于多维数组, 可以让它们的元素沿指定轴重复
arr = np.random.randn(2, 2)
print arr
print arr.repeat(2, axis=0)

# 如果没有设置轴向, 则数组会被扁平化。 在对多维进行重复时, 可以传入一组整数, 使各切片重复不同的次数
print arr.repeat([2, 3], axis=0)
print arr.repeat([2, 3], axis=1)

# tile: 沿指定轴向堆叠数组的副本
# 和repeat不同, repeat是元素级别的复制, tile是整体的复制
print arr
print np.tile(arr, 2)
# 第二个参数元组为布局, (x, y): 在水平方向复制y, 在竖直方向复制x
print np.tile(arr, (2, 1))
print np.tile(arr, (3, 2))
