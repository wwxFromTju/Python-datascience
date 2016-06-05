#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 替换值
# 类似于fillna, 对值进行替换
data = Series([1., -999., 2., -999., -1000., 3.])
print data
# 我们可以约定-999是缺失值,但是NaN没有二义性
print data.replace(-999, np.nan)
# 一次替换多个
print data.replace([-999, -1000], np.nan)
# 不同值替换成不同的值,注意位置对应
print data.replace([-999, -1000], [np.nan, 0])
# 字典: key是要被替换的, value是替换的
print data.replace({-999: np.nan, -1000: 0})