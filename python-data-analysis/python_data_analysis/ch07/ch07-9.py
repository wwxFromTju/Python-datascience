#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 重命名轴索引

data = DataFrame(np.arange(12).reshape((3, 4)),
                 index=['Ohio', 'Colorado', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
print data
# 通过index访问轴,然后通过map来进行操作
print data.index.map(str.upper)

# 可以修改index和columns索引
print data.rename(index=str.title, columns=str.upper)
# rename的不同参数可以传入字典来进行替换
print data.rename(index={'Ohio': 'INDIANA'},
                  columns={'three': 'peekaboo'})