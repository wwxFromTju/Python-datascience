#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# pandas输入输出对象
# 输入输出通常分为几个大类: 读取文本文件/高效的磁盘存储格式,加载数据库中的数据,利用Web API操作网络资源

# 读写文本格式的数据
# pandas提供了一些用于将表格型数据读取为DataFrame对象的函数

# read_csv 从文件/URL/文件型对象中加载带分隔符的数据。默认分隔符为逗号
# read_table 从文件/URL/文件型对象中加载带分隔符的数据。默认分隔符为制表符"\t"
# read_fwf 读取定宽列格式的数据,就是没有分隔符,只靠固定长度
# read_clipboard 读取剪切版中的数据, 可以理解为read_table的剪贴板版。(一般用于从网页中收集数据)

# 下面的命令在ipython中运行
# 运行shell中的cat出ex1.csv的内容
# !cat ex1.csv
# 等价于用pandas来读取
# 因为csv是用','分隔的,所以可以直接使用read_csv
df = pd.read_csv('ex1.csv')
print df
# 也可以使用read_table,然后指定分隔符
df_read_table = pd.read_table('ex1.csv', sep=',')
print df_read_table

# 下面的命令在ipthon中运行
# !cat ex2.csv
# 注意到和ex1.csv不同的是第一行,ex1的第一行是属性,然后ex2的第一行就直接是数据
# 可以用pandas来分配默认的列名, 默认是从0开始的连续数字
df_defaul_col = pd.read_csv('ex2.csv', header=None)
print df_defaul_col
# 也可以指定对应的列名
df_set_col = pd.read_csv('ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
print df_set_col
# 可以通过设置index_col来指定索引列,可以指定多个
names = ['a', 'b', 'c', 'd', 'message']
pd_set_index = pd.read_csv('ex2.csv', names=names, index_col=['message'])
print pd_set_index

# 下面的命令在ipython中运行
# !cat csv_mindex.csv
# 将多个列做成层次索引
parsed =  pd.read_csv('csv_mindex.csv', index_col=['key1', 'key2'])
print parsed

# 有些文件由数量不确定的空白符号分隔,可以使用正则表达式来分隔
print list(open('ex3.txt'))
# 由于空白的个数不确定,但是数量>=1,所以使用\s+
# 由于第一行的列比下面的行的列少一列,所以读取的时候推断第一列为索引列
result = pd.read_csv('ex3.txt', sep='\s+')
# 等价于下面那一句
# result = pd.read_table('ex3.txt', sep='\s+')
print result

# 下面的命令在ipython中运行
# !cat ex4.csv
# 为异形的文件,即行与行的格式不一样,只读取其中几行
# 使用skiprows来跳过
df_skip_rows = pd.read_csv('ex4.csv', skiprows=[0, 2, 3])
df_skip_rows_end = pd.read_csv('ex4.csv', skip_footer=1)
print df_skip_rows
print df_skip_rows_end

# 处理缺失值
# 默认情况下,pandas的缺失值可以指定,比如:NA, -1, #IND, NULL等
resule_ex5 = pd.read_csv('ex5.csv')
# 没有处理缺失值
print resule_ex5
print resule_ex5.isnull()
# 用na_values来指定缺失值
resule_ex5_lack = pd.read_csv('ex5.csv', na_values=['foo'])
# 注意上面和下面的isnull的不同,上面只识别NaN是null, 下面我们指定了foo是null
# 所以下面的foo被换为NaN
print resule_ex5_lack
# print resule_ex5_lack.isnull()
# 可以使用字典, 针对不同的列指定不同的缺失值
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
result_ex5_col_lack = pd.read_csv('ex5.csv', na_values=sentinels)
print resule_ex5_lack

# read_csv/read_table函数的参数
# path 指定文件系统的位置, URL, 文件型对象的字符串
# sep或delimiter 指定分隔符是什么,可以是字符串也可以是正则表达式
# header 用作列名的行号,默认为0(第一行),如果没有header的行就设置为None
# index_col 来层次化索引, 可以是单个名称/数字或由多个名称/数字组成的列表(层次化索引)
# names 用于结果的列名列表, 结合header=None
# skiprows 忽略掉的行数,从0开始
# na_values 用来指定缺失值
# comment 用于将注释信息拆分出去的字符
# parse_dates 将数据解析为日期, 默认为False。如果为True则解析所有列。还可以指定一组行号或列号。如果列表的元素为列表或者元组,则将多个列组合在一起再进行日期解析工作
# keep_date_col 如果连接多列解析日期,则保持参与连接的列。默认为False。
# converters 由列号/列名跟函数之间的映射关系组成的字典。例如,{'foo': f}会对foo列的所以值运用函数f
# dayfirst 当解析有歧义的日期时,将其看做国际格式(7/6/2012 -> June 7, 2012)。默认为False
# date_parse 用于解析日期的函数
# nrows 需要读取的行数
# iterator 返回一个TextParse以便逐块读取文件
# chunksize 文件块的带小奥
# skip_footer 需要忽略的行数,从后面算回来,是一个数,不能是list,最后一行是1,然后往上增加,是指忽略n到最后
# verbose 打印各种解析器输出信息
# encoding 用于unicode的文本编码格式
# squeeze 如果数据解析后只有一行,则返回Series
# thousands 千分位分隔符, 如','或'.'