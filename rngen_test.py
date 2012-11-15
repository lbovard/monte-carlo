#!/usr/bin/env python

import random, math
import numpy as np
import matplotlib.pyplot as plt

n=10000

s=np.zeros(n)

# illustrating importance sampling
for j in range(0,n):
	s[j]=math.pi*math.sqrt(random.random())/2.0

n, ns, patches = plt.hist(s, 20, normed=1)
print np.sum(n * np.diff(ns))
plt.show()

