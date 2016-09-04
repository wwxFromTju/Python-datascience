#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame


# 指数加权函数
# 定义一个衰减因子(decay factor)常量, 近期的观测值拥有更大的权数
# 定义衰减因子的方式有很多, 比较流行的是时间间隔(span), 可以使结果兼容于窗口大小等于时间间隔的简单移动窗口(simple moving window)函数
# 指数加权可以更好表示出变化(相对等权统计)

close_px_all = pd.read_csv('stock_px.csv', parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px = close_px.resample('B').ffill()

# 对比apple公司股价的60日移动平均和span=60的指数加权移动平均
# 下面的代码在ipython中运行
fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True, figsize=(12, 7))

aapl_px = close_px.AAPL['2005': '2009']
ma60 = pd.rolling_mean(aapl_px, 60, min_periods=50)
ewma60 = pd.ewma(aapl_px, span=60)

aapl_px.plot(style='k-', ax=axes[0])
ma60.plot(style='k--', ax=axes[0])

aapl_px.plot(style='k-', ax=axes[1])
ewma60.plot(style='k--', ax=axes[1])

axes[0].set_title('Simple MA')
axes[1].set_title('Exponentially-weighted MA')



