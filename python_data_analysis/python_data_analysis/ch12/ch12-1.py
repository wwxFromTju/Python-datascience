#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# Numpy高级应用
# ndarray对象的内部机理
# Numpy的ndarray提供了一种将同质数据快(可以连续或非连续存储)解释为多维数组对象的方式
# 数据类型(dtype)决定了数据的解释方式, 比如浮点数, 整数, 布尔值等

# ndarray:所有数据对象都是数据快的一个跨度视图(strided view)
# 数组视图arr[::2, ::-1]不复制任何数据: ndarray不只是一块内存和一个dtype,还有相应的跨度信息, 是数组能以
# 各种步幅(step size)在内存中移动

# ndarray内部由以下内容组成
# 一个指向数组(一个系统内存块)的指针
# 数据类型和dtype
# 一个表示数组形状(shape)的元组, 比如10x5的数组, 形状为(10, 5)
# 一个跨度元组(stride), 其中的整数: 为了前进到下一份维度需要'跨过'的字节数。 比如一个3x4x5的float64(8字节)数据, 跨度为(160, 40, 8)
print np.ones((3, 4, 5), dtype=np.float64).strides

# 跨度信息: 构建非复制数组视图, 跨度可以是负数, 可以使数组在内存中移动, 类似切片中的[::-1]
