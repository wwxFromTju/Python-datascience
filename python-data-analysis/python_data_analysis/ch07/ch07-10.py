#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 离散化和面元划分

# 为了便于分析, 连续数据通常被离散化或拆分为'面元'(bin)
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

# 指定分割的点 [18 25] [26 35] [36 60]...
bins = [18, 25, 35, 60, 100]

# 分割
# cut返回的是Categorical对象, 含有表示不同分类名称的levels, 对年龄数据进行标号的labels
cats = pd.cut(ages, bins)
print cats

# 默认左开右闭, 可以使用right来控制
print pd.cut(ages, [18, 26, 36, 61, 100], right=False)

# 可以自己设置面元名称
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
print pd.cut(ages, bins, labels=group_names)

# 可以直接向cut传入面元的数量, 那么会自动根据面元的数量去计算对应区间
data = np.random.rand(20)
print pd.cut(data, 4, precision=2)

# qcut根据分位数对数据进行面元划分,每个划分中数量相等
data = np.random.randn(1000)
cats = pd.qcut(data, 4)
print cats
print pd.value_counts(cats)

# 可以自定义分位数
cats = pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.])
print cats
print pd.value_counts(cats)