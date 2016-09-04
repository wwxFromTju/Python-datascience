#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# 自定义ufunc
# numpy.frompyfunc接受一个python函数以及两个分别表示输入输出参数数量的整数
def add_elements(x, y):
    return x + y

add_them = np.frompyfunc(add_elements, 2, 1)
print add_them(np.arange(8), np.arange(8))

# 用frompyfunc创建的函数总是返回Python对象数组
# 可以使用numpy.vectorize
add_them = np.vectorize(add_elements, otypes=[np.float64])
print add_them(np.arange(8), np.arange(8))

# 这两个函数提供了一种创建ufunc型函数的手段, 但是慢
# 因为它们在计算每个元素的时候都要执行一次Python函数调用
arr = np.random.randn(10000)
# 下面的代码请在ipython中运行
# 使用ufunc
# %timeit add_them(arr, arr)
# 使用Numpy自带的基于C的ufunc
# %timeit np.add(arr, arr)



