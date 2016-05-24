#!/usr/bin/env python
# encoding=utf-8

import numpy as np
from numpy.linalg import inv, qr

# 文件保存,如果文件名没有后缀的话,那么自动加上npy
arr = np.arange(10)
np.save("./the_array", arr)

# 文件读取
# print np.load('the_array.npy')

# 将多个数组保存在一个压缩文件中,如果没有后缀的话,那么会默认加上npz
np.savez('the_array', a=arr, b=arr)
load_zip = np.load('the_array.npz')
# print load_zip['b']

# 载入文本文件,并指定分割符,保存的时候没有默认后缀
arr_text = np.loadtxt('text.txt', delimiter=',')
np.savetxt('text2.txt', arr_text)
# print arr_text

# 线性代数
x = np.array([[1., 2., 3.],
             [4., 5., 6.]])
y = np.array([[6., 23.],
             [-1., 7.],
             [8., 9.]])
# 矩阵乘法
# print x.dot(y)
# print np.dot(x, y) == x.dot(y)

# numpy.linalg中的inv, qr
X = np.random.randn(5, 5)
mat = X.T.dot(X)
# print mat
# print inv(mat)
# print mat.dot(inv(mat))
q, r = qr(mat)
# print q
# print r
# 常用numpy.linalg
# diag() 以一维数组的形式返回方针的对角线元素,或者将一个一维数组补成方阵(除了对角线外其他补0)
# dot() 矩阵乘法
# trace() 计算对角线的和
# det() 计算行列式
# eig() 计算本征值和本征向量
# inv() 计算方阵的逆
# pinv() 计算方阵的Moore-Penrose伪逆
# qr() 计算QR分解
# svd() 计算svd分解即奇异值分解
# solve 解线性方程组Ax=b, A为方阵
# lstsq 计算Ax=b的最小二乘解

# 随机数生成
# normal 标准正态分布
samples = np.random.normal(size=(4, 4))
# print samples
# np.random 比 python的random更快

# numpy.random函数
# seed 确定种子
# permutation 返回一个序列的随机排列或者返回一个随机排列的范围
# shuffle 对于一个序列就地随机排列
# rand 产生均匀分布的样本值
# randint 从给定上下限的范围内随机选取整数
# randn 产生正态分布
# binomial 产生二项分布的样本值
# normal 产生高斯(正态)分布
# beta 产生beta分布
# chisquare 产生卡方分布
# gamma 产生Gamma分布
# uniform 产生[0, 1)的样本值

