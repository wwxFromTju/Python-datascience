#!/usr/bin/env pythoon
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 排列和随机采样
# 采用numpy.random.permutation函数可以对Series,DataFrame的列进行排列。
# 可以通过permutation来调节长度
df = DataFrame(np.arange(5 * 4).reshape(5, 4))
sampler = np.random.permutation(5)
print sampler
print df

# 通过take来重排列index
print df.take(sampler)

# 选取index中的一部分
print df.take(np.random.permutation(len(df))[:3])

# 使用randint产生随机整数
bag = np.array([5, 7, -1, 6, 4])
# 产生0到len(bag)范围内的10个值
sampler = np.random.randint(0, len(bag), size=10)
draws = bag.take(sampler)
print sampler
print bag
print draws