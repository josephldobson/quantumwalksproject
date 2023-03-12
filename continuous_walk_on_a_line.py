import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

C0 = np.array([1, 0])  # |0>
C1 = np.array([0, 1])  # |1>
C00 = np.outer(C0, C0)  # |0><0|
C01 = np.outer(C0, C1)  # |0><1|
C10 = np.outer(C1, C0)  # |1><0|
C11 = np.outer(C1, C1)  # |1><1|

a = 1
b = 1
c = 1
d = -1
Coin_operator = (a*C00 + b*C01 + c*C10 + d*C11) / np.sqrt(2.)

t = 100     # number of random steps
n = 2 * t + 1  # number of positions
gamma = 1./(2.*np.sqrt(.2))

e = 1
f = 1
psi = (e*C0 + f*C1)/np.sqrt(e**2+f**2)

H_operator = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i == j:
            H_operator[i, j] = 2.*gamma
        if i == j-1:
            H_operator[i, j] = -gamma
        if i == j+1:
            H_operator[i, j] = -gamma
Hexp_operator = sp.linalg.expm(- 1j * t * H_operator)

posn_0 = np.zeros(n)
posn_0[t] = 1     # array indexing starts from 0, so index N is the central posn
Psi = np.dot(Hexp_operator, posn_0)
print(Psi)
#psiN = np.linalg.matrix_power(H_operator, t).dot(psi_0)

prob = np.absolute(Psi)
prob = np.square(prob)
print(prob)
X = np.arange(-t,t+1)
plt.plot(X, prob[X])
plt.show()