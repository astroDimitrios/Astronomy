""" snippet to create a fading line plot with Matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

r = 1
theta = np.arange(0, 2*np.pi, 0.1)
x = r*np.cos(theta)
y = r*np.sin(theta)

# intitial colour rgb and alpha
colour = np.array([63, 191, 63])/255
alpha = 1

def fade_line(x, y, colour, alpha):
    # make LineCollection
    Npts = len(x)

    # create colours array
    colours = np.zeros((Npts, 4))
    colours[:, 0:3] = colour
    colours[:, 3] = alpha*np.linspace(0, 1, Npts)

    # N-1 segments for N points
    # (x, y) start point and (x2, y2) end point
    segments = np.zeros((Npts-1, 2, 2))
    # segment start values - slice of last value
    segments[:, 0, 0] = x[:-1]
    segments[:, 0, 1] = y[:-1]
    # segements end values - slice of first value
    segments[:, 1, 0] = x[1:]
    segments[:, 1, 1] = y[1:]

    lc = LineCollection(segments, color=colours)
    return lc

# show some example data
f, ax = plt.subplots()
lc = fade_line(x, y, colour, alpha)
ax.add_collection(lc)

ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal')
ax.set_axis_off()

ax.plot(0, 0, marker='*', markersize='10', color='gold', alpha=.8,
    markeredgecolor = 'none')
ax.plot(x[-1], y[-1], marker='.', markersize='15', color='k', 
    alpha=1, markeredgecolor = 'none')
    
plt.show()