#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 检测和过滤异常值
# 异常值 outlier

np.random.seed(12345)
data = DataFrame(np.random.randn(1000, 4))
# describe统计相应的参数
print data.describe()

# 统计第三列中绝对值超过3的值
col = data[3]
print col[np.abs(col) > 3]

# 选出全部含有绝对值超过3的行
print data[(np.abs(data) > 3).any(1)]

# 可以通过赋值来限制值的范围
# 将绝对值超过3的转换为绝对值为3
data[(np.abs(data) > 3)] = np.sign(data) * 3

print data.describe()