#!/usr/bin/env python
# encoding=utf-8

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 随机采样和排列

# 从牌堆中抽取5张牌
def draw(deck, n=5):
    return deck.take(np.random.permutation(len(deck))[:n])


# 红桃Hearts 黑桃Spades 梅花Clubs 方块Diamonds
suits = ['H', 'S', 'C', 'D']
card_val = (range(1, 11) + [10] * 3) * 4
base_names = ['A'] + range(2, 11) + ['J', 'K', 'Q']
cards = []

for suit in suits:
    cards.extend(str(num) + suit for num in base_names)
deck = Series(card_val, index=cards)
print deck[:13]

# 随机抽5张牌
print draw(deck)

# 从每种花色中随机抽取2张牌
# 先groupby分组再抽取
get_suit = lambda card: card[-1]
print deck.groupby(get_suit).apply(draw, n=2)
print deck.groupby(get_suit, group_keys=False).apply(draw, n=2)
