#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 数据聚合

def peak_to_peak(arr):
    return arr.max() - arr.min()


df = DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                'key2': ['one', 'two', 'one', 'two', 'one'],
                'data1': np.random.randn(5),
                'data2': np.random.randn(5)})
print df

# quantile计算Series, DataFrame的样本分位数,会采用线性插值
grouped = df.groupby('key1')
print grouped['data1'].quantile(0.9)

# GroupBy会高效对Series进行切片, 然后对各切片piece.quantile(0.9),然后再组装起来

# 使用自己的聚合函数,传给aggregate/agg
print grouped.agg(peak_to_peak)

# 经过优化的GroupBy的方法
# count 分组中的非NA值的数量
# sum 非NA值的和
# mean 非NA值的平均值
# median 非NA值的算术中位数
# std var 无偏(分母为N-1)标准差/方差
# min max 非NA值的最小值/最大值
# prod 非NA值的积
# first/last 非NA值的第一个/最后一个
