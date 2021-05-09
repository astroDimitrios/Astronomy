import numpy as np
import matplotlib.pyplot as plt

from tides import Main, Body

mMars = 0.64171*10**24 # kg
scale = mMars          # so tidal force is per unit mass (has units of acceleration)

# offsets in radians from theta = 0
off_p = 0
off_d = np.pi/4

step = 1/8
rMars = 3389.5 *1000 # m

# initialise Earth and Moon
mars = Main('Mars', mMars, rMars, step, scale)
phobos = Body('Phobos', 10.6*10**15, 9378000, off_p)
deimos = Body('Deimos', 2.4*10**15, 23459000, off_d)

# calculate tidal forces
forces = mars.tides(phobos, deimos)
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
planetCircle = plt.Circle((0,0), 1, color='firebrick', zorder=0)
ax.add_patch(planetCircle)
# plot the arrows
q = ax.quiver(x, y, u, v, zorder=1)

# title and subtitle
title_text = 'Tidal Acceleration from Phobos at {:.0f}'.format(off_p/2/np.pi*360)+r'$^{\circ}$'+'and Deimos at {:.0f}'.format(off_d/2/np.pi*360)+r'$^{\circ}$'
ax.text(0.5, 0.98, title_text, fontsize=20,
     horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
sub_title_text = 'Acc. on an object of unit mass. Arrows to scale not including arrowheads.\n Sizes and distances NTS.'
ax.text(0.5, 0.93, sub_title_text, 
     horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

# # annotate direction of the Body object/s
# ax.annotate("Phobos",
#             xy=(0.5, -0.1), xycoords='data',
#             xytext=(0, -0.1), textcoords='data', ha="center", va="center", size='x-large',
#             arrowprops=dict(arrowstyle="->",
#                             connectionstyle="arc3"),
#             )
# ax.annotate("Deimos",
#             xy=(0.45*np.cos(off_d), 0.45*np.sin(off_d)+0.1), xycoords='data',
#             xytext=(0, 0.1), textcoords='data', ha="center", va="center", size='x-large',
#             arrowprops=dict(arrowstyle="->",
#                             connectionstyle="arc3"),
#             )

# Add circles with labels for Moons instead of annotating
dist_1 = 1.7
dist_2 = 1.4
# Try to get areas somewhat scaled
a_p = 0.0038507109
r_p = np.sqrt(a_p)
a_d = 0.00231042654
r_d = np.sqrt(a_d)
phobosCircle = plt.Circle((dist_1*np.cos(off_p),dist_1*np.sin(off_p)), r_p, color='peru', zorder=1, clip_on=False)
ax.add_patch(phobosCircle)
ax.text(dist_1*np.cos(off_p),dist_1*np.sin(off_p)-.12, 'Phobos', 
     horizontalalignment='center', verticalalignment='center')
deimosCircle = plt.Circle((dist_2*np.cos(off_d),dist_2*np.sin(off_d)), r_d, color='burlywood', zorder=1, clip_on=False)
ax.add_patch(deimosCircle)
ax.text(dist_2*np.cos(off_d),dist_2*np.sin(off_d)-.1, 'Deimos', 
     horizontalalignment='center', verticalalignment='center')

# annotate max vert and hor acceleration components
max_h_ang = thetas[np.where(u == u.max())[0][0]]/2/np.pi*360
t1 = 'Max Hor. Acceleration = {:.4G}'.format(u.max())+r' ms$^{-2}$'+' at angle {:.0f}'.format(max_h_ang)+'$^{\circ}$'
max_v_ang = thetas[np.where(v == v.max())[0][0]]/2/np.pi*360
t2 = 'Max Vert. Acceleration = {:.4G}'.format(v.max())+r' ms$^{-2}$'+' at angle {:.0f}'.format(max_v_ang)+'$^{\circ}$'
t3 = 'Angles measured anticlockwise from + x-axis'
ax.text(0.5, 0.05, t1+'\n'+t2+'\n'+t3, 
     horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

# Mars label
ax.text(0, 0, 'Mars', fontsize=20,
     horizontalalignment='center', verticalalignment='center')

# turn axis off
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')

# plt.show()
file_name = 'Tides_Mars_{:.0f}_{:.0f}.png'.format(off_p, off_d)
plt.savefig(file_name, dpi=150)
# file_name_tight = 'Tides_Mars_{:.0f}_{:.0f}_tight.png'.format(off_p, off_d)
# plt.savefig(file_name_tight, dpi=150, bbox_inches="tight")