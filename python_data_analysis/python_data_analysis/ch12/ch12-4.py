#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# C和Fortran的顺序
# Numpy可以灵活地控制数据在内存中的布局
# 默认为按行优先顺序创建。 另外一种是列优先
# 行优先: C顺序
# 列优先: Fortran顺序
# 可以设置order参数 'C'-》C顺序 'F'-》Fortran顺序, 还有一些不常用的选项
arr = np.arange(12).reshape((3, 4))
print arr
print arr.ravel()
# 注意由于在内存中存放的位置, 所以顺序是按列优先排列
print arr.ravel('F')

# C/Fortran顺序的关键区别就是维度的行进行
# C/行优先顺序: 先经过更高的维度(例如, 轴1会先于轴0被处理)
# Fortran/列优先顺序: 后经过更高的维度(例如, 轴0会先于轴1被处理)



