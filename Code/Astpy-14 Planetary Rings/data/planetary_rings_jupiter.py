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

file = 'planetary_rings.csv'

df = pd.read_csv(file)

print(df.head())

saturn_rings = df.loc[df['object'] == 'jupiter']

print(saturn_rings)

names = saturn_rings['ring_name_simp'].values
inner = saturn_rings['min'].values
outer = saturn_rings['max'].values
# width = (saturn_rings['width lower'] + saturn_rings['width upper'])/2
# width = width.values
od = (saturn_rings['od lower'] + saturn_rings['od upper'])/2
od = od.values

# scale alphas based on od
# alphas = []
# for i in od:
#     # max alpha is 1
#     if i > 1:
#         alphas.append(1)
#     # threshold min for it to be visible
#     elif i < 0.001:
#         alphas.append(0.025)
#     elif i < 0.01:
#         alphas.append(i*100)
#     else:
#         alphas.append(i*1.8)
from sklearn.preprocessing import MinMaxScaler
min_max_scaler = MinMaxScaler(feature_range=(.05, .7))
alphas = min_max_scaler.fit_transform(np.reshape(od, (-1, 1)))
alphas = alphas.flatten()
alphas[-1] = 0.04
print(alphas)

fig = plt.figure(num=1, figsize=(14, 14))
ax = plt.subplot(111)

z=30

rad = 142984/2 # km
circle = Circle((0, 0), rad, color='goldenrod', zorder=z, alpha=1, ec='None')
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
    circle = Circle((0, 0), outer[i], color='peru', zorder=z, alpha=alphas[i], ec='None')
    ax.add_artist(circle)
    z -=1
    tx = (outer[i]-inner[i])/2 + inner[i]
    if names[i] == 'M':
        tx += 500
    if names[i] not in ['B', 'CD', 'A', 'M']:
        color='darkgray'
    else:
        color='dimgrey'
    if translate % 2 == 0:
        ty = 0
    else:
        ty = 0
    ax.text(tx, ty, names[i], fontsize=10, color=color, zorder=32, ha='center', va='center')
    translate += 1

moonfile = 'jupiter_moons.csv'
moons = pd.read_csv(moonfile)

moons = moons.loc[moons['Semimajor Axis'] <= moons.loc[moons['Name'] == 'Thebe', 'Semimajor Axis'].iloc[0]]

moon_names = moons['Name'].values
moon_A = moons['Semimajor Axis'].values
moon_diam = moons['Mean Radius'].values *2
print(moon_diam)

def moon_pos(A):
    seed(3)
    rands = [random() for i in range(len(A))]
    rands = np.asarray(rands) * 2 * np.pi 
    x = np.multiply(A, np.cos(rands))
    y = np.multiply(A, np.sin(rands))
    return x, y

moon_x, moon_y = moon_pos(moon_A)

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
        shift = moon_diam[i]*30
    textx = moon_x[i]+shift
    texty = moon_y[i]+shift
    if moon_names[i] == 'Adrastea':
        textx -= 30000 
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

limit = outer[-2]+80000
ax.set_xlim(-limit*1.01, limit*1.01)
ax.set_ylim(-limit*1.01, limit*1.01)

print('Scale bar in km then AU')
# twice the limit divided by 10 (asuming split 0-1 transAxes coords into 10)
# times by two assuming axhline extends 0.2
scale = limit*1.01*2/10*2
print(scale)
print(scale/(1.496*10**8))
ax.axhline(255000, 0.1, 0.3, color='darkgray', lw=1)
ax.text(0.2, 0.955, '{:,.0f} km'.format(scale), color='darkgray', fontsize=10, zorder=31, transform=ax.transAxes, ha='center')

ax.text(0.87, 0.03, 'Moon sizes are shown relative to each\nother but not to Jupiter and the rings.\nOpacity is relative to the optical depth\nwhich is greatly exaggerated.', color='darkgray', fontsize=8, zorder=31, transform=ax.transAxes, ha='center', multialignment='right', alpha=.7)

ax.set_aspect('equal')
ax.axis('off')

plt.show()
# plt.savefig('../figures/jupiter_rings.png', dpi=150, bbox_inches='tight')