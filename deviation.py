from matplotlib import rc
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import json
import numpy as np

params = {"ytick.color" : "black",
          "xtick.color" : "black",
          "axes.labelcolor" : "black",
          "axes.edgecolor" : "black",
          "text.usetex" : True,
          "font.family" : "serif",
          "font.serif" : ["Computer Modern Serif"]}

X = [2*i for i in range(50)]
Y1 = [np.sqrt(i) for i in X]
Y2 = [0.54*i for i in X]


plt.style.use('seaborn-pastel')
plt.rcParams.update(params)
fig = plt.figure()
fig.patch.set_facecolor('#F2F2F2')
plt.scatter(X, Y1, label='SRW')
plt.scatter(X, Y2, label='QW')


plt.xlabel("Time")
plt.ylabel("Deviation")
plt.legend()

plt.savefig('foo.png')
