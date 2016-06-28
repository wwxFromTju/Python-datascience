#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 间接排序: argsort和lexsort
# 通过给定一个或多个键, 可以得到以一个由整数组成的索引数组, 索引值是数据在新顺序下的位置

values = np.array([5, 0, 1, 3, 2])
indexer = values.argsort()
# 将索引代表的值从小到大排序
print indexer
print values[indexer]

# 根据数组的第一行对其进行排序
arr = np.random.randn(3, 5)
arr[0] = values
print arr
print arr[:, arr[0].argsort()]

# lexsort可以一次对多个键数组执行间接排序(字典序)
first_name = np.array(['Bob', 'Jane', 'Steve', 'Bill', 'Barbara'])
last_name = np.array(['Jones', 'Arnold', 'Arnold', 'Jones', 'Walters'])
# 注意是从参数顺序从后往前排序1
sorter = np.lexsort((first_name, last_name))
print zip(last_name[sorter], first_name[sorter])

