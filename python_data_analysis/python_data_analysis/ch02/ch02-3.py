#!/usr/bin/env python
# encoding=utf-8
import pandas as pd
import numpy as np
#注意在ipython --pylab模式下面运行这段代码的时候需要import
# import matplotlib.pyplot as plt

def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group


def get_top1k(group):
    return group.sort_index(by='births', ascending=False)[:1000]


def get_quantile_count(group, q=0.5):
    group = group.sort_index(by='prop', ascending=False)
    return int(group.prop.cumsum().searchsorted(q) + 1)

columns = ['name', 'sex', 'births']
names1880 = pd.read_csv('../../pydata-book-master/ch02/names/yob1880.txt', names=columns)
# print names1880
# print names1880.groupby('sex').births.sum()

years = range(1880, 2011)
pieces = []

for year in years:
    path = '../../pydata-book-master/ch02/names/yob{}.txt'.format(year)
    frame = pd.read_csv(path, names=columns)

    frame['year'] = year
    pieces.append(frame)

# print pieces
names = pd.concat(pieces, ignore_index=True)
# print names

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
# print total_births.tail()

# 注意一下,下面这个语句需要在ipython --pylab模式下运行
# total_births.plot(title='Total births by sex and year')

keys = ['year', 'sex']

names = names.groupby(keys).apply(add_prop)
# print names

np.allclose(names.groupby(keys).prop.sum(), 1)

top1k = names.groupby(keys).apply(get_top1k)
# print top1k

pieces2 = []
for year, group in names.groupby(['year', 'sex']):
    pieces2.append(group.sort_index(by='births', ascending=False)[:1000])
top1000 = pd.concat(pieces2, ignore_index=True)
# print top1000

boys = top1k[top1k.sex == 'M']
girls = top1k[top1k.sex == 'F']
# print boys
# print girls

total_births2 = top1k.pivot_table('births', index='year', columns='name', aggfunc=sum)
# print total_births2

subset = total_births2[['John', 'Harry', 'Mary', 'Marilyn']]

#注意下面的代码需要在ipython --pylab
#subset.plot(subplots=True, figsize=(12, 10), grid=False, title='Number of births per year')

table = top1k.pivot_table('prop', index='year', columns='sex', aggfunc=sum)
#注意一下代码要在ipython --pylab
# table.plot(title='Sum of table1k.prop by year and sex', yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))

df = boys[boys.year == 2010]
# print df

prop_cumsum = df.sort_index(by='prop', ascending=False).prop.cumsum()
# print prop_cumsum[:10]
# print prop_cumsum.searchsorted(0.5)

df = boys[boys.year == 1900]
in1900 = df.sort_index(by='prop', ascending=False).prop.cumsum()
# print in1900.searchsorted(0.5) + 1

diversity = top1k.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')
# print diversity.head()

# 注意下面的代码需要在ipython --pylab模式下运行
# diversity.plot(title='Number of popular names in top 50%')

get_last_letter = lambda x : x[-1]
lase_letters = names.name.map(get_last_letter)
lase_letters.name = 'last_letter'

table = names.pivot_table('births', index=lase_letters, columns=['sex', 'year'], aggfunc=sum)
# print table
subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
# print subtable.head()
# print subtable.sum()

letter_prop = subtable / subtable.sum().astype(float)
# print letter_prop

#下面3行代码需要在ipython --pylab模式下运行
# fig, axes = plt.subplots(2, 1, figsize=(10, 8))
# letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
# letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)

letter_prop = table / table.sum().astype(float)
dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T
# print dny_ts.head()

#下面的代码需要在ipython --pylab模式下面运行
# dny_ts.plot()

all_names = top1k.name.unique()
mask = np.array(['lesl' in x.lower() for x in all_names])
lesley_like = all_names[mask]
# print lesley_like

filtered = top1k[top1k.name.isin(lesley_like)]
# print filtered.groupby('name').births.sum()

table = filtered.pivot_table('births', index='year', columns='sex', aggfunc='sum')
table = table.div(table.sum(1), axis=0)

# 下面的代码需要在ipython --pylab模式下面运行
# table.plot(style={'M': 'k-', 'F': 'k--'})
