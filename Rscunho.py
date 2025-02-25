import numpy as np
import matplotlib.pyplot as plt
import time


#Constants
M = int(input("Tamanho da matriz ")) #tamanho do dominio #250
V = 1.0 #potêncial
target = 1e-5 #mínimo

phi = np.zeros([M, M], float)
phi[0, :] = V
phi[M - 1, :] = V
phi[:, 0] = V
phi[:, M - 1] = V

phi[125:128, 125:128] = -V
phiprime = np.empty([M, M], float)

phi[125:128, 125:128] = -V

delta = 1.0

phiprime[0, :] = phi[0, :]
phiprime[M - 1, :] = phi[M - 1, :]
phiprime[:, 0] = phi[:, 0]
phiprime[:, M - 1] = phi[:, M - 1]
phiprime[125:128, 125:128] = phi[125:128, 125:128]

tic = time.time()

while delta > target:

    phiprime = (np.roll(phi, 1, axis = 0) + np.roll(phi, -1, axis = 0) + np.roll(phi, 1, axis = 1) + np.roll(phi, -1, axis = 1))/4

    phiprime[0, :] = phi[0, :]
    phiprime[M - 1, :] = phi[M - 1, :]
    phiprime[:, 0] = phi[:, 0]
    phiprime[:, M - 1] = phi[:, M - 1]
    phiprime[125:128, 125:128] = phi[125:128, 125:128]

    delta = np.max(np.abs(phi - phiprime))
    phi, phiprime = phiprime, phi

print(time.time()-tic)
print(len(phiprime))
plt.imshow(phi)
plt.colorbar()
plt.show()