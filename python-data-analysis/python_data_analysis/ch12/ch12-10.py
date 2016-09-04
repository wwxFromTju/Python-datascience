#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# ufunc高级应用
# Numpy的各个二元ufunc都有一些用于执行特定矢量化运算的特殊方法


# reduce接受一个数组参数, 通过一系列的二元运算可以对其值进行聚合(可以指明轴向)
# 对数组各元素进行求和
arr = np.arange(10)
print np.add.reduce(arr)
print arr.sum()

# 用np.logical_and检查数组各行的值是否有序
arr = np.random.randn(5, 5)
arr[::2].sort(1)
print arr[:, :-1] < arr[:, 1:]
# 等价于下面的方法
print np.logical_and.reduce(arr[:, :-1] < arr[:, 1:], axis=1)

# accumulate跟reduce的关系类似cumsum跟sum类似
# 它产生一个跟原数组大小相同的中间'累计'数组:
arr = np.arange(15).reshape((3, 5))
print np.add.accumulate(arr, axis=1)

# outer用于计算2个数组的叉积
arr = np.arange(3).repeat([1, 2, 2])
print arr
print np.multiply.outer(arr, np.arange(5))

# outer的输出结果的维度是两个输入数据的维度之和
result = np.subtract.outer(np.random.randn(3, 4), np.random.randn(5))
print result.shape

# reduceat用于计算'局部约简', 其实就是一个对数据各切片进行聚合的groupby运算
# 它接受一组用于指示如何对值进行拆分和聚合的面元边界
arr = np.arange(10)
# arr[0:5], arr[5:8] arr[8:] 上执行的约简
print np.add.reduceat(arr, [0, 5, 8])
# 设置axis
arr = np.multiply.outer(np.arange(4), np.arange(5))
print arr
print np.add.reduceat(arr, [0, 2, 4], axis=1)

# ufunc方法
# reduce(x) 通过连续执行原始运算的方式对值进行聚合
# accumulate(x) 聚合值, 保留所有局部聚合结果
# reduceat(x, bins) '局部'约简(也就是groupby)。约简数据的各个切片以产生聚合型数组
# outer(x, y) 对x和y种的每对元素应用原始运算。 结果数组的形状为x.shape + y.shape

