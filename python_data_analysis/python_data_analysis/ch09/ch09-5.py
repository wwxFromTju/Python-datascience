#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 分组级运算合转换


# 距平化函数 demeaning function
def demean(arr):
    return arr - arr.mean()


df = DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                'key2': ['one', 'two', 'one', 'two', 'one'],
                'data1': np.random.randn(5),
                'data2': np.random.randn(5)})
print df

k1_means =df.groupby('key1').mean().add_prefix('mean_')
print k1_means
# 添加用于存放各索引分组平均值的列, 一个办法是先聚集再合并
# 可以看成利用np.mean函数对两个数据列进行转换
print pd.merge(df, k1_means, left_on='key1', right_index=True)


# transform相对严格,传入函数只能产生2种结果: 一个是可以广播的标量值(np.nan)或者产生一个相同大小的结果数组
people = DataFrame(np.random.randn(5, 5),
                   columns=['a', 'b', 'c', 'd', 'e'],
                   index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
key = ['one', 'two', 'one', 'two', 'one']
print people
print people.groupby(key).mean()
# transform 将一个函数应用到各个分组,然后将结果放在对应分组的数据位置上
# 如果结果是标量,则广播。
print people.groupby(key).transform(np.mean)

# 各数值减去对应分组的平均值
demeaned = people.groupby(key).transform(demean)
print demeaned
# 各值减掉对应分组的平均值, 则均值为0
print demeaned.groupby(key).mean()
