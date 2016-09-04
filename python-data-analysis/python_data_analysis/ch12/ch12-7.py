#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 花式索引的等价函数: take和put
arr = np.arange(10) * 100
inds = [7, 1, 2, 6]
print arr[inds]

# ndarray有两个方法专门用于获取和设置单个轴向上的选区
print arr.take(inds)

# 将对应位置的数替换掉
arr.put(inds, 42)
print arr

# 使用axis参数来指定对应的轴
# put不接受axis参数, 只能在数组的扁平化版本上(一维, C顺序)上进行索引, 如果需要在其他轴向的索引设置元素时, 最好使用花式索引
inds = [2, 0, 2, 1]
arr = np.random.randn(2, 4)
print arr
print arr.take(inds, axis=1)

# 通常take和put函数的性能比花式索引好得多(实际上我运行的时候, 花式效果更好)
arr = np.random.randn(1000, 50)
inds = np.random.permutation(1000)[:500]
# 下面代码请在ipython中运行
# 花式索引
# %timeit arr[inds]
# take函数
# %timeit arr.take(inds, axis=0)



