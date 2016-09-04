#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 2012联邦选举委员会数据库


def get_top_amounts(group, key, n=5):
    totals = group.groupby(key)['contb_receipt_amt'].sum()
    return totals.sort_values(ascending=False)[:n]


fec = pd.read_csv('P00000001-ALL.csv')
print fec
# 察看对应行
print fec.ix[123456]

unique_cands = fec.cand_nm.unique()
print unique_cands
print unique_cands[2]

# 党派关系
parties = {'Bachmann, Michelle': 'Republican',
           'Cain, Herman': 'Republican',
           'Gingrich, Newt': 'Republican',
           'Huntsman, Jon': 'Republican',
           'Johnson, Gary Earl': 'Republican',
           'McCotter, Thaddeus G': 'Republican',
           'Obama, Barack': 'Democrat',
           'Paul, Ron': 'Republican',
           'Pawlenty, Timothy': 'Republican',
           'Perry, Rick': 'Republican',
           "Roemer, Charles E. 'Buddy' III": 'Republican',
           'Romney, Mitt': 'Republican',
           'Santorum, Rick': 'Republican'}

print fec.cand_nm[123456:123461]
# 将奥巴马转换为民主党
print fec.cand_nm[123456:123461].map(parties)
# 添加新列
fec['party'] = fec.cand_nm.map(parties)
print fec['party'].value_counts()
# 统计最终捐款和退款的
print (fec.contb_receipt_amt > 0).value_counts()
# 限定真正出资的
fec = fec[fec.contb_receipt_amt > 0]
fec_mrbo = fec[fec.cand_nm.isin(['Obama, Barack', 'Romney, Mitt'])]

# 根据职业和雇主统计赞助信息
print fec.contbr_occupation.value_counts()[:10]

# 职业对应的工作类型
occ_mapping = {
   'INFORMATION REQUESTED PER BEST EFFORTS' : 'NOT PROVIDED',
   'INFORMATION REQUESTED' : 'NOT PROVIDED',
   'INFORMATION REQUESTED (BEST EFFORTS)' : 'NOT PROVIDED',
   'C.E.O.': 'CEO'
}

# 如果没有对应的类型,则直接返回原来的字符串
f = lambda x: occ_mapping.get(x, x)
fec.contbr_occupation = fec.contbr_occupation.map(f)

# 过滤掉出资不足200w的数据
by_occupation = fec.pivot_table('contb_receipt_amt', index='contbr_occupation', columns='party', aggfunc='sum')
over_2mm = by_occupation[by_occupation.sum(1) > 2000000]
print over_2mm

# 下面的绘图建议在ipython的pylab模式下运行
# over_2mm.plot(kind='barh')

# 根据雇主进行聚合
grouped = fec_mrbo.groupby('cand_nm')
# 职业前7
print grouped.apply(get_top_amounts, 'contbr_occupation', n=7)
# 雇主前19
print grouped.apply(get_top_amounts, 'contbr_employer', n=10)

# 对出资额分组
bins = np.array([0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
labels = pd.cut(fec_mrbo.contb_receipt_amt, bins)
print labels

# 根据候选人姓名和面元标签对数据进行分组
grouped = fec_mrbo.groupby(['cand_nm', labels])
print grouped.size().unstack(0)

bucket_sums = grouped.contb_receipt_amt.sum().unstack(0)
print bucket_sums

normed_sums = bucket_sums.div(bucket_sums.sum(axis=1), axis=0)
print normed_sums

# 下面的绘图指令建议在ipython的pylab中使用
# normed_sums[:-2].plot(kind='barh', stacked=True)


