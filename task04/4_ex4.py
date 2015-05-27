import numpy as np
import matplotlib.pyplot as mpl
from scipy.stats import pearsonr

g = np.genfromtxt("bkgd.csv", dtype = [float, float, float, float, float, float, float, float, float, float, float, int],
names = ['M2AB', 'M2AC', 'XA', 'XB', 'XC', 'Y1', 'Y2', 'Y3', 'Y4', 'W', 'PMIN', 'ID'], delimiter = '\t', skiprows = 1)
x = [i[0] for i in g]
for j in range(12):
    x[j] = [i[j] for i in g]
matrix = np.array([pearsonr(z, y)[0] for z in x[:9] for y in x[:9]])
mpl.imshow(matrix.reshape(9, 9), cmap='Reds', interpolation = 'None')
ax = mpl.gca()
ax.invert_yaxis()
mpl.colorbar()
mpl.yticks(np.arange(9), ('M2AB', 'M2AC', 'XA', 'XB', 'XC', 'Y1', 'Y2', 'Y3', 'Y4'), rotation = 'horizontal')
mpl.xticks(np.arange(9), ('M2AB', 'M2AC', 'XA', 'XB', 'XC', 'Y1', 'Y2', 'Y3', 'Y4'), rotation = 'vertical')
mpl.show()