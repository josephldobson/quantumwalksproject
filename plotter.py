from discrete_walk_on_a_line import *
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

with open("simulation/simple200", "r") as fp:
    plots = json.load(fp)
max_frames = len(plots)
width = len(plots[0][0])

plt.style.use('seaborn-pastel')
fig = plt.figure()
ax = plt.axes(xlim=(0, width), ylim=(0, 0.2))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])

    return line,
def animate(i):
    X = plots[i][0]
    Y = plots[i][1]

    line.set_data(X, Y)

    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=max_frames, interval=1, blit=True)


anim.save(f"simple{max_frames*2}.gif", writer='imagemagick')