#!/usr/bin/env python
# encoding=utf-8

import numpy as np

data = np.array([[0.1, 0.2, 0.3],
                 [0.4, 0.5, 0.6]])

print data
print data * 10
print data + data
print data.shape
print data.dtype

# 将数组转换为数组array
data1 = [6, 7.5, 8, 2, 1]
arr1 = np.array(data1)
print arr1

# 将list转换为数组array
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print arr2
print arr2.ndim
print arr2.shape

# 如果数组中有小数的话,那么dtype为float64
# 如果数组中没有小数的话,那么dtype为int64
print arr1.dtype
print arr2.dtype

# 创建为0的数组
# 创建一个1行10列的0数组
print np.zeros(10)
# 创建一个和输入多维数组一样的数组,但是每个元素都是0
temp = np.array(data2)
print np.zeros_like(temp)

# 创建一个3行6列的0数组
print np.zeros((3, 6))

# 创建2个2行3列的数组, 对里面的数字没有指定
# 第一个参数为 n行, 第二个参数为 m列, 第三个参数为 x个数组
print np.empty((2, 3, 2))

# 创建一个从0开始的有序的数组, n为数组大小
print np.arange(10)

# 创建数组
# array 将list tuple 等其他序列转换为ndarray, 可以自动推倒ntype, 也可以显式指定
print np.array([1, 2, 3], dtype=complex)

# asarray 将输入转换为narray, 如果输入本身就是ndarray的话, 那么不进行复制
temp = np.asarray(arr2)
print temp
temp2 = np.asarray(temp)
print temp is temp2

# ones one_like 类似zeros

# 创建单位矩阵
print np.eye(10)
print np.identity(10)

# 类型转换
# 注意转换的时候, 小数部分可能会被截断
# 如果是字符串的数组, 而且字符串是数字, 那么可以转换为数字
# 转换错误会抛出TypeError
print arr1.dtype
float_arr1 = np.asarray(arr1)
print arr1
print float_arr1.astype(np.int64)

# vectorization 矢量化
# 大小相同的数组之间的算术运算会运用到元素级
print arr1
print arr1 * arr1
print arr1 + arr1
print 1 / arr1
print arr1 ** 0.5

# 不同大小的数组之前的运算叫做广播

# 类似list, 可以进行slice切片操作
# 切片时候narray并没有复制,只是指向了同一个位置,如果利用[]对内容修改的话,那么指向的内容也会变化 : 视图
# 原因是numpy设计就是为了处理大量数据,若大量频繁操作,则效率损失特别大
print arr1[1:4]
arr1[1:2] = 100000
print arr1

# 2 维数组
arr2d = np.array([[1, 2], [3, 4]])
print arr2d[1]
print arr2d[1][1]
print arr2d[1, 1]
print arr2d[:, :1]

# bool型索引
name = np.array(['wwx', 'zyf', 'wwx', 'zyh', 'wwx', 'hhh', 'wwx', 'qsy'])
data_rand = np.random.randn(8, 7)
print name
print data_rand
print name == 'wwx'
print data_rand[name == 'wwx', -1]
print data_rand[name == 'wwx', -1:]
print (name == 'wwx') | (name == 'hhh')
data_rand[data_rand < 0 ] = 0
print data_rand

# Fancy indexing 花式索引
# 和slice不一样, 不是视图, 而是复制一个新的数组
arr_fancy = np.empty((8, 4))
for i in range(8):
    arr_fancy[i] = i
print arr_fancy
# 用一个list来选择对应的行, 同时顺序不变
print arr_fancy[[5,2,0]]
print arr_fancy[[-1, 1, -2, 2]]
# 取出(3, -2), (2, 2) (1, 1)
print arr_fancy[[3, 2, 1], [-2, 2, 1]]
# 取出第3, 2, 1行的第2, 0列
print arr_fancy[[3, 2, 1]][:, [2, 0]]
print arr_fancy[np.ix_([2, 3, 0, 0], [0, 2, ])]

# reshape把元素重新排列称对应的数组
# T为对应的转置
arr_shape = np.arange(15).reshape((3, 5))
print arr_shape
print arr_shape.T
# 矩阵乘法
print np.dot(arr_shape, arr_shape.T)

