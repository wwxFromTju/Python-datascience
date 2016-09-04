#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 数组的合并和拆分
# numpy.concatenate可以按指定轴将一个由数组组成的序列连接到一起
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print np.concatenate([arr1, arr2], axis=0)
print np.concatenate([arr1, arr2], axis=1)

# 对于常见的连接操作, Numpy提供了一些比较方便的方法(vstack和hstack)
# v: Vertical 竖直
print np.vstack((arr1, arr2))
# h: horizontal 水平
print np.hstack((arr1, arr2))

# split将一个数组沿指定轴拆分为多个数组
arr = np.random.randn(5, 2)
print arr

first, second, third = np.split(arr, [1, 3])
print first
print second
print third

# 下面是关于数组连接和拆分的函数
# concatenate           最一般化的连接, 沿一条轴连接一组数组
# vstack/row_stack      以面向行的方式对数组进行堆叠(沿轴0)
# hstack                以面向列的方式对数组进行堆叠(沿轴1)
# column_stack          类似hstack, 但是会将一维数组转换为二维列向量
# dstack                以面向'深度'的方式对数组进行堆叠(沿轴二)
# split                 沿指定轴在指定的位置拆分数组
# hsplit vsplit dsplit  split的便捷化函数, 分别沿轴0, 轴1, 轴2进行拆分

# 堆叠辅助类: r_和c_
# Numpy命名空间中有2个特殊的对象---r_和c_, 它们可以使数组的堆叠操作更为简洁
arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = np.random.randn(3, 2)
print arr1
print arr2
print np.r_[arr1, arr2]
print np.c_[np.r_[arr1, arr2], arr]

#  将切片翻译成数组
print np.c_[1:6, -10:-5]



