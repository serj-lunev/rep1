import numpy as np
import matplotlib.pyplot as mpl

g = np.genfromtxt("bkgd.csv", dtype = [float, float, float, float, float, float, float, float, float, float, float, int],
names = ['M2AB', 'M2AC', 'XA', 'XB', 'XC', 'Y1', 'Y2', 'Y3', 'Y4', 'W', 'PMIN', 'ID'], delimiter = '\t', skiprows = 1)
x = [i[0] for i in g]
y = [i[1] for i in g]
mpl.hist2d(x, y, bins = 40, range = [[0, 0.8], [0, 0.8]], cmap = mpl.cm.Blues)
mpl.colorbar()
mpl.xlabel("M2AB")
mpl.ylabel("M2AC")
mpl.show()