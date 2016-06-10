#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

def peak_to_peak(arr):
    return arr.max() - arr.min()


tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']
print tips[:6]

# 对Series/DataFrame列的聚合运算其实就是使用aggregate(自定义)或者使用mean/std之类的

# 对不同的列使用不同的聚合函数/一次使用多个函数
grouped = tips.groupby(['sex', 'smoker'])
grouped_pct = grouped['tip_pct']
print grouped_pct.agg('mean')

# 如果传入一组函数或者函数名,则得到的DataFrame的列会以相应的函数命名
print grouped_pct.agg(['mean', 'std', peak_to_peak])
# 传入一个二元组(name, func) 第一个为指定的名字, 第二个为对应的函数
print grouped_pct.agg([('foo', 'mean'), ('bar', np.std)])

# 对DataFrame可以定义一组应用全部列的函数/不同列不同函数
functions = ['count', 'mean', 'max']
# 会产生层次化的列
result = grouped['tip_pct', 'total_bill'].agg(functions)
print result
print result['tip_pct']

# 可以传入自定义名称的元组列表
ftuples = [('Durchschnitt', 'mean'), ('Abweichung', np.var)]
print grouped['tip_pct', 'total_bill'].agg(ftuples)

# 对不同的列应用不同的函数
print grouped.agg({'tip': np.max, 'size': 'sum'})
print grouped.agg({'tip_pct': ['min', 'max', 'mean', 'std'],
                   'size': 'sum'})

# 以无索引返回聚合数据
print tips.groupby(['sex', 'smoker'], as_index=False).mean()
