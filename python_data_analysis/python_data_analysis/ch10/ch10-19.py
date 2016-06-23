#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pytz
from pandas import Series, DataFrame

# 升采样和插值
# 将数据从低频率转换到高频率
frame = DataFrame(np.random.randn(2, 4),
                  index=pd.date_range('1/1/2000', periods=2, freq='W-WED'),
                  columns=['Colorado', 'Texas', 'New York', 'Ohio'])
print frame[:5]

# 将重采样到日频率, 默认引入缺失值
df_daily = frame.resample('D')
print df_daily

# 使用resampling的填充和插值方式和fillna和reindex一样
# 下面的Future以后可能被抛弃
# print frame.resample('D', fill_method='ffill')
# 现在下面使用
print frame.resample('D').ffill()

# 可以填充指定的时期数(目的是限制前面的观测值的持续使用距离)
# 下面future未来可能会被废弃
# print frame.resample('D', fill_method='ffill', limit=2)
print frame.resample('D').ffill(limit=2)

# 新的日期索引完全没有跟旧的相交
# print frame.resample('W-THU', fill_method='ffill')
print frame.resample('W-THU').ffill()
