#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 嵌套dtype和多维字段
# 在定义结构化dtype时, 可以设置一个形状(可以是一个整数, 也可以是一个元组)
dtype = [('x', np.int64, 3), ('y', np.int32)]
arr = np.zeros(4, dtype=dtype)
print arr

# 各个记录的x字段所表示的是一个长度为3的数组
print arr[0]['x']
# 访问arr['x']可以得到一个二维数组
print arr['x']
# 所以我们可以用单个数组的内存块存放复杂的嵌套结构。
# 嵌套dtype
dtype = [('x', [('a', 'f8'), ('b', 'f4')]), ('y', np.int32)]
data = np.array([((1, 2), 5), ((3, 4), 6)], dtype=dtype)
print data
print data['x']
print data['y']
print data['x']['a']
