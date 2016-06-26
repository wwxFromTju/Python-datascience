#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 分组变换和分析
# 对数据集的分组应用自定义的变换函数

# 假想一组股票投资组合
# 首先随机生成1000个股票代码
import random; random.seed(0)
import string


def rands(n):
    choices = string.ascii_uppercase
    return ''.join([random.choice(choices) for _ in xrange(n)])

N = 1000
tickers = np.array([rands(5) for _ in xrange(N)])

# 创建一个含有3列的DataFrame来承载这些假想数据, 只选择部分股票组成投资组合
M = 500
df = DataFrame({'Momentum': np.random.randn(M) / 200 + 0.03,
                'Value': np.random.randn(M) / 200 + 0.08,
                'ShortInterest': np.random.randn(M) / 200 - 0.02},
               index=tickers[:M])

# 为股票随机创建一个行业分类
# 只选择2个行业, 并将映射关系保存在Series中
ind_names = np.array(['FINANCIAL', 'TECH'])
sampler = np.random.randint(0, len(ind_names), N)
industries = Series(ind_names[sampler], index=tickers,
                    name='industry')

# 根据行业分类进行分组并执行分组聚合和变换
by_industry = df.groupby(industries)
print by_industry.mean()
print by_industry.describe()


# 编写自定义的变换函数
# 行业内标准化处理
def zscore(group):
    return (group - group.mean()) / group.std()


# 处理之后, 各行业的平均值为0, 标准差为1
df_stand = by_industry.apply(zscore)
print df_stand.groupby(industries).agg(['mean', 'std'])

# 内置变换函数
# 比如rank来处理行业内降序排名
ind_rank = by_industry.rank(ascending=False)
print ind_rank.groupby(industries).agg(['min', 'max'])

# 在股票投资组合的定量分析中, 排名和标准化是一种很常见的变换运算组合
# 使用rank和zscore链接组合在一起即可
print by_industry.apply(lambda x: zscore(x.rank()))



