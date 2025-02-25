import numpy as np
import matplotlib.pyplot as plt
import time


#Constants
M = 250 #tamanho do dominio
V = 1.0 #potêncial
E = -1.0
target = 1e-5 #mínimo

phi = np.zeros([M + 1, M + 1], float)
phi[0, :] = V
phi[M, :] = V
phi[:, 0] = V
phi[:, M] = V
phiprime = np.empty([M + 1, M + 1], float)

phiprime[125, 125] = E
phiprime[125, 126] = E
phiprime[125, 127] = E
phiprime[126, 125] = E
phiprime[126, 126] = E
phiprime[126, 127] = E
phiprime[127, 125] = E
phiprime[127, 126] = E
phiprime[127, 127] = E


#Main loop
delta = 1.0

phiprime[0, :] = phi[0, :]
phiprime[M, :] = phi[M, :]
phiprime[:, 0] = phi[:, 0]
phiprime[:, M] = phi[:, M]



tic = time.time()

while delta > target:

    phiprime = (np.roll(phi, 1, axis = 0) + np.roll(phi, -1, axis = 0) + np.roll(phi, 1, axis = 1) + np.roll(phi, -1, axis = 1))/4

    phiprime[0, :] = phi[0, :]
    phiprime[M, :] = phi[M, :]
    phiprime[:, 0] = phi[:, 0]
    phiprime[:, M] = phi[:, M]

    delta = np.max(np.abs(phi - phiprime))
    phi, phiprime = phiprime, phi

print(time.time()-tic)
plt.imshow(phi)
plt.gray()
plt.show()
