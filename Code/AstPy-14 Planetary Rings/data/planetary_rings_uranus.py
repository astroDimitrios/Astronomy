import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from random import seed
from random import random

from matplotlib import rc
# You will need latex installed
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

file = '../data/planetary_rings.csv'

df = pd.read_csv(file)

print(df.head())

saturn_rings = df.loc[df['object'] == 'uranus']

saturn_rings = saturn_rings[saturn_rings.ring_name_simp != '1986U2R']

print(saturn_rings)

names = saturn_rings['ring_name_simp'].values
inner = saturn_rings['min'].values
outer = saturn_rings['max'].values
width = (saturn_rings['width lower'] + saturn_rings['width upper'])/2
width = width.values
od = (saturn_rings['od lower'] + saturn_rings['od upper'])/2
od = od.values

# scale alphas based on od
alphas = []
for i in od:
    if np.isnan(i):
        alphas.append(0.025)
    # max alpha is 1
    elif i > 1:
        alphas.append(1)
    # threshold min for it to be visible
    elif i < 0.001:
        alphas.append(0.025)
    elif i < 0.01:
        alphas.append(i*100)
    else:
        alphas.append(i+.2)

print(alphas)

fig = plt.figure(num=1, figsize=(14, 14))
ax = plt.subplot(111)

z=30

rad = 51118/2 # km
circle = Circle((0, 0), rad, color='cornflowerblue', zorder=z, alpha=1, ec='None')
ax.add_artist(circle)
z -= 1

# the first circle will block out the inner part of the second creating a ring
translate = 0
count = 1
no_count = 0
not_plot_text = 'The following rings after $\zeta$ are shown but not labelled: '
for i in range(len(names)):
    if np.isnan(outer[i]):
        outer_ring = inner[i]+width[i]/2
        inner_ring = inner[i]-width[i]/2
    else:
        outer_ring = outer[i]
        inner_ring = inner[i]
    # first white circle 
    circle = Circle((0, 0), inner_ring, color='w', zorder=z, ec='None')
    ax.add_artist(circle)
    z -= 1
    # second ring circle
    if not np.isnan(outer[i]):
        circle = Circle((0, 0), outer_ring, color='steelblue', zorder=z, alpha=alphas[i], ec='None')
        ax.add_artist(circle)
    else:
        circle = Circle((0, 0), outer_ring, color='k', zorder=z, alpha=alphas[i], fc='None')
        ax.add_artist(circle)
    z -=1
    tx = (outer_ring-inner_ring)/2 + inner_ring
    # if names[i] == 'E':
    #     tx = 215000
    # if names[i] not in ['B', 'CD', 'A']:
    #     color='darkgray'
    # else:
    #     color='dimgrey'
    color='dimgray'
    if translate % 2 == 0:
        ty = 0
    else:
        ty = 0
    if (translate == 2) or (translate == 3):
        tx = tx
    if count in [1, 2, 3, 16, 17]:
        if count == 3:
            ty+=500
        ax.text(tx, ty, names[i], fontsize=10, color=color, zorder=32, ha='center', va='center')
    else:
        if count != 15:
            if count != 4:
                if no_count % 4 != 0:
                    not_plot_text += ', '
                else:
                    # not_plot_text += ',\n'
                    not_plot_text += ', '
        else:
            not_plot_text += ',and '
        not_plot_text += names[i]
        no_count += 1
    translate += 1
    count += 1
not_plot_text += '.'
print(not_plot_text)

moonfile = '../data/uranus_moons.csv'
moons = pd.read_csv(moonfile)

moons = moons.loc[moons['Semimajor Axis'] <= moons.loc[moons['Name'] == 'Mab', 'Semimajor Axis'].iloc[0]]

moon_names = moons['Name'].values
moon_A = moons['Semimajor Axis'].values
moon_diam = moons['Mean Radius'].values*2

def moon_pos(A):
    seed(1)
    rands = [random() for i in range(len(A))]
    rands = np.asarray(rands) * 2 * np.pi 
    x = np.multiply(A, np.cos(rands))
    y = np.multiply(A, np.sin(rands))
    return x, y

moon_x, moon_y = moon_pos(moon_A)

