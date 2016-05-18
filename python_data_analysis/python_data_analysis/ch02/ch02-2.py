#!/usr/bin/env python
# encoding=utf-8
import pandas as pd


#读取对应的数据,为表的格式
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
user = pd.read_table('../../pydata-book-master/ch02/movielens/users.dat', sep='::', header=None, names=unames)

rname = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('../../pydata-book-master/ch02/movielens/ratings.dat', sep='::', header=None, names=rname)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('../../pydata-book-master/ch02/movielens/movies.dat', sep='::', header=None, names=mnames)

# print user[:5]
# print ratings[:5]
# print movies[:5]
# print ratings

#通过相同的属性将表合并在一起
data = pd.merge(pd.merge(ratings, user), movies)
#print data
# print data.ix[0]

#原来的代码中为: rows='title' cols='gender' 对于现在的方法中的key不对应
#现在的key为:pandas.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All')
mean_ratings = data.pivot_table('rating', index=['title'], columns=['gender'], aggfunc='mean')
#print mean_ratings[:5]

ratins_by_title = data.groupby('title').size()
# print ratins_by_title[:10]

active_titles = ratins_by_title.index[ratins_by_title >= 250]
# print active_titles

mean_ratings = mean_ratings.ix[active_titles]
# print mean_ratings

top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
# print top_female_ratings[:10]

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')
# print sorted_by_diff[:15]
# print sorted_by_diff[-15:][::-1]

rating_std_by_title = data.groupby('title')['rating'].std()
ratins_std_by_title = rating_std_by_title.ix[active_titles]
print ratins_std_by_title.order(ascending=False)[:10]
