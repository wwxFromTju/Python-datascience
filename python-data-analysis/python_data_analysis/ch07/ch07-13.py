#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 计算指标/哑变量

# 分类变量categorical variable -》 哑变量矩阵 dummy matrix / 指标矩阵 indicator matrix
# 如果一列中有k个不同的值,派生除k列矩阵或DataFrame(0/1矩阵)
df = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                'data1': range(6)})
print df
print pd.get_dummies(df['key'])

# 给DataFrame的列加上前缀,方便合并
dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(dummies)
print df_with_dummy

# 某一行同属于多个分类
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movies.dat', sep='::', header=None, names=mnames)
print movies[:10]
# 数据规整
genre_iter = (set(x.split('|')) for x in movies.genres)
# 抽取出不同的值
genres = sorted(set.union(* genre_iter))
print genre_iter
print genres

# 构建全0的DataFrame
dummies = DataFrame(np.zeros((len(movies), len(genres))), columns=genres)
for i, gen in enumerate(movies.genres):
    dummies.ix[i, gen.split('|')] = 1
movies_windic = movies.join(dummies.add_prefix('Genre_'))
print movies_windic.ix[0]

# 结合get_dummies和诸如cut之类离散化函数
values = np.random.rand(10)
print values
bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
print pd.get_dummies(pd.cut(values, bins))
