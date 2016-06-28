#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# Numpy的matrix类
# 相比MATLAB/GAUSS等, Numpy的线性代数语法往往语法比较繁琐
# 因为矩阵操作常常要用到numpy.dot, Numpy的索引语义也不同
# 比如X[1, :] X[:, 1] 在Numpy中会产生一维数组, 但是MATLAB中却是二维数组, 所以移植还是有问题
X = np.array([[ 8.82768214,  3.82222409, -1.14276475,  2.04411587],
               [ 3.82222409,  6.75272284,  0.83909108,  2.08293758],
               [-1.14276475,  0.83909108,  5.01690521,  0.79573241],
               [ 2.04411587,  2.08293758,  0.79573241,  6.24095859]])

# 一维的
print X[:, 0]

# 切片可以产生二维
y = X[:, :1]
print y

# 计算向量乘法
print np.dot(y.T, np.dot(X, y))

# Numpy提供了matrix类, 来简化运用
Xm = np.matrix(X)
ym = Xm[:, 0]
print Xm
print ym
print ym.T * Xm * ym

# matrix还有一个特殊的属性I, 返回矩阵的逆:
print Xm.I * X

# 不建议用np.matrix替代正规的ndarray, 因为应用面较窄
# 如果有大量线性代数运算函数, 可以先转为matrix类型, 然后用np.asarray(不复制)转换为ndarray
1
