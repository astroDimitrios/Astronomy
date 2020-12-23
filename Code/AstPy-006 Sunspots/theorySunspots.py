import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.legend_handler import HandlerLine2D

## Visualising theoretical sunspots

# Visualise a sunspot travelling across a unit circle
t = np.linspace(0, 1, num=18)
theta = np.linspace(0, np.pi, 18)
r = 1.
x = np.cos(theta)*r
# Shift the x values to all be positive and always increasing like in our images
shiftx = []
for i in x:
    if i < 0:
        shiftx.append(r+abs(i))
    else:
        shiftx.append(r-abs(i))
shiftx = np.asarray(shiftx)

# Print the polyfit data - change j to see how the number of points supplied to the fit
# changes the goodness of the fit
print('Polyfit power 3 All data')
print(np.polyfit(t, shiftx, 3, full=True))
j = 5
print('\n x up to entry {}'.format(j))
print(shiftx[:j])
print('\n Polyfit power 3 with cut x data from start')
print(np.polyfit(t[:j], shiftx[:j], 3, full=True))
print('\n Polyfit power 2 with cut x data from start')
print(np.polyfit(t[:j], shiftx[:j], 2, full=True))
print('\n Polyfit power 1 with center data only')
print(np.polyfit(t[7:-7], shiftx[7:-7], 1, full=True))

# Plot the change in x over time
fig = plt.figure(1)
plt.scatter(t, shiftx, color='k', zorder=1)
# Get and plot the polyfit data
p, res, rank, sing, rcond = np.polyfit(t, shiftx, 3, full=True)
p2 = np.polyfit(t, shiftx, 2)
p3 = np.polyfit(t, shiftx, 1)
p4 = np.polyfit(t[7:-7], shiftx[7:-7], 1)
theory = p[0]*t**3 + p[1]*t**2 + p[2]*t +p[3]
theory2 = p2[0]*t**2 + p2[1]*t +p2[2]
theory3 = p3[0]*t + p3[1]
theory4 = p4[0]*t + p4[1]
plt.plot(t, theory, '-', color='orange', alpha=.5, zorder=0, label='3')
plt.plot(t, theory2, '--', color='g', alpha=.5, zorder=0, dashes=[6,2,6,6], label='2')
plt.plot(t, theory3, '--', color='r', alpha=.5, zorder=0, dashes=[6,6,6,2], label='1')
plt.plot(t, theory4, '-', color='r', alpha=.5, zorder=0, label='1 center')
plt.xlabel('t')
plt.ylabel('x')
legend = plt.legend(handlelength=2, frameon=False)
# Shift the legend text to center aligned
renderer = fig.canvas.get_renderer()
shift = max([t.get_window_extent(renderer).width for t in legend.get_texts()])/2
for text in legend.get_texts():
    text.set_ha('center')
    text.set_position((shift,0))

# Plot the path of the sunspot on the face of the sun
fig = plt.figure(2)
ax = fig.add_subplot()
circle = plt.Circle((1,1), 1.035, color='gold', zorder=0)
ax.add_artist(circle)
# ax.scatter(shiftx[1:-1], np.ones(len(shiftx[1:-1])), color='k', zorder=1)
ax.scatter(shiftx, np.ones(len(shiftx)), color='k', zorder=1)
ax.set_ylim(-.2,2.2)
ax.set_aspect('equal')
ax.axis('off')

# Top view of Figure 2
fig = plt.figure(3)
ax = fig.add_subplot()
circle = plt.Circle((1,2), 1.035, color='gold', zorder=0)
ax.add_artist(circle)
x2 = 1 + np.cos(theta)*r
y2 = 2 - np.sin(theta)*r
ax.scatter(x2, y2, color='k', zorder=1)
ax.set_ylim(0.8,3.2)
ax.set_aspect('equal')
ax.axis('off')

# Plot a figure with all three subplots
fig = plt.figure(4, figsize=(15,10))
G = gridspec.GridSpec(1,3)
ax1 = plt.subplot(G[0:2])
ax2 = plt.subplot(G[2])

ax1.scatter(t, shiftx-1, color='k', zorder=1)
ax1.plot(t, theory-1, '-', color='orange', alpha=.5, zorder=0, label='Fit Power 3')
ax1.plot(t, theory2-1, '--', color='g', alpha=.5, zorder=0, dashes=[6,2,6,6], label='Fit Power 2')
ax1.plot(t, theory3-1, '--', color='r', alpha=.5, zorder=0, dashes=[6,6,6,2], label='Fit Power 1')
ax1.plot(t, theory4-1, '-', color='r', alpha=.5, zorder=0, label='Fit Power 1\nCentre Values')
ax1.set_xlabel('time', fontsize=16)
ax1.set_ylabel('displacement', labelpad=10, fontsize=16)
ax1.spines['bottom'].set_position('zero')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.tick_params(axis='x', which='both', bottom=False)
ax1.tick_params(axis='y', labelsize=16)
ax1.set_yticks([-1,0,1])
ax1.set_yticklabels(['-A', 0, '+A'])
ax1.xaxis.set_major_formatter(plt.NullFormatter())
ax1.set_xlim(0, 1)
ax1.xaxis.set_label_coords(0.75, 0.47) 
h, l = ax1.get_legend_handles_labels()
kw = dict(frameon=False, fontsize=14, handlelength=2)    
leg1 = ax1.legend(h[:3],l[:3], loc=(0.22, .82),**kw)
leg2 = ax1.legend(h[3:],l[3:], loc=(0.2, .75),**kw)
plt.setp(leg2.get_texts(), multialignment='center')
ax1.add_artist(leg1)

size = 20
circle1 = plt.Circle((1,1), 1.035, color='gold', zorder=0, clip_on=False)
ax2.add_artist(circle1)
ax2.scatter(shiftx, np.ones(len(shiftx)), color='k', zorder=2, s=size)
ax2.plot(shiftx, np.ones(len(shiftx)), '--', color='grey', zorder=1, alpha=.5, linewidth=1)
circle2 = plt.Circle((1,2+2), 1.035, color='gold', zorder=0, clip_on=False)
ax2.add_artist(circle2)
y2off = y2+2
ax2.scatter(x2, y2off, color='k', zorder=2, s=size)
ax2.plot(x2, y2off, '--', color='grey', zorder=1, alpha=.5, linewidth=1)
for i in range(len(shiftx)):
    ax2.vlines(shiftx[i], 1, y2off[i], colors='grey', linestyles='dashed', alpha=.5, linewidth=.5)
ax2.set_ylim(-.2, 5.2)
ax2.set_aspect('equal')
ax2.axis('off')

plt.show()

## Reference

# scienceinschool - Measuring Solar Rotation - https://www.scienceinschool.org/content/sunspots-rotating-sun