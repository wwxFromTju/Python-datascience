#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

# 散布图scatter plot
macro = pd.read_csv('macrodata.csv')
data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
trans_data = np.log(data).diff().dropna()
print trans_data[-5:]

plt.scatter(trans_data['m1'], trans_data['unemp'])
plt.title('Change in log{} vs. {}'.format('m1', 'unemp'))

# 散布图矩阵(scatter plot matrix)
pd.scatter_matrix(trans_data, diagonal='kde', color='k', alpha=0.3)