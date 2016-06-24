#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 频率不同的时间序列的运算
# 经济学时间序列通常是年, 季, 月, 日计算或者其他更特殊的频率, 设置不规律的
# 比如对于盈利预测调整随时都可能会发生
# 主要采用频率转换resample到固定频率
# reindex使数据符合一个新索引

ts1 = Series(np.random.randn(3), index=pd.date_range('2012-6-13', periods=3, freq='W-WED'))
print ts1

# 重采样到工作日
# 注意产生的NaN值
print ts1.resample('B').mean()
# 使用fill来填充前面的空白, 通常在低频率数据这么做
print ts1.resample('B').mean().ffill()

# 实际中将较低频率的数据升采样到较高的规整频率
# 但是对于更一般的不规整时间序列有局限性
dates = pd.DatetimeIndex(['2012-6-12', '2012-6-17', '2012-6-18',
                          '2012-6-21', '2012-6-22', '2012-6-29'])
ts2 = Series(np.random.randn(6), index=dates)
print ts2

# 将ts1中最当前的值向前填充加到ts2上, 即维持ts2的索引
# 先使用ts2的索引来填充ts1的值
print ts1.reindex(ts2.index, method='ffill')
# 然后在加上去
print ts2 + ts1.reindex(ts2.index, method='ffill')


# 使用Period表示时间区间
gdp = Series([1.78, 1.94, 2.08, 2.01, 2.15, 2.31, 2.46],
             index=pd.period_range('1984Q2', periods=7, freq='Q-SEP'))

infl = Series([0.025, 0.045, 0.037, 0.04],
              index=pd.period_range('1982', periods=4, freq='A-DEC'))

print gdp
print infl

# 和Timestamp的时间序列不同Q-SEP得到该频率下的正确时间
infl_q = infl.asfreq('Q-SEP', how='end')
print infl_q

# 重索引
print infl_q.reindex(gdp.index, method='ffill')


