import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation
import FuncAnimation

def Laplaciano(phi, phiprime, target, n):
  phiprime = (np.roll(phi, 1, axis = 0) + np.roll(phi, -1, axis = 0) + np.roll(phi, 1, axis = 1) + np.roll(phi, -1, axis = 1))/4
  phiprime[0, :, n] = phi[0, :, n]
  phiprime[M - 1, :, n] = phi[M - 1, :, n]
  phiprime[:, 0, n] = phi[:, 0, n]
  phiprime[:, M - 1, n] = phi[:, M - 1, n]
  phiprime[(M//4):(((3*M)//4)), (M//4):(((3*M)//4)), n] = phi[(M//4):(((3*M)//4)), (M//4):(((3*M)//4)), n]
  delta = np.max(np.abs(phi - phiprime))
  phi, phiprime = phiprime, phi
  if delta > target:
    return (phi, phiprime)
  else:
    return print("Vc n deveria ler isso")

def Humilhacao(phi, phiprime, target, T, M):
  for n in range(T):
    phi, phiprime = Laplaciano(phi, phiprime, target, n)
    if n == (T-2):
      T = M + T
      nova_dimensao = (M, M, (T))
      nova_matriz = np.zeros(nova_dimensao, dtype=phi.dtype)
      # Copia os valores da matriz original para a nova matriz
      nova_matriz[:phi.shape[0], :phi.shape[1], :phi.shape[2]] = phi
      phi = nova_matriz

      nova_matriz = np.zeros(nova_dimensao, dtype=phiprime.dtype)
      # Copia os valores da matriz original para a nova matriz
      nova_matriz[:phiprime.shape[0], :phiprime.shape[1], :phiprime.shape[2]] = phiprime
      phiprime = nova_matriz


Cronos = []
M = 250
T = M
V = 1.0
target = 1e-5


phi = np.zeros([M, M, T])

phi[0, :, 0] = -V
phi[M - 1, :,0] = -V
phi[:, 0, 0] = -V
phi[:, M - 1, 0] = -V
phi[(M//4):(((3*M)//4)), (M//4):(((3*M)//4)), 0] = V


phiprime = np.empty([M, M, M], float)
n = 0
delta = 1.0

phiprime[0, :, 0] = phi[0, :, 0]
phiprime[M - 1, :, 0] = phi[M - 1, :, 0]
phiprime[:, 0,0] = phi[:, 0, 0]
phiprime[:, M - 1, 0] = phi[:, M - 1, 0]
phiprime[(M//4):((3*M)//4), (M//4):((3*M)//4), 0] = phi[(M//4):((3*M)//4), (M//4):((3*M)//4), 0]

plt.imshow(phi[:,:,0])
plt.colorbar()
plt.show()

Humilhacao(phi, phiprime, target, T, M)





plt.imshow(phi[:,:,0])
plt.colorbar()
plt.show()

plt.imshow(phi[:,:,1])
plt.colorbar()
plt.show()

plt.imshow(phi[:,:,(T-1)//2])
plt.colorbar()
plt.show()

plt.imshow(phi[:,:,(T-1)])
plt.colorbar()
plt.show()
print(T)