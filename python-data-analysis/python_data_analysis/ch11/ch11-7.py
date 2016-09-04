#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import string
import random
from pandas import Series, DataFrame

# 分组因子暴露
# 因子分析(factor analysis)是投资组合定量管理中的一种技术
# 投资组合的持有量和性能(收益和损失)可以被分解为一个或多个表示投资组合权重的因子
# 比如某只股票的价格和某个基准的协动性被称为贝塔风险系数(beta, 一种常见的风险因子)

random.seed(0)


def rands(n):
    choices = string.ascii_uppercase
    return ''.join([random.choice(choices) for _ in xrange(n)])

N = 1000
tickers = np.array([rands(5) for _ in xrange(N)])

# 下面是一个投资组合, 由三个随机生成的因子(通常称为因子载荷)和一些权重构成
fac1, fac2, fac3 = np.random.rand(3, 1000)

ticker_subset = tickers.take(np.random.permutation(N)[:1000])

# 因子加权和以及噪声
port = Series(0.7 * fac1 - 1.2 * fac2 + 0.3 * fac3 + np.random.rand(1000),
              index=ticker_subset)
factors = DataFrame({'f1': fac1, 'f2': fac2, 'f3': fac3},
                    index=ticker_subset)

print factors.corrwith(port)

# 计算因子暴露的标准方式是最小二乘回归
# 使用pandas.ols来计算整个投资组合的暴露
print pd.ols(y=port, x=factors).beta


# 通过groupby计算各行业的暴露量
def beta_exposure(chunk, factors=None):
    return pd.ols(y=chunk, x=factors).beta

ind_names = np.array(['FINANCIAL', 'TECH'])
sampler = np.random.randint(0, len(ind_names), N)
industries = Series(ind_names[sampler], index=tickers,
                    name='industry')

by_ind = port.groupby(industries)
exposures = by_ind.apply(beta_exposure, factors=factors)
print exposures.unstack()
