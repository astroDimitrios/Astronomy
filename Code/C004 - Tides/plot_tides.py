import numpy as np
import matplotlib.pyplot as plt

from tides import Main, Body

scale = 5.972*10**24    # mass of Earth so tidal force is per unit mass (has units of acceleration)

# offsets in radians from theta = 0
off_moon = 0

step = 1/8
rEarth = 6371000

# initialise Earth and Moon
earth = Main('Earth', 5.972*10**24, rEarth, step, scale)
moon = Body('Moon', 7.34767309*10**22, 384400000, off_moon)

# calculate tidal forces
forces = earth.tides(moon)
# print(forces)

# x and y values for arrow tails
thetas = np.arange(0, 2*np.pi, step*np.pi)
x = np.cos(thetas)   # scaled to rEarth
y = np.sin(thetas)   # scaled to rEarth

# length of arrows set to tidal acceleration components
u = forces[2]
v = forces[4]

fig = plt.figure(num=1, figsize=(10, 10))
ax = fig.add_subplot(111, label="ax")

# plot the planet circle
planetCircle = plt.Circle((0,0), 1, color='lightskyblue', zorder=0)
ax.add_patch(planetCircle)
# plot the arrows
q = ax.quiver(x, y, u, v, zorder=1)

# title and subtitle
title_text = 'Tidal Acceleration from the Moon at {:.0f}'.format(off_moon)+'$^{\circ}$'
ax.text(0.5, 1, title_text, fontsize=20,
     horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
sub_title_text = 'Acc. on an object of unit mass. Arrows to scale not including arrowheads.'
ax.text(0.5, 0.95, sub_title_text, 
     horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

# annotate direction of the Body object/s
ax.annotate("Moon",
            xy=(0.5, 0), xycoords='data',
            xytext=(0, 0), textcoords='data', ha="center", va="center", size='x-large',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )

# annotate max vert and hor acceleration components
max_h_ang = thetas[np.where(u == u.max())[0][0]]/2/np.pi*360
t1 = 'Max Hor. Acceleration = ${:.4G}'.format(u.max())+r'\ ms^{-2}$'+' at angle {:.0f}'.format(max_h_ang)+'$^{\circ}$'
max_v_ang = thetas[np.where(v == v.max())[0][0]]/2/np.pi*360
t2 = 'Max Vert. Acceleration = ${:.4G}'.format(v.max())+r'\ ms^{-2}$'+' at angle {:.0f}'.format(max_v_ang)+'$^{\circ}$'
t3 = 'Angles measured counterclockwise from + x-axis'
ax.text(0.5, 0.05, t1+'\n'+t2+'\n'+t3, 
     horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

# turn axis off
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')

# plt.show()
file_name = 'Tides_Moon_{:.0f}.png'.format(off_moon)
plt.savefig(file_name, dpi=150)