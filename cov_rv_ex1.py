#!/usr/bin/env python

import random, math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

n=50000

fig=plt.figure()
ax=fig.add_subplot(111)
s=np.zeros(n)

for j in range(0,n):
	s[j]=random.gauss(0,1)**2

n,bins,patches= ax.hist(s,200,normed=1, facecolor='green')

ncenters = 0.5*(bins[1:]+bins[:-1])
y=np.zeros(len(ncenters))
for j in range(0,len(ncenters)):
	y[j]=1/np.sqrt(2*np.pi*ncenters[j])*np.exp(-ncenters[j]/2)

ax.plot(ncenters, y, 'r--', linewidth=3)

plt.xlim([0,5])
plt.grid(True)
plt.show()

