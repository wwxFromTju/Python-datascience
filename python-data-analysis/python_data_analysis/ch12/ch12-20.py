#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# HDF5及其他数组的存储方式
# PyTables和h5py这两个Python项目可以将Numpy的数组存储为高效且可压缩的HDF5格式(HDF: 层次化数据格式)

# 性能建议
# 一些需要注意的事项
# 将Python循环和条件逻辑转换为数组运算和布尔数组运算
# 尽量使用广播
# 避免复制数据, 尽量使用数组视图(即切片)
# 利用ufunc及各种方法

# 连续内存的重要性
# 有时候数据的内存布局可以对计算速度造成非常大影响, 在一定程度和CPU的高速缓存(cache)体系有关
# 运算过程中访问连续的内存块一般是最快的

arr_c = np.ones((1000, 1000), order='C')
arr_f = np.ones((1000, 1000),order='F')
print arr_c.flags
print
print arr_f.flags
print
print arr_f.flags.f_contiguous

# 理论上是arr_c会比arr_f快, 因为arr_c会比arr_f快, 是因为arr_c的内存连续
# 下面的代码请在ipython中运行
# %timeit arr_c.sum(1)
# %timeit arr_f.sum(1)

# 如果内存顺序不符合你的要求, 可以使用copy, 同时设置顺序
print arr_f.copy('C').flags

# 在构造数组的视图时, 结果不一定是连续
print arr_c[:50].flags.contiguous
print arr_c[:, :50].flags

2






