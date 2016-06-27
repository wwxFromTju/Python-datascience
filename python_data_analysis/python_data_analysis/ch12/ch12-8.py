#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 广播
# 广播(broadcasting)指不同形状的数组之间的算术运算的执行方式, 他是一种非常强大的功能

# 将标量值和数组结合会产生最简单的广播
arr = np.arange(5)
print arr
# * 4 被广播到数组的所有元素上了
print arr * 4

# 我们可以通过减去平均值的方式对数组的每一列进行距平化处理
arr = np.random.randn(4, 3)
print arr.mean(0)
demeaned = arr - arr.mean(0)
print demeaned
print demeaned.mean(0)

# 广播的原则
# 如果两个数组的后缘维度(trailing dimension, 即从末尾开始算起的维度)的轴长度相符或者其中一方的长度为1, 则广播相融
# 广播会在缺失和(或)长度为1的维度上进行
# 因为arr是(4, 3) 所以在axis=0上做广播则为(3, 1), 在轴(4, 1)做广播的,则为(4, 1)
print arr
row_means = arr.mean(1)
print row_means.reshape((4, 1))
demeaned = arr - row_means.reshape((4, 1))
print demeaned.mean(1)

# 沿其他轴向广播
# 较小数组的广播维必须为1, 比如上面的平均值的形状最少为(4, 1), 而不是(4, )
# 对于三维中的任何一维上广播本质其实也就是将数据重塑为兼容的形状
# 则出现为了广播而添加一个长度为1的新轴, 可以使用reshape, 但插入轴需要构造一个表示新形状的元组
# Numpy数组提供了一种通过索引机制插入轴的特殊语法
arr = np.zeros((4, 4))
arr_3d = arr[:, np.newaxis, :]
print arr_3d.shape
arr_1d = np.random.normal(size=3)
print arr_1d[:, np.newaxis]
print arr_1d[np.newaxis, :]

# 三维数组对轴2进行距平化
arr = np.random.randn(3, 4, 5)
depth_means = arr.mean(2)
demeaned = arr - depth_means[:, :, np.newaxis]
print demeaned.mean(2)


# 对指定轴进行距平化, 使用索引上的技巧, 通用且不牺牲性能
def demean_axis(arr, axis=0):
    means = arr.mean(axis)

    # 下面这些一般化的东西类似于N维的[:, :, np.newaxis]
    indexer= [slice(None)] * arr.ndim
    indexer[axis] = np.newaxis
    return arr - means[indexer]


