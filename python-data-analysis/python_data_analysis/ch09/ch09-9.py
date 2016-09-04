#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import statsmodels.api as sm
from pandas import Series, DataFrame

#  分组加权平均数和相关系数

df = DataFrame({'category': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
                'data': np.random.randn(8),
                'weights': np.random.rand(8)})
print df
grouped = df.groupby('category')

# 加权平均数
get_wavg = lambda g: np.average(g['data'], weights=g['weights'])

print grouped.apply(get_wavg)

close_px = pd.read_csv('stock_px.csv', parse_dates=True, index_col=0)
print close_px
print close_px[-4:]


# 计算日收益率
rets =close_px.pct_change().dropna()
spx_corr = lambda x: x.corrwith(x['SPX'])
by_year = rets.groupby(lambda x: x.year)
print by_year.apply(spx_corr)

# 微软和苹果的年度相关系数
print by_year.apply(lambda g: g['AAPL'].corr(g['MSFT']))


# 线性回归
def regress(data, yvar, xvars):
    Y = data[yvar]
    X = data[xvars]
    X['intercept'] = 1.
    result = sm.OLS(Y, X).fit()
    return result.params

print by_year.apply(regress, 'AAPL', ['SPX'])

