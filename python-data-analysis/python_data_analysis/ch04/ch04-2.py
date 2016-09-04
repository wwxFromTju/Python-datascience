#!/usr/bin/env python
# encoding=utf-8

import numpy as np
# 下面这句尽量在虚拟环境中使用
# import matplotlib.pyplot as plt

# numpy中的一元ufunc
# abs fabs 计算整数 浮点数 负数的绝对值, 不是复数可以使用fabs更快
# sqrt 平方根 类似 x ** 0.5
# square 平方 类似 x ** 2
# exp 自然指数
# log log10 log2 log1p 对应的对数
# sign 计算正负 正 +1 零 0 负 -1
# ceil 计算天蓬
# floor 计算地板
# rint 四舍五入
# modf 将数组的小数和整数部分分开返回
# isnan 返回bool数组, nan的值的位置为True
# isfinite isinf 返回bool数组 分别是有穷, 无穷
# cos cosh sin sinh tan tanh 普通型, 双曲型三角函数
# arccos arccosh arcsin arcsinh arctan arctanh 对应的反三角函数
# logcal_not 计算not x, 相当于 -arr


# numpy中的二元ufunc
# add 相加
# subtract 第一个数组减掉第二个数组
# multiply 数组元素相乘
# divide floor_divide 除法 向下取整除法
# power 乘方
# maximum fmax 在参数中的最大数字, fmax会忽略 NaN
# minimum fmin 和上面那个类似,但是是取小的值
# mod 元素级别的取余
# copysign 将第二个数组中的元素符号复制给第二个数组
# greater greater_equal less less_equal  equal not_equal 为bool数组, 为2个数组对应元素的比较
# logical_and logical_or logical_xor 元素级别的真值逻辑运算

# 科学计算中,通常用矢量化来替代循环,这样通常比较快

# 生成对应的数组从-5 到 5, 步长为0.001
points = np.arange(-5, 5, 0.001)
# meshegrid接受2个数组输入,然后生成2个二维矩阵,其中的值为数组对应的
xs, ys = np.meshgrid(points, points)
print points
print xs
print ys

# 下面的语句最好不要在虚拟环境中运行,推荐在ipython中运行
# z = np.sqrt(xs **2 + ys ** 2)
# cmap是设置对应的图片的颜色
# plt.imshow(z, cmap=plt.cm.gray)
# 画出旁边的颜色和对应的数值
# plt.colorbar()
# 画出标题
# plt.title('Image plot of $\sqrt{x^2 + y^2}$ for a grid of values')

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

# 如果是是使用python的if else
result_python = [(x if c else y)
                 for x, y, c in zip(xarr, yarr, cond)]
# 可以使用numpy的where函数
result_numpy = np.where(cond, xarr, yarr)
print result_python
print result_numpy == result_python

arr_rand = np.random.randn(4, 4)
print arr_rand
print np.where(arr_rand > 0, 2, -2)
print np.where(arr_rand > 0, 2, arr_rand)

arr_rand2 = np.random.randn(5, 4)
print arr_rand2.mean()
print np.mean(arr_rand2)
print arr_rand2.sum()
print np.sum(arr_rand2)
# 对于上面调用和类似的函数, 可以指定一个axis参数, 用来指定是从那一维计算, 结果比原来的少一维
print arr_rand2.mean(axis=1)
print arr_rand2.mean(1)
print arr_rand2.sum(axis=0)
print arr_rand2.sum(0)

# 类似cumsum, cumprod 之类的函数则不聚合, 产生的是中间结果的数组
arr_rand3 = np.array([[0, 1, 2],
                      [3, 4, 5],
                      [6, 7, 8]])
print arr_rand3.cumsum(0)
print arr_rand3.cumsum(1)
print arr_rand3.cumprod(1)

# 用于bool型数组的方法
arr_bool = np.random.randn(100)
print arr_bool
print (arr_bool > 0).sum()
bools = np.array([False, False, True])
print bools.any()
print bools.all()

# numpy的数组可以通过sort方法排序
arr = np.random.randn(8)
print arr
arr.sort()
print arr
# 可以在多维数组上进行排序,只要指定axis
arr = np.random.randn(5, 3)
print arr
arr.sort(1)
print arr
large_arr = np.random.randn(1000)
large_arr.sort()
# 中位数
print large_arr[int(0.05 * len(large_arr))]

# 惟一化和其他逻辑
names = np.array(['wwx', 'zyf', 'qsy', 'zyh', 'wwx', 'father', 'wwx is other father'])
print np.unique(names)
ints = np.array([1, 2, 3, 4, 1, 2, 3, 4, 5, 61, 2])
print np.unique(ints)
# 判断第一个数组的元素是否在在第二个数组
values = np.array([6, 0, 0, 3, 2, 5, 6])
print np.in1d(values, [2, 3, 6])
# 还有其他运算
# unique(x) 返回x中的唯一的元素,同时有序
# intersect1d(x, y) 计算x, y中的公共元素, 同时有序
# union1d(x, y) 计算x, y的并集, 同时有序
# in1d(x, y) 判断x中元素是否在y中, 为bool数组
# setdiff1d(x, y) 差集
# setxor1d(x, y) 对称差