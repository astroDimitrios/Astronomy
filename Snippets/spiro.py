import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk
from matplotlib.collections import LineCollection

t_end = 10*np.pi
t_step = 10000
t = np.linspace(0, t_end, t_step)

R = 3
r = 2
a = 3

# http://www.mathematische-basteleien.de/spirographs.htm
# Epicycloid

x = (R+r)*np.cos(r/R*t)-a*np.cos((1+r/R)*t)
y = (R+r)*np.sin(r/R*t)-a*np.sin((1+r/R)*t)

plt.style.use("cyberpunk")
fig = plt.figure(num=1, figsize=(10,10), dpi=150)
ax = plt.subplot()
scale = 1.05
ax.set_xlim(np.min(x)*scale, np.max(x)*scale)
ax.set_ylim(np.min(y)*scale, np.max(y)*scale)

from gradient import polylinear_gradient

colour_grad = polylinear_gradient(['#9D00FF', '#FF0099', '#FD1C03'], len(t))
colour_g = np.array(list(zip(colour_grad['r'], colour_grad['g'], colour_grad['b'])))
if len(colour_g) != len(t):
    row = colour_g[-1, :]
    colour_g = np.vstack([colour_g, row])
colours = np.zeros((len(t), 4))
colours[:, 0:3] = colour_g/255
alpha = np.ones((1, len(t)))
colours[:, 3] = alpha

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
# norm = plt.Normalize(t.min(), t.max())
# lc = LineCollection(segments, cmap='viridis', norm=norm)
# lc.set_array(t)
lc = LineCollection(segments, color=colours)
lc.set_linewidth(2)
line = ax.add_collection(lc)

def make_glow(segments, colours, width, scale, n=10):
    new_colours = colours
    new_a = np.linspace(0.3, 0.1, n)
    for i in range(1, n):
        new_colours[:, 3] = colours[:, 3]*new_a[i-1]
        new_lc = LineCollection(segments, color=colours)
        new_lc.set_linewidth(width+i*scale)
        new_lc.set_zorder(-i)
        ax.add_collection(new_lc)
        # print('here')

make_glow(segments, colours, 2, 1, 50)

# ax.plot(x, y)


# mplcyberpunk.add_glow_effects()
# mplcyberpunk.make_lines_glow()
# mplcyberpunk.add_underglow()

ax.axis('off')
# fig.patch.set_facecolor('w')
# print(ax.collections)

plt.show()