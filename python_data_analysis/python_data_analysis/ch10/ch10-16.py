#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pytz
from pandas import Series, DataFrame

# 重采样及频率转换
# 重采样(resampling): 将时间序列从一个频率转换到另一个频率
# 降采样(downsampling): 将高频数据聚合到低频率
# 升采样(upsampling): 将低频数据转换到高频率

# resample
rng = pd.date_range('1/1/2000', periods=100, freq='D')
ts = Series(np.random.randn(len(rng)), index=rng)
print ts

# 下面的Future以后可能会被放弃
# print ts.resample('M', how='mean')
# 下面是未来的Future
print ts.resample('M').mean()
# print ts.resample('M', how='mean', kind='period')
print ts.resample('M', kind='period').mean()

# resample方法的参数
# freq 表示重采样频率的字符串/DateOffset, 如: 'M', '5min' 或 Second(15)
# how  聚合函数/数据函数 mean/ohlc/np.max等, 默认为:mean。其他常见有:first/last/median/ohlc/max/min
# axis 重采样的轴, 默认为axis=0
# fill_method 升采样时候如何插值, 比如ffill或bfill, 默认不插值
# closed 在降采样中, 各时间段的哪一端是闭合(即包含), right或者left 默认为right
# label 在降采样中, 如何设置聚合值的标签, right或left(面元的右边界或左边界) (9:30 9:35) -》 右边界:9:35
# loffset  面元标签的时间校正值, 比如-1s/Second(-1) 用于将聚合标签调早1秒
# limit  在前向或后向填充时, 允许填充的最大时期数
# kind  聚合到时期'period'或时间戳'timestamp', 默认聚合到时间序列的索引类型
# convention  当重采样时期, 将低频率转换到高频率所采用的约定(start或end) 默认为end


