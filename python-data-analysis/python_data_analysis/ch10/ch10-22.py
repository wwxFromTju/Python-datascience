#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 移动窗口函数
# 在移动窗口上(可以带有指数衰减权数)上计算的各种统计函数,称为移动窗口函数(moving window function)

close_px_all = pd.read_csv('stock_px.csv', parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px = close_px.resample('B').ffill()

# 下面代码请在ipython中运行
close_px.AAPL.plot()
# 计算平均数
pd.rolling_mean(close_px.AAPL, 250).plot()

# 一般情况下, rolling需要指定数量的非NA观测值
# apple公司250日每日回报标准差
appl_std250 = pd.rolling_std(close_px.AAPL, 250, min_periods=10)
print appl_std250[5:12]
appl_std250.plot()

# 计算扩展窗口平均(expanding window mean)
# 可以将扩展窗口看成一个特殊的窗口, 长度和时间序列一阿姨难过,但只需一期(或多期)即可计算一个值
# 通过rolling_mean扩展平均
expanding_mean = lambda x: pd.rolling_mean(x, len(x), min_periods=1)

# 各股票60日均线
# 下面代码请在ipython中运行
pd.rolling_mean(close_px, 60).plot()

# pandas相应的移动窗口和指数加权函数
# rolling_count 返回各窗口非NA观测值的数量
# rolling_sum   移动窗口的和
# rolling_mean  移动窗口的平均值
# rolling_median    移动窗口的中位数
# rolling_var/rolling_std   移动窗口的方差和标准差。 分母为n-1
# rolling_skew/rolling_kurt     移动窗口的偏度(三阶矩)和峰度(四阶矩)
# rolling_min/rolling_max   移动窗口的最小值和最大值
# rolling_quantile  移动窗口指定百分位数/样本分位数位置的值
# rolling_corr/rolling_cov  移动窗口的相关系数和协方差
# rolling_apply 移动窗口应用普通数组函数
# ewma  指数加权移动平均
# ewmvar/ewmstd 指数加权移动方差/标准差
# ewmcorr/ewmcov    指数加权移动相关系数和协方差

# 相关操作也可以使用bottleneck库





