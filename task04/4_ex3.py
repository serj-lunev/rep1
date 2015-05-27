import numpy as np
import matplotlib.pyplot as mpl
from mpl_toolkits.mplot3d import Axes3D

g = np.genfromtxt("bkgd.csv", dtype = [float, float, float, float, float, float, float, float, float, float, float, int],
names = ['M2AB', 'M2AC', 'XA', 'XB', 'XC', 'Y1', 'Y2', 'Y3', 'Y4', 'W', 'PMIN', 'ID'], delimiter = '\t', skiprows = 1)
x_d = [i[0] for i in g]
y_d = [i[1] for i in g]
hist, x, y = np.histogram2d(x_d, y_d, bins = 40, range = [[0, 0.8], [0, 0.8]])
fig = mpl.figure()
ax = Axes3D(fig)
x, y = np.meshgrid(x[:40], y[:40])
surf = ax.plot_surface(x[:40], y[:40], hist, rstride=1, cstride=1, cmap='Blues', linewidth = 0)
fig.colorbar(surf, shrink = 0.5, aspect = 5)
ax.invert_yaxis()
ax.invert_xaxis()
ax.view_init(elev = 75, azim = -150)
mpl.show()