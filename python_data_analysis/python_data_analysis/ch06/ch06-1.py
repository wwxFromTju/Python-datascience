#!/usr/bin/env python
# encoding=utf-8

# pandas输入输出对象
# 输入输出通常分为几个大类: 读取文本文件/高效的磁盘存储格式,加载数据库中的数据,利用Web API操作网络资源

# 读写文本格式的数据
# pandas提供了一些用于将表格型数据读取为DataFrame对象的函数

# read_csv 从文件/URL/文件型对象中加载带分隔符的数据。默认分隔符为逗号
# read_table 从文件/URL/文件型对象中加载带分隔符的数据。默认分隔符为制表符"\t"
# read_fwf 读取定宽列格式的数据,就是没有分隔符,只靠固定长度
# read_clipboard 读取剪切版中的数据, 可以理解为read_table的剪贴板版。(一般用于从网页中收集数据)

# 下面的命令在ipython中运行