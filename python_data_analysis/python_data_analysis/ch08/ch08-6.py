#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

# 柱状图
fig = plt.figure()
fig, axes = plt.subplots(2, 1)
data = Series(np.random.rand(16), index=list('abcdefghijklmnop'))
# bar 竖状的柱状图
# barh 水平的柱状图
data.plot(kind='bar', ax=axes[0], color='k', alpha=0.7)
data.plot(kind='barh', ax=axes[1], color='k', alpha=0.7)

df = DataFrame(np.random.rand(6, 4),
               index=['one', 'two', 'three', 'four', 'five', 'six'],
               columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
print df
df.plot(kind='bar')
# 设置stacked=True可以生成堆积图
df.plot(kind='barh', stacked=True, alpha=0.5)

# 可以使用value_counts图形化显示Series各值的出现频率
data.value_counts().plot(kind='bar')

