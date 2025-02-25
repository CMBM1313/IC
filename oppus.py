import numpy as np
import matplotlib.pyplot as plt
import time


M = 100
V = -1
target = 1e-5

phi = np.zeros([M, M], float)
phi[50, 50] = V
phi[49, 49] = V
phi[49, 50] = V
phi[50, 49] = V
phi[48, 48] = V
phi[51, 51] = V
phi[52, 52] = V
phi[47, 47] = V
phi[49, 48] = V
phi[50, 48] = V
phi[51, 48] = V
phi[52, 47] = V
phi[49, 47] = V
phi[50, 47] = V
phi[48, 49] = V
phi[47, 49] = V
phi[51, 49] = V
phi[52, 49] = V
phi[52, 49] = V
phi[48, 50] = V
phi[47, 50] = V
phi[51, 50] = V
phi[52, 50] = V
phi[49, 51] = V
phi[48, 51] = V
phi[50, 51] = V
phi[47, 52] = V
phi[49, 52] = V
phi[50, 52] = V

phi[0, :] = -(V)
phi[M-1, :] = -(V)
phi[:, 0] = -(V)
phi[:, M-1] = -(V)

phiprime = np.empty([M, M], float)
delta = 1


tic = time.time()

while delta > target:
    phiprime = (np.roll(phi, 1, axis=0) + np.roll(phi, -1, axis=0) + np.roll(phi, 1, axis=1) + np.roll(phi, -1,axis=1))/4
    phiprime[0, :] = phi[0, :]
    phiprime[M - 1, :] = phi[M - 1, :]
    phiprime[:, 0] = phi[:, 0]
    phiprime[:, M - 1] = phi[:, M - 1]

    delta = np.max(np.abs(phi - phiprime))
    phi, phiprime = phiprime, phi

print(time.time()-tic)
plt.imshow(phi)
plt.gray()
plt.show()
