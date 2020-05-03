# # © Dimitrios Theodorakis GNU General Public License v3.0 https://github.com/DimitriosAstro/Astronomy
# Adapted from work by	
# Tom Aldcroft, Tom Robitaille, Brian Refsdal, Gus Muench, Smithsonian Astrophysical Observatory
# https://python4astronomers.github.io/index.html

from numpy.random import default_rng
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# from matplotlib.animation import PillowWriter

# Define properties of the "bouncing balls"
n = 10
rng = default_rng()
pos = (20 * rng.random(n*2) - 10).reshape(n, 2)
vel = (0.3 * rng.random(size=n*2)).reshape(n, 2)
sizes = 100 * rng.random(n) + 100

colors = rng.random([n, 4])

# setup initial plot
fig = plt.figure(num=1, figsize=(5,5))
ax = plt.axes(xlim=(-n,n), ylim=(-n,n))
circles = plt.scatter(pos[:,0], pos[:,1], marker='o', s=sizes, c=colors)

def animate(i):
    global pos
    pos += vel
    bounce = abs(pos) > 10      # Find balls that are outside walls
    vel[bounce] = -vel[bounce]  # Bounce if outside the walls
    circles.set_offsets(pos)    # Change the positions
    return circles

# make animation with 100 frames and interval in ms
anim = animation.FuncAnimation(fig, animate, frames=500, interval=100)

# imagemagick is slow and needs to be installed to save the gif
# anim.save('bounce.gif', writer='imagemagick', fps=30)
plt.show()