for i in range(len(moons)):
    ax.scatter(moon_x[i], moon_y[i], ec='None', s=[moon_diam[i]], color='darkgray', zorder=31)
    if moon_diam[i] < 1:
        shift = moon_diam[i]*1500/2
    elif moon_diam[i] < 20:
        shift = moon_diam[i]*800/2
    elif moon_diam[i] < 50:
        shift = moon_diam[i]*100/2
    elif moon_diam[i] < 120:
        shift = moon_diam[i]*50/2
    else:
        shift = moon_diam[i]*23/2
    textx = moon_x[i]+shift
    texty = moon_y[i]+shift
    if moon_names[i] == 'Cupid':
        textx -= 5000
        texty -= 5000
    if moon_names[i] == 'Desdemona':
        textx -= 18000
    ax.text(textx, texty, moon_names[i], fontsize=8, color='dimgrey', zorder=31)

# # Roche limits fluid

# moons['Density'] = moons['Mass']*10**13/(4/3*np.pi*(moons['Mean Diameter']/2*1000)**3)
# moon_dens = moons['Density'].values # kg/m^3

# density = 687 # kg/m^3

# roche = 2.44*rad*(density/moon_dens)**(1/3)
# for m, r in zip(moon_names, roche):
#     print(m+': {:.1f} km'.format(r))

# # Pan
# circle = Circle((0, 0), roche[0], ls=(0, (3, 5, 1, 5)), color='darkgray', zorder=30, fc='None', alpha=.5)
# ax.add_artist(circle)
# # Mimas
# circle = Circle((0, 0), roche[-5], ls='--', color='darkgray', zorder=30, fc='None')
# ax.add_artist(circle)

# # Roche limit solid for Pan

# roche_pan_rigid = rad*(2*density/moon_dens[0])**(1/3)
# circle = Circle((0, 0), roche_pan_rigid, ls=':', color='darkgray', zorder=30, fc='None', alpha=.5)
# ax.add_artist(circle)

# # End Roche

# # Custom Legend for Roche Limits

# from matplotlib.lines import Line2D
# custom_lines = [Line2D([0], [0], color='darkgray', lw=1, ls=(0, (3, 5, 1, 5)), alpha=.7),
#                 Line2D([0], [0], color='darkgray', lw=1, ls=':', alpha=.7),
#                 Line2D([0], [0], color='darkgray', lw=1, ls='--', alpha=.7)]

# leg = ax.legend(custom_lines, ['Pan Fluid', 'Pan Rigid', 'Mimas Fluid'], numpoints=6, frameon=False, bbox_to_anchor=(0.15, 0.1), title='Roche Limits', fontsize=8)
# plt.setp(leg.get_texts(), color='darkgrey', alpha=.7)
# plt.setp(leg.get_title(), color='darkgrey', alpha=.7)
# leg._legend_box.align='left'

# # End Legend

limit = outer[-1]+10000
ax.set_xlim(-limit*1.01, limit*1.01)
ax.set_ylim(-limit*1.01, limit*1.01)

print('Scale bar in km then AU')
# twice the limit divided by 10 (asuming split 0-1 transAxes coords into 10)
# times by two assuming axhline extends 0.2
scale = limit*1.01*2/10*2
print(scale)
print(scale/(1.496*10**8))
ax.axhline(110000, 0.1, 0.3, color='darkgray', lw=1, zorder=31)
ax.text(0.2, 0.949, '{:,.1f} km'.format(scale), color='darkgray', fontsize=10, zorder=31, transform=ax.transAxes, ha='center')

ax.text(0.87, 0.95, 'Moon sizes are shown relative to each\nother but not to Uranus and the rings.\nOpacity is relative to the optical depth.', color='darkgray', fontsize=8, zorder=31, transform=ax.transAxes, ha='center', multialignment='right', alpha=.7)
ax.text(0.5, 0.01, not_plot_text, color='darkgray', fontsize=10, zorder=31, transform=ax.transAxes, ha='center', multialignment='left', alpha=.7)


ax.set_aspect('equal')
ax.axis('off')

plt.show()
# plt.savefig('../figures/uranus_rings.png', dpi=150, bbox_inches='tight')