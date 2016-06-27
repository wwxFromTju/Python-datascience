#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 高级数组操作

# 数组重塑
# 不需要复制, 将一个数组从一个形状转换为另外一个形状
arr = np.arange(8)
print arr
print arr.reshape((4, 2))

# 重塑多维数组
print arr.reshape((4, 2)).reshape((2, 4))

# 塑造多维数组的时候, 维度的参数为-1值得是: 大小通过数据本身推断而来
arr = np.arange(15)
# 推断为(5, 3)
print arr.reshape((5, -1))

# shape属性是一个元组, 所以可以传入shape
other_arr = np.ones((3, 5))
print other_arr.shape
print arr.reshape(other_arr.shape)

# 与reshape相反的过程称为扁平化(flattening)或散开(raveling)
arr = np.arange(15).reshape((5, 3))
print arr
# 如果没有必要, ravel不会产生源数据的副本
print arr.ravel()
# flatten方法的行为类似ravel, 但是总是返回数据的副本
print arr.flatten()
