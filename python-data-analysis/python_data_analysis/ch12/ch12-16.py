#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 其他排序算法
# 稳定的(stable)排序算法会保持等价元素的相对位置
values = np.array(['2:first', '2:second', '1:first', '1:second', '1:third'])
key = np.array([2, 2, 1, 1, 1])
indexer = key.argsort(kind='mergesort')
# 注意等价元素的相对顺序
print indexer
print values.take(indexer)

# mergesort是提供的惟一的稳定排序
# kind      速度      稳定性     工作空间        最坏情况
# quicksort   1        否        0             O(n2)
# mergesort   2        是        n/2           O(nlogn)
# heapsort    3        否        0             O(nlogn)
1