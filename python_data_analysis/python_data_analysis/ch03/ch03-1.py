#!/usr/bin/env python
# encoding=utf-8
# 这一章的代码是在ipython下运行的,所以以下代码建议复制到ipython下运行

import numpy as np
from IPython.core.debugger import Pdb
import sys
import datetime


def add_numbers(a, b):
    """
    这里是文档注释
    :param a:
    :param b:
    :return: a+b
    """
    return a + b


def set_trace():
    Pdb(color_scheme='Linux').set_trace(sys._getframe().f_back)


def debug(f, *args, **kwargs):
    pdb = Pdb(color_scheme='Linux')
    return pdb.runcall(f, *args, **kwargs)


def f(x, y, z=1):
    tmp = x + y
    return tmp / z


# 这里可以方便地使用pdb
debug(f, 1, 2, z=3)

# 这里用ipython的run运行这个脚本文件的时候, 会自己在这里停
# pdf.set_trace
set_trace()
data = {i: np.random.randn() for i in range(7)}
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


# ctrl + p 或者 ctrl + 向上 为: 在历史记录中向上搜索, 如果这个时候已经有一部分输入了,那么是含有这部分的历史记录
# ctrl + n 或者 ctrl + 向下 为: 与上面相同, 不过是向下
# ctrl + r 搜索 : 可以部分匹配
# command + shift + v(OS X mac) : 从剪贴板中复制
# ctrl + c : 中止当前正在运行的代码
# ctrl + a : 光标移动到行头
# ctrl + e : 光标移动到行尾
# ctrl + k : 删除从光标开始到行尾的字母
# ctrl + u : 删除从行开头到光标的字母
# ctrl + f : 光标向前移动一个字母
# ctrl + b : 光标向后移动一个字母
# ctrl + l : 清屏和 clear 命令一样


# 通过%run命令来直接运行的python脚本如果发生异常, 那么ipython会打印出调用栈来trackback

# 在ipython有Magic Command即魔术命令, 通常为%xxx格式的
a = np.random.randn(100,100)
# 以下这条命令在ipython下面运行
# %timeit np.dot(a, a) 来计算np.dot(a, a)的时间
# 比如%reset -f 可以重置命名空间
# 在ipython中输入 %magic 或者 %quickref 可以察看这些特殊的命令
# %quickref : ipython 中的快速参考
# %magic : 魔术命令的文档
# %debug : 察看最近的异常信息,然后进入ipdb调试,
# %hist : 输出之前的输入的历史记录
# %pdb : 开启之后,如果发生异常,那么进入ipdb调试, 之后可以通过u(up),d(down)来跳转不同栈,用s xx 来在xx行加断电,然后c(continue),之后可以n来接着执行,默认为关闭,发生异常时候只输出异常信息
# %paste : 直接复制粘贴板的内容
# %cpaste : 打开一个可以手工复制的操作
# %reset : 清楚命名空间
# %page object : 分页打印object
# %run xxx.py : 运行对应的python脚本, 加上参数d : 为debug模式, 加上b行号, 为在第xx行加上断点,
# %prun xxx.py : 通过cProfile来执行statement, 并打印分析器的输出结果, 这是用来分析程序的
# %time xxxxxxx : 用来统计xxxxxxx的运行时间
# %timeit XXXXXXX : 通过多次执行xxxxxxx然后取平均数来分析, 对于小的程序而言, 由于运行时间太短, 用%time 无法统计
# %who %who_ls %whos 来显示命名空间中定义的变量
# %xdel xxx : 来删除对应xxx


# 通过ipython qtconsole --pylab=inline 来启动 给予QT的ipython
# 通过ipthon --pylab 来启动ipython同时集成matplotlib

# ipython 维护一个在硬盘上的小型的数据库, 其中包含着你执行过的每一条命令的文本
# 这样可以用来搜索, 并自动执行你之前执行过的命令
# 会话间持久化命令历史
# 将输入/输出历史记录到日志文件

# 在ipython中 _ 保存着上一个输出, __ 保存着上上个输出

# _i行号xx : 为第xx行的输入变量, 为字符串, 所以可以用exec关键字来重新执行
# _行号xx : 为第xx行的输出

# 在操作大量数据的时候, 可以尝试使用 %reset %xdel 来避免内存方面的问题

# 如果要保存日志%logstart 对应 %logoff, 还有 %logon %logstate %logstop

# ipython存在与相应操作系统交互的魔术命令, 与具体平台相关
# 类似 %ls %pwd等等
# 也可以用 !xxx 来在系统的shell中执行xxx, xxx 的参数可以是使用ipython中的变量, 不过要在前面加$
# 可以用%alias x1 xxxxx -xxx : 来别名xxxx -xxx ,可以用x1来简化输入

# %bookmark xx 路径 : 可以保存路径, 之后可以通过cd x1来快速跳转

# ipython(python)调试命令:
# h help: help 显示命令列表
# help xxx : 显示xxx的文档
# c continue : 恢复城市的执行
# q quit : 退出调试器, 不再执行
# b(break) xxx : 在当前文件的xxx行加断点
# b 路径/文件名 xx行 : 指定文件加上断点
# s step : 单步进入函数调用
# n next : 执行当前行, 并前进到当前级别的下一行
# u, d : 在上面的pdb中说了
# a args : 显示当前函数的参数
# debug xxx : 在新的调试器(递归)中调用语句xxx
# l(list) xxx : 显示xxx行,与xxx行的上下问参考代码
# w where : 打印当前的完整栈跟踪


# 通过ipython notebook --pylab=inline 来启动notebook,同时包含matplotlib

# python(ipython) 为 "一次加载"
# 即在import xxx 时候, xxx中的代码会被执行, 其中所有的变量, 函数, 引入项, 都会被保存在一个新建的xxx模块命名空间
# 之后如果修改了xxx ,但是有地方在import xxx, 还是执行第一次import的那个旧的xxx, 所以如果需要的话,使用reload(xxx)