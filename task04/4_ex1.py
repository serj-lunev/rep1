import numpy as np
import matplotlib.pyplot as mpl

data = np.genfromtxt("bkgd.csv")[1:]
columns = ["M2AB", "M2AC", "XA", "XB", "XC", "Y1", "Y2", "Y3", "Y4", "W", "PMIN", "ID"]
mpl.figure(1,figsize=(10, 5), facecolor='white')
mpl.subplot(121)
mpl.hist(data[::,0], bins=30, histtype='step')
mpl.subplot(122)
mpl.xlim(0, 0.5)
mpl.xlabel('M2AB')
mpl.ylabel('N')
y, bin_edge, useless = mpl.hist(data[::,0], bins=50, histtype='step')
bin_centres = 0.5*(bin_edge[1:] + bin_edge[:-1])
mpl.errorbar(bin_centres, y, yerr=y**0.5, color='red', linestyle='None', marker='o', markersize=2)
mpl.show()