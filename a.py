import numpy as np

x = np.array([[1, 2, 3,4], [5, 6,7,8], [9,10,11,12],[13,14,15,16]])
print (x,"\n")
print(np.roll(x, 1, axis = 1),"\n\n", np.roll(x, -1, axis = 1), "\n\n", np.roll(x, 1, axis = 0),"\n\n", np.roll(x, -1, axis = 0))
print("\n")
print((np.roll(x, 1, axis = 1) + np.roll(x, -1, axis = 1) + np.roll(x, 1, axis = 0) + np.roll(x, -1, axis = 0))/4)