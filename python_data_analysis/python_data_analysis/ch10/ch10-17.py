#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import pytz
from pandas import Series, DataFrame

# 降采样
# 将数据聚合到规整的低频率

# '1分钟'数据
# 下面是12分钟
rng = pd.date_range('1/1/2000', periods=12, freq='T')
ts = Series(np.arange(12), index=rng)
print ts

# 聚合到5分钟中
print ts.resample()





