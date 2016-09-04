#!/usr/bin/env python
# encoding=utf-8

# 未完成

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from pandas import Series, DataFrame

# 绘制地图
# 图形化显示海地地震危机数据


def to_cat_list(catstr):
    stripped = (x.strip() for x in catstr.split(','))
    return [x for x in stripped if x]


def get_all_categories(cat_series):
    cat_sets = (set(to_cat_list(x)) for x in cat_series)
    return sorted(set.union(*cat_sets))


def get_english(cat):
    code, names = cat.split('.')
    if '|' in names:
        names = names.split('|')[1]
    return code, names.strip()


def get_code(seq):
    return [x.split('.')[0] for x in seq if x]

data = pd.read_csv('Haiti.csv')
data = data[(data.LATITUDE > 18) & (data.LATITUDE < 20) & (data.LONGITUDE > -75) & (data.LONGITUDE < -70) & data.CATEGORY.notnull()]

get_english('2. Urgences logistiques | Vital Lines')

all_cats = get_all_categories(data.CATEGORY)
english_mapping = dict(get_english(x) for x in all_cats)
print english_mapping['2a']
print english_mapping['6c']

all_codes = get_code(all_cats)
code_index = pd.Index(np.unique(all_codes))
dummy_frame = DataFrame(np.zeros((len(data), len(code_index))), index=data.index,
                        columns=code_index)
# print dummy_frame.ix[:, :6]

for row, cat in zip(data.index, data.CATEGORY):
    codes = get_code(to_cat_list(cat))
    dummy_frame.ix[row, codes] = 1
data = data.join(dummy_frame.add_prefix('category_'))
data.ix[:, 10:15]
