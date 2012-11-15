#!/usr/bin/env python

'''
naive monte carlo integration of

\int_{-1}^{1}\int_{-1}^{1}\exp(-(x-y)^{2}) 
\approx \frac{4}{N}\sum_{n=1}^{N}f(x_{i},y_{i})
'''
import random
import numpy as np
n=10000

exact=2.54664120193843
def f(x,y):
	return np.exp(-(x-y)**2)

mc_sum=0.0;

for i in range(0,n):
	mc_sum=mc_sum+f(random.uniform(-1,1),random.uniform(-1,1))

mc_sum=4.0*mc_sum/n
print 'approx=',mc_sum
print 'exact =',exact
print 'error =', np.fabs(exact-mc_sum)
