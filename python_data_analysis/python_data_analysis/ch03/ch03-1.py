#!/usr/bin/env python
# encoding=utf-8
# 这一章的代码是在ipython下运行的,所以一下代码建议复制到ipython下运行

import numpy as np
import datetime

def add_numbers(a, b):
    '''
    这里是文档注释
    :param a:
    :param b:
    :return: a+b
    '''

    return  a + b


data = {i : np.random.randn() for i in range(7)}
# print data

# 在ipython可以通过tab键自动补全

an_apple = 27
an_example = 42
# 在这里输入an然后按tab键会在下面提示相应变量
# an_apple   an_example

b = [1, 2, 3]
# 在这里输入b.然后按tab,然后下面会提示list的相应的方法

# 这里输入datetime.然后按tab,然后会提示datetime下面的方法
# ipython会隐藏以下划线开头的方法和属性
# 你可以通过先输入_然后再按tab键来进行补全

# 同时tab键还可以进行类似的路径补全的东西,只要你的当前输入像一个路径

# 内审: 在一个变量的前面或者后面加上一个?可以获得这个对象的通用信息
# 比如b? ?b ?b?

# 对于一个方法可以用过一个?来获得对应的信息和文档注释
# 也可以通过两个??来获得对应的sourcecode
# 比如add_numbers?? 或者 ??add_numbers ??add_numbers??

# 同时可以通过 * 和 ? 来搜索命名空间中的信息
#  np.*load*?

# %run 在ipython中可以通过这条命令来直接运行对应的python文件
# 比如在当前路径下运行 %run ch03-1.py
# 由于脚本是在一个空的命名空间运行的,所以外部的变量不会干扰到内部的代码
# 如果需要访问ipython命名空间中的变量,那么应该使用: %run -i xxxx.py
# 但是在运行脚本之后可以访问内部的变量

# 中断正在运行中的ipython 或者通过%run 运行的代码段, 可以通过ctrl-c来直接中断

# 如果在ipython终端中直接复制粘贴的话
# 如果你在缩进中有空白的换行, 那么这个时候如果直接复制的会出现报错
# 在这个时候应该是采用 %paste 运行, ipython会自动将粘贴板中的文字代码复制进去
# 同理 %cpython ,然后复制进去, 之后ctrl-d 来结束输入



