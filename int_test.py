#!/usr/bin/env python
'''
This is a simple program that integrates

\int_{0}^{\pi/2}dx \sin x

using simple Monte Carlo and importance sampled Monte carlo
'''
import numpy as np
import random,math

#number of data points
N=1000
exact=1.0

def f(x):
	return np.sin(x)

is_sum=0.0
nois_sum=0.0

for i in range(0,N):
	isvar=math.pi*math.sqrt(random.random())/2.0
	noisvar=math.pi*random.random()/2.0
	is_sum=is_sum+f(isvar)/isvar
	nois_sum=nois_sum+f(noisvar)

#mutiply by constants
nois_sum=math.pi/(2.0*N)*nois_sum
is_sum=math.pi**2 /(8.0*N)*is_sum

print 'no is=',nois_sum
print 'w/ is=',is_sum
print 'exact=',exact
	
