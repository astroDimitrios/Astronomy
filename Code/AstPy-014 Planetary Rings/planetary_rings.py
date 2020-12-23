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

# get data
file = './data/planetary_rings.csv'
df = pd.read_csv(file)
print(df.head())

# get saturn
saturn_rings = df.loc[df['object'] == 'saturn']
print(saturn_rings)

# get names, ring radii, and optical densities
names = saturn_rings['ring_name_simp'].values
inner = saturn_rings['min'].values
outer = saturn_rings['max'].values
od = (saturn_rings['od lower'] + saturn_rings['od upper'])/2
od = od.values

# scale alphas based on od
alphas = []
for i in od:
    # max alpha is 1
    if i > 1:
        alphas.append(1)
    # threshold min for it to be visible
    elif i < 0.001:
        alphas.append(0.025)
    elif i < 0.01:
        alphas.append(i*100)
    else:
        alphas.append(i*1.8)

fig = plt.figure(num=1, figsize=(14, 14))
ax = plt.subplot(111)

# zorder counter
z=30

# plot the planet
rad = 120536/2 # km
circle = Circle((0, 0), rad, color='gold', zorder=z, alpha=1, ec='None')
ax.add_artist(circle)
z -= 1

# the first circle will block out the inner part of the second creating a ring
translate = 0
for i in range(len(names)):
    # first white circle 
    circle = Circle((0, 0), inner[i], color='w', zorder=z, ec='None')
    ax.add_artist(circle)
    z -= 1
    # second ring circle
    circle = Circle((0, 0), outer[i], color='goldenrod', zorder=z, alpha=alphas[i], ec='None')
    ax.add_artist(circle)
    z -=1
    # fix name locations
    # swap every other to be zig zagged not straight line and fix E label pos
    tx = (outer[i]-inner[i])/2 + inner[i]
    if names[i] == 'E':
        tx = 215000
    if names[i] not in ['B', 'CD', 'A']:
        color='darkgray'
    else:
        color='dimgrey'
    if translate % 2 == 0:
        ty = 1000*3
    else:
        ty = -1000*3
    ax.text(tx, ty, names[i], fontsize=10, color=color, zorder=32, ha='center', va='center')
    translate += 1

# load moon data
moonfile = './data/saturn_moons.csv'
moons = pd.read_csv(moonfile)

moons = moons.loc[moons['Semimajor Axis'] <= moons.loc[moons['Name'] == 'Enceladus', 'Semimajor Axis'].iloc[0]]

moon_names = moons['Name'].values
moon_A = moons['Semimajor Axis'].values
moon_diam = moons['Mean Diameter'].values

# rand pos for moons so that they're not all along a straight line
def moon_pos(A):
    seed(1)
    rands = [random() for i in range(len(A))]
    rands = np.asarray(rands) * 2 * np.pi 
    x = np.multiply(A, np.cos(rands))
    y = np.multiply(A, np.sin(rands))
    return x, y

moon_x, moon_y = moon_pos(moon_A)

# plot moons and shift the text based on the diameter
for i in range(len(moons)):
    ax.scatter(moon_x[i], moon_y[i], ec='None', s=[moon_diam[i]], color='darkgray', zorder=31)
    if moon_diam[i] < 1:
        shift = moon_diam[i]*1500
    elif moon_diam[i] < 20:
        shift = moon_diam[i]*800
    elif moon_diam[i] < 50:
        shift = moon_diam[i]*100
    elif moon_diam[i] < 120:
        shift = moon_diam[i]*50
    else:
        shift = moon_diam[i]*23
    textx = moon_x[i]+shift
    texty = moon_y[i]+shift
    ax.text(textx, texty, moon_names[i], fontsize=8, color='dimgrey', zorder=31)

# Roche limits fluid

moons['Density'] = moons['Mass']*10**13/(4/3*np.pi*(moons['Mean Diameter']/2*1000)**3)
moon_dens = moons['Density'].values # kg/m^3

density = 687 # kg/m^3

roche = 2.44*rad*(density/moon_dens)**(1/3)
for m, r in zip(moon_names, roche):
    print(m+': {:.1f} km'.format(r))

# Pan
circle = Circle((0, 0), roche[0], ls=(0, (3, 5, 1, 5)), color='darkgray', zorder=30, fc='None', alpha=.5)
ax.add_artist(circle)
# Mimas
circle = Circle((0, 0), roche[-5], ls='--', color='darkgray', zorder=30, fc='None')
ax.add_artist(circle)

# Roche limit solid for Pan

roche_pan_rigid = rad*(2*density/moon_dens[0])**(1/3)
circle = Circle((0, 0), roche_pan_rigid, ls=':', color='darkgray', zorder=30, fc='None', alpha=.5)
ax.add_artist(circle)

# End Roche

# Custom Legend for Roche Limits

from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color='darkgray', lw=1, ls=(0, (3, 5, 1, 5)), alpha=.7),
                Line2D([0], [0], color='darkgray', lw=1, ls=':', alpha=.7),
                Line2D([0], [0], color='darkgray', lw=1, ls='--', alpha=.7)]

leg = ax.legend(custom_lines, ['Pan Fluid', 'Pan Rigid', 'Mimas Fluid'], numpoints=6, frameon=False, bbox_to_anchor=(0.15, 0.1), title='Roche Limits', fontsize=8)
plt.setp(leg.get_texts(), color='darkgrey', alpha=.7)
plt.setp(leg.get_title(), color='darkgrey', alpha=.7)
leg._legend_box.align='left'

# End Legend

limit = outer[-2]+80000
ax.set_xlim(-limit*1.01, limit*1.01)
ax.set_ylim(-limit*1.01, limit*1.01)

# make the scale bar
print('Scale bar in km then AU')
# twice the limit divided by 10 (asuming split 0-1 transAxes coords into 10)
# times by two assuming axhline extends 0.2
scale = limit*1.01*2/10*2
print(scale)
print(scale/(1.496*10**8))
ax.axhline(215000, 0.1, 0.3, color='darkgray', lw=1)
ax.text(0.2, 0.9, '{:,.0f} km'.format(scale), color='darkgray', fontsize=10, zorder=31, transform=ax.transAxes, ha='center')

ax.text(0.87, 0.03, 'The E ring extends to 450,000 km.\nMoon sizes are shown relative to each\nother but not to Saturn and the rings.\nOpacity is relative to the optical depth.', color='darkgray', fontsize=8, zorder=31, transform=ax.transAxes, ha='center', multialignment='right', alpha=.7)

ax.set_aspect('equal')
ax.axis('off')

plt.show()
# plt.savefig('saturn_rings_roche.png', dpi=150, bbox_inches='tight')