#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('populations.txt')
year, hares, lynxes, carrots = data.T
year = year.astype(int)
populations = data[:, 1:]
species = np.array(['Hares', 'Lynxes', 'Carrots'])

print '1. The mean and std of the populations of each species for the years in the period:'
print dict(zip(species, populations.mean(axis=0)))
print '2.Which year each species had the largest population:'
print dict(zip(species, year[populations.argmax(axis=0)]))
print '3.Which species has the largest population for each year:'
print dict(zip(year, species[populations.argmax(axis=1)]))
print '4.Which years any of the populations is above 50000:'
print year[[np.any(populations > 50000, axis=1)]]
print '5.The top 2 years for each species when they had the lowest populations:'
print dict(zip(species, year[populations.argsort(axis=0)[:2]].T))
print '6.Compare the change in hare population and the number of lynxes. Check correlation:'
grad = np.gradient(hares)
print np.corrcoef(grad, lynxes)[0,1]
plt.plot(year, grad, year, lynxes)
plt.legend(('Hares', 'Lynxes'), loc='lower center')
plt.show()
