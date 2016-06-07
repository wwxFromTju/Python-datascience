#!/usr/bin/env python
# encoding=utf-8

import json

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 载入json
db = json.load(open('foods-2011-10-03.json'))

# 察看对应的信息
print len(db)
print db[0].keys()
print db[0]['nutrients'][0]

nutrients = DataFrame(db[0]['nutrients'])
print nutrients[:7]

info_keys = ['description', 'group', 'id', 'manufacturer']
info = DataFrame(db,  columns=info_keys)
print info[:5]
print info

print pd.value_counts(info.group)[:10]

nutrients = []

for rec in db:
    fnuts = DataFrame(rec['nutrients'])
    fnuts['id'] = rec['id']
    nutrients.append(fnuts)

nutrients = pd.concat(nutrients, ignore_index=True)
print nutrients
print nutrients.duplicated().sum()

nutrients = nutrients.drop_duplicates()

col_mapping = {'description': 'food',
               'group': 'fgroup'}

info = info.rename(columns=col_mapping, copy=False)
print info

col_mapping = {'description': 'nutrient',
               'group': 'nutgroup'}
nutrients = nutrients.rename(columns=col_mapping, copy=False)
print nutrients

ndata = pd.merge(nutrients, info, on='id', how='outer')
print ndata
print ndata.ix[30000]

result = ndata.groupby(['nutrient', 'fgroup'])['value'].quantile(0.5)
# 下面这句话在ipython中运行
# result['Zinc, Zn'].order().plot(kind='barh')

by_nutrient = ndata.groupby(['nutgroup', 'nutrient'])

get_maximun = lambda x: x.xs(x.value.idxmax())
get_minimun = lambda x: x.xs(x.value.idxmin())

max_foods = by_nutrient.apply(get_maximun)[['value', 'food']]

max_foods.food = max_foods.food.str[:50]
