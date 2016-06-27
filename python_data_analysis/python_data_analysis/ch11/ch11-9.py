#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pandas.io.data as web
from pandas import Series, DataFrame

# 信号前沿分析
# 简化的截面动量投资组合, 通过模型参数化网格

# 将金融和技术领域的几只股票做成一个投资组合, 加载它们的历史价格数据
names = ['AAPL', 'GOOG', 'MSFT', 'DELL', 'GS', 'MS', 'BAC', 'C']


def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']

px = DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})
px = px.asfreq('B').fillna(method='pad')
rets = px.pct_change()
# 下面的代码请在ipython的pylab模式下面运行
# ((1 + rets).cumprod() - 1).plot()


# 对于投资组合的构建, 计算特定回顾的动量, 按降序排列并标准化
def calc_mom(price, lookback, lag):
    foo = price.shift(lag)
    foo2 = foo.pct_change(lookback)
    mom_ret = price.shift(lag).pct_change(lookback)
    ranks = mom_ret.rank(axis=1, ascending=False)
    demeaned = ranks - ranks.mean(axis=1)
    temp = demeaned / demeaned.std(axis=1)
    return demeaned / demeaned.std(axis=1)

# 对策略进行事后检验的函数
# 通过指定回顾期和持有期(买卖之间的日期)计算投资组合整体的夏普比率
compound = lambda x: (1 + x).prod() -1
daily_sr = lambda x: x.mean() / x.std()


def start_sr(prices, lb, hold):
    # 计算投资组合权重
    freq = '%dB' % hold
    port = calc_mom(prices, lb, lag=1)
    daily_rets = prices.pct_change()
    print 'PORT',port
    print 'DAILY-RETS', daily_rets
    print port
    # 计算投资组合收益
    port = port.shift(1).resample(freq).first()
    returns = daily_rets.resample(freq).apply(compound)
    port_rets = (port * returns).sum(axis=1)

    return daily_sr(port_rets) * np.sqrt(252 / hold)

print start_sr(px, 70, 30)

#