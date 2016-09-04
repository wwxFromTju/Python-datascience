#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 通过广播设置数组的值
arr = np.zeros((4, 3))
arr[:] = 5
print arr

col = np.array([1.28, -0.42, 0.44, 1.6])
arr[:] = col[:, np.newaxis]
print arr

arr[:2] = [[-1.37], [0.509]]
print arr
