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


# 对分组进行迭代
for name, group in df.groupby('key1'):
    print name
    print group

# 多重键 第一个元素是由键值组成的元组
for (k1, k2), group in df.groupby(['key1', 'key2']):
    print k1, k2
    print group

# 转换成字典
pieces = dict(list(df.groupby('key1')))
print pieces['b']

# groupby 默认是在axis=0上进行分组,可以设置在另外的轴上面进行分组
print df.dtypes
# 通过dtype对列进行分组
grouped = df.groupby(df.dtypes, axis=1)
print dict(list(grouped))


