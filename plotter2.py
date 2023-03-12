from matplotlib import rc
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import json

params = {"ytick.color" : "black",
          "xtick.color" : "black",
          "axes.labelcolor" : "black",
          "axes.edgecolor" : "black",
          "text.usetex" : True,
          "font.family" : "serif",
          "font.serif" : ["Computer Modern Serif"]}

with open("simulation/simple100", "r") as fp:
    plots1 = json.load(fp)
    print(len(plots1))

with open("simulation/quantum100", "r") as fp:
    plots2 = json.load(fp)
    print(len(plots2))

frame_num = min(len(plots1), len(plots2))
width = len(plots1[0][0])


plt.style.use('seaborn-pastel')
plt.rcParams.update(params)

fig = plt.figure()
fig.patch.set_facecolor('#F2F2F2')
fig.set_dpi(400)
ax = plt.axes(xlim=(-int(width/2), int(width/2)), ylim=(0, 0.2))

#plt.title("Simple Random Walk vs Quantum Walk")
#plt.xlabel("Position",fontsize = 16)
#plt.ylabel("Probability",fontsize = 16)
plt.title("Simple Random Walk vs Quantum Walk")


ticks = [0,0.1,0.2]
plt.yticks(ticks)


time_text = ax.text(0.05, 0.95,'',horizontalalignment='left',verticalalignment='top', transform=ax.transAxes)

line1, = ax.plot([], [], lw=2, label = 'SRW')
line2, = ax.plot([], [], lw=2, label = 'QW')
leg = ax.legend();


def init():
    line1.set_data([], [])
    line2.set_data([], [])
    time_text.set_text('steps = 0')

    return line1, line2, time_text

def animate(i):
    X1 = plots1[i][0]
    X1 = [i - int(width/2) for i in X1]
    Y1 = plots1[i][1]

    X2 = plots2[i][0]
    X2 = [i - int(width/2) for i in X2]
    Y2 = plots2[i][1]

    line1.set_data(X1, Y1)
    line2.set_data(X2, Y2)

    time_text.set_text(f'steps = {2*i}')  # <<<<<Here. This doesn't work

    if i == 12: fig.savefig(f'fig{i}.png')
    if i == 24: fig.savefig(f'fig{i}.png')
    if i == 36: fig.savefig(f'fig{i}.png')
    if i == 48: fig.savefig(f'fig{i}.png')

    return line1, line2, time_text

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=frame_num, interval=1, blit=True)


anim.save(f"simple{frame_num*2}.gif", writer='imagemagick', fps=10)