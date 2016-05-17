import pandas as pd
import numpy as np
import json
from collections import defaultdict
from pandas import DataFrame, Series

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts


def top_counts(count_dict, n = 10):
    values_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    values_key_pairs.sort()
    return values_key_pairs[-n:]




path = '../../pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'

records = [json.loads(line) for line in open(path)]
#print records

time_zone = [rec['tz'] for rec in records if 'tz' in rec]
#print time_zone

counts = get_counts(time_zone)
counts2 = get_counts2(time_zone)
#print counts,'\n',counts2

top_counts_10 = top_counts(counts)
#print top_counts_10

frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()
#print tz_counts[:10]

clean_tz = frame['tz'].fillna("Missing")
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts_clean = clean_tz.value_counts()
#print tz_counts_clean[:10]
#在虚拟环境下,matplotlib不能显示出来,推荐采用在命令行中直接 ipython --pylib然后运行本文件代码
tz_counts_clean[:10].plot(kind='barh', rot=0)