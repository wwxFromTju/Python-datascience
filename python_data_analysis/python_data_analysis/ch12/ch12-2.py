#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# Numpy数据类型体系

# 判断dtype是否属于某个大类
# dtype有相应的超类如: np.integer np.floating等
# 可以使用np.issubdtype函数结合
ints = np.ones(10, dtype=np.uint16)
floats = np.ones(10, dtype=np.float32)

# 可以判断ints是否从属于integer
print np.issubdtype(ints.dtype, np.integer)
# 判断floats是否从属于float
print np.issubdtype(floats.dtype, np.float)

# 调用dtype的mro方法可以察看其他的所有父类
print np.float64.mro()
