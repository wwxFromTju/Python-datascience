#!/usr/bin//env python
# encoding=utf-8

# 数据聚集和分组运算

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

df = DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                'key2': ['one', 'two', 'one', 'two', 'one'],
                'data1': np.random.randn(5),
                'data2': np.random.randn(5)})

print df

# 按照key1进行分组
grouped = df['data1'].groupby(df['key1'])
print grouped

# 计算data1列的平均值
print grouped.mean()

# 一次传入多个数组
means = df['data1'].groupby([df['key1'], df['key2']]).mean()
print means
print means.unstack()

# 分组键可以是任意长度适合的数组
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
yesrs = np.array([2005, 2005, 2006, 2005, 2006])
print df['data1'].groupby([states, yesrs]).mean()

# 将列名用作分组键
# 注意没有key2,因为key2不是数值数据,所以在结果列中被排除了
print df.groupby('key1').mean()
# 注意有key2
print df.groupby(['key1', 'key2']).mean()

# 返回对应分组的大小
print df.groupby(['key1', 'key2']).size()
