#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pandas.io.data as web
from pandas import Series, DataFrame

# 十分位和四分位分析
# 基于样本分位数的分析是金融分析师的重要工作
# 比如股票投资组合的性能可以根据各股的市盈率别划分入4分数(4个大小相等的块)
# 通过pandas.qcut和groupby可以轻松地实现分位数分析
data = web.get_data_yahoo('SPY', '2006-01-01', '2012-07-27')
print data

# 计算日收益率
px = data['Adj Close']
returns = px.pct_change()


# 编写用于将收益率变换为趋势信号(通过滞后移动形成)
def to_index(rets):
    index = (1 + rets).cumprod()
    first_loc = index.notnull().argmax()
    index[first_loc] = 1
    return index


def trend_signal(rets, lookback, lag):
    signal = pd.rolling_sum(rets, lookback, min_periods=lookback - 5)
    return signal.shift(lag)

# 创建和测试一种根据每周五动量信号进行交易的交易策略
signal = trend_signal(returns, 100, 3)
print signal
trade_friday = signal.resample('W-FRI').mean().resample('B').ffill()
trade_rets = trade_friday.shift(1) * returns

# 下面代码最好在ipython的pylab模式下面运行
# SPY动量策略收益指数
# to_index(trade_rets).plot()

# 将该策略的性能按不同大小的交易期波幅进行划分
# 年度标准差是计算波幅的一种简单办法
# 我们可以通过计算夏普比率来观察不同波动机制下的风险收益率
vol = pd.rolling_std(returns, 250, min_periods=200) * np.sqrt(250)


def sharpe(rets, ann=250):
    return rets.mean() / rets.std() * np.sqrt(ann)

print trade_rets[:1655].groupby([pd.qcut(vol, 4)]).agg(sharpe)



