#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# apply: 一般性的'拆分-应用-合并'
# apply 会将处理对象拆分成多个片段,然后对各片段调用传入函数,最后尝试将各片段组合到一起


# 默认选出最高的5个tip_pct值
def top(df, n=5, column='tip_pct'):
    return df.sort_index(by=column)[-n:]


def get_stats(group):
    return {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'mean': group.mean()}


tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']
# 选出最高的6个值
print top(tips, n=6)

# 对smoker分组,并调用top函数进行apply
# top是对每个分组进行调用的,所以在每个分组上分别选出前5个值, 并产生一个层次化索引
print tips.groupby('smoker').apply(top)

# 对传给apply的函数的参数,可以写在apply内部之后
print tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill')
result = tips.groupby('smoker')['tip_pct'].describe()
print result
print result.unstack('smoker')
# 等价于
f = lambda x: x.describe()
print tips.groupby('smoker')['tip_pct'].apply(f).unstack()

# 禁止分组键, 分组键会和原始对象的索引共同构成结果对象中的层次化索引。可以通过group_keys来设置
print tips.groupby('smoker').apply(top)
print tips.groupby('smoker', group_keys=False).apply(top)


# 分位数和桶分析
# 通过指定面元或样本分位数可以将数据拆分成多块,和groupby结合可以实现桶(bucker)或分位数(quantile)分析
frame = DataFrame({'data1': np.random.randn(10000),
                   'data2': np.random.randn(10000)})
# 得到区间大小相同
factor = pd.cut(frame.data1, 4)
print factor[:10]
grouped = frame.data2.groupby(factor)
print grouped.apply(get_stats).unstack()
# 得到样本数相同
grouping = pd.qcut(frame.data1, 10, labels=False)
grouped = frame.data2.groupby(grouping)
print grouped.apply(get_stats).unstack()