#!/usr/bin/env python

import random, math
import numpy as np

#number of trials per run
ntrial=10000
x=np.zeros(2)

def trial(n_steps):
	x=np.zeros(2)
	for j in range(0,n_steps):
		r=random.random()
		if r<0.25:
			x[0]=x[0]+1
		elif r<0.5:
			x[1]=x[1]+1
		elif r<0.75:
			x[0]=x[0]-1
		else:
			x[1]=x[1]-1

	return x

def distance(x):
	return math.sqrt(x[0]**2+x[1]**2)

N=1
pows=7
data=np.zeros([2,pows])
for j in range(0,pows):
	N=N*10
	data[0,j]=N
	mdist=0.0
	for i in range(0,ntrial):
		x=trial(N)
		mdist=distance(x)+mdist
	data[1,j]=mdist/ntrial

print data
