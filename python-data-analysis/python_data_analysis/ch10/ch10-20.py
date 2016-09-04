#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pytz
from pandas import Series, DataFrame

# 通过时期进行重采样

frame = DataFrame(np.random.randn(24, 4),
                  index=pd.period_range('1-2000', '12-2001', freq='M'),
                  columns=['Colorado', 'Texas', 'New York', 'Ohio'])
print frame[:5]

# 降采样
annual_frame = frame.resample('A-DEC').mean()
print annual_frame

# 升采样
# 设置对应区间的左侧(右侧)的值
# convention 默认为start, 可以设置为end
print annual_frame.resample('Q-DEC').ffill()
print annual_frame.resample('Q-DEC', convention='end').ffill()
print annual_frame.resample('Q-DEC', convention='start').ffill()

# 由于是时间区间, 不满足下面的频率异常, 主要是影响按季, 年, 周计算的频率, 例如Q-MAR定义的时间区间,只能生采样为A-MAR, A-JUN, A-SEP, A-DEC
# 在降采样中, 目标频率必须是源频率的子时期(subperiod)
# 在升采样中, 目标频率必须是源频率的超时期(superperiod)
print annual_frame.resample('Q-MAR').ffill()


