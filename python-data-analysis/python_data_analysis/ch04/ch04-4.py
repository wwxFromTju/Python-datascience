#!/usr/bin/env python
# encoding=utf-8

import random
import numpy as np

position = 0
walk_random = [position]
steps_random = 1000
for i in xrange(steps_random):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk_random.append(position)

# 在ipython --pylab模式下
# plot(walk)

nsteps_numpy = 1000
draws_numpy = np.random.randint(0, 2, size=nsteps_numpy)
nsteps_numpy = np.where(draws_numpy > 0, 1, -1)
walk_numpy = nsteps_numpy.cumsum()
