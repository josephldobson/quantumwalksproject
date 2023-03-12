import numpy as np
import matplotlib.pyplot as plt

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

N = 1000     # number of random steps
P = 2*N+1  # number of positions

e = 1
f = 1
psi = (e*C0 + f*C1*1j) / np.sqrt(e**2+f**2)


shift_up = np.roll(np.identity(P), 1, axis=0)
shift_down = np.roll(np.identity(P), -1, axis=0)
S_operator = np.kron(shift_up, C00) + np.kron(shift_down, C11)
U_operator = S_operator.dot(np.kron(np.identity(P), Coin_operator))

posn_0 = np.zeros(P)
posn_0[N] = 1     # array indexing starts from 0, so index N is the central posn

psi_0 = np.kron(posn_0, psi)

psiN = np.linalg.matrix_power(U_operator, N).dot(psi_0)

prob = np.empty(P)
for k in range(P):
    posn = np.zeros(P)
    posn[k] = 1
    M_hat_k = np.kron(np.outer(posn, posn), np.identity(2))
    proj = M_hat_k.dot(psiN)
    prob[k] = proj.dot(proj.conjugate()).real

X = np.arange(P)[0::2]

plt.plot(X, prob[X])
plt.show()