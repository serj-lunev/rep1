import numpy as np
print('Form the 2-D array (without typing it in explicitly):')
a = np.arange(1, 16, 1).reshape(3, 5).transpose()
print a
print('and generate a new array containing its 2nd and 4th rows')
b = a[[2, 4]]
print b