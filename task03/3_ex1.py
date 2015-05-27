import numpy as np
import matplotlib.pyplot as plt
# a cosine as a function of time
x = np.arange(-6, 6, 0.1)
y = np.cos(x)
plt.plot(x, y)
#plt.title("cos(t)")
plt.xlabel("t")
plt.ylabel("cos(t)")
plt.show()
# 2D matrix using the gray colormap
image = np.random.rand(50, 50)
plt.imshow(image, cmap=plt.cm.gray)
plt.show()