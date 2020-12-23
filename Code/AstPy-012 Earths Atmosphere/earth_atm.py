import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

file = 'int_std_atm.csv'

df = pd.read_csv(file)

print(df.head())

h = df['h'].values
lapse = df['lapse_rate'].values
T = df['T'].values

heights = []
temps = []

# construct temps from lapse rates
for i in range(len(h)-1):
    res = 1 # m - lower than 1000
    base_h = h[i]
    next_base_h = h[i+1]
    base_T = T[i]
    this_lapse = lapse[i]
    new_heights = np.arange(base_h, next_base_h, res)
    size = len(new_heights)
    new_temps = np.zeros((size))
    for j in range(size):
        new_temps[j] = base_T - this_lapse*res*j/1000
    heights.append(new_heights)
    temps.append(new_temps)

heights = np.concatenate(heights)/1000
temps = np.concatenate(temps)

fig = plt.figure(num=1, figsize=(6,10))
ax = plt.subplot(111)

# ax.plot(temps, heights, 'w', zorder=0)

# ax.set_xlim(min(temps)-10, max(temps)+10)
# ax.set_ylim(min(heights), 100)

df2 = pd.read_csv('structure.csv')

earth_atm = df2.query('object==\'earth\' and atm==\'y\' and layer_type==\'mechanical\'')
print(earth_atm)

depth = earth_atm['depth'].values
depth[0] = 11
depth[1] = 47
depth[2] = 84.852
colors = earth_atm['color'].values
orders = earth_atm['depth_order'].values[::-1]
orders -= 2*min(orders)
# width = max(temps)+10-min(temps)+10
# width = 110
width = 500

# add layer rectangles
for i in range(len(depth)):
    # this_height = depth[i] - min(heights)
    this_height = depth[i]
    # starty = min(heights)
    starty = 0
    # startx = min(temps)-10
    startx = 0
    rect = Rectangle((startx, starty), width=width, height=this_height, fc=colors[i], ec='None', zorder=orders[i], alpha=.8, clip_on=True)
    ax.add_patch(rect)

# height vs temp
# fs = 8
# al = .6
# ax.text(0.05, 0.05, 'Troposphere', color='w', fontsize=fs, transform=ax.transAxes)
# ax.text(0.8, 0.12, 'Tropopause', color='w', fontsize=fs, transform=ax.transAxes, alpha=al)
# ax.text(0.05, 0.28, 'Stratosphere', color='w', fontsize=fs, transform=ax.transAxes)
# ax.text(0.8, 0.478, 'Stratopause', color='w', fontsize=fs, transform=ax.transAxes, alpha=al)
# ax.text(0.05, 0.65, 'Mesosphere', color='w', fontsize=fs, transform=ax.transAxes)
# ax.text(0.8, 0.854, 'Mesopause', color='w', fontsize=fs, transform=ax.transAxes, alpha=al)
# ax.text(0.05, 0.92, 'Thermosphere', color='w', fontsize=fs, transform=ax.transAxes)

# height vs pressure
# fs = 8
# al = .6
# xloc = .9
# ax.text(xloc, 0.105, 'Troposphere', color='w', fontsize=fs, transform=ax.transAxes, ha='center')
# ax.text(xloc, 0.23, 'Tropopause', color='w', fontsize=fs, transform=ax.transAxes, alpha=al, ha='center')
# ax.text(xloc, 0.595, 'Stratosphere', color='w', fontsize=fs, transform=ax.transAxes, ha='center')
# ax.text(xloc, 0.95, 'Stratopause', color='w', fontsize=fs, transform=ax.transAxes, alpha=al, ha='center')
# # ax.text(0.05, 0.65, 'Mesosphere', color='w', fontsize=fs, transform=ax.transAxes)

# height vs density
# fs = 8
# al = .6
# xloc = .9
# ax.text(xloc, 0.105, 'Troposphere', color='w', fontsize=fs, transform=ax.transAxes, ha='center')
# ax.text(xloc, 0.23, 'Tropopause', color='w', fontsize=fs, transform=ax.transAxes, alpha=al, ha='center')
# ax.text(xloc, 0.595, 'Stratosphere', color='w', fontsize=fs, transform=ax.transAxes, ha='center')
# ax.text(xloc, 0.95, 'Stratopause', color='w', fontsize=fs, transform=ax.transAxes, alpha=al, ha='center')
# # ax.text(0.05, 0.65, 'Mesosphere', color='w', fontsize=fs, transform=ax.transAxes)

# height vs speed of sound
fs = 8
al = .6
ax.text(0.05, 0.06, 'Troposphere', color='w', fontsize=fs, transform=ax.transAxes)
ax.text(0.8, 0.14, 'Tropopause', color='w', fontsize=fs, transform=ax.transAxes, alpha=al)
ax.text(0.05, 0.32, 'Stratosphere', color='w', fontsize=fs, transform=ax.transAxes)
ax.text(0.8, 0.565, 'Stratopause', color='w', fontsize=fs, transform=ax.transAxes, alpha=al)
ax.text(0.05, 0.76, 'Mesosphere', color='w', fontsize=fs, transform=ax.transAxes)
# ax.text(0.8, 0.854, 'Mesopause', color='w', fontsize=fs, transform=ax.transAxes, alpha=al)
# ax.text(0.05, 0.92, 'Thermosphere', color='w', fontsize=fs, transform=ax.transAxes)

# ax.set_xlabel(r'Temperature / $^{\circ}C$', color='darkgray', labelpad=10, fontsize=12)
ax.set_ylabel('Geopotential Altitude / $km$', color='darkgray', labelpad=10, fontsize=12)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_color('grey')
ax.tick_params(axis='both', which='both', colors='lightgrey', labelcolor='darkgray')

#cal pressures
g = 9.8 # m/s^2
R = 287 # m^2/s^2/K
To = 288 # K
Po = 101.3 # kPa
L = 0.0065 # K/m

T_trop = np.arange(To, 216.60, -.05)
h_trop = (To - T_trop)/L
P_trop = Po*(T_trop/To)**(g/(L*R))

Ts = 216.6
hs = max(h_trop)
Ps = min(P_trop)

# WRONG
# T_strat = np.array(-56.5, -3, .5)
h_strat = np.arange(hs, 47000, 1)
P_strat = Ps*np.exp(g*(hs-h_strat)/R/Ts)

# ax.plot(P_trop, h_trop/1000, color='w', zorder=4)
# ax.plot(P_strat, h_strat/1000, color='w', zorder=4)

# ax.set_xlim(0, 110)
# ax.set_ylim(0, 50)

# ax.set_xlabel(r'Pressure / $kPa$', color='darkgray', labelpad=10, fontsize=12)

# calc densities
# P = rho*R*T

rho_trop = P_trop/R/T_trop

# construct T_strat to match h_strat
T_strat = []
j = 0
k = 0
for i in h_strat:
    if i < 20000:
        T_strat.append(-56.5+273.15)
    elif i < 32000:
        if j == 0:
            j = i
        T_strat.append(-56.5+273.15 + 1 * (i-j) / 1000)
    else:
        if k ==0:
            k = i
        T_strat.append(-44.5+273.15 + 2.8 * (i-k) / 1000)

# WRONG
T_strat = np.array(T_strat)

rho_strat = P_strat/R/T_strat

# ax.plot(rho_trop*1000, h_trop/1000, color='w', zorder=4)
# ax.plot(rho_strat*1000, h_strat/1000, color='w', zorder=4)

# print(rho_trop)
# print(rho_strat)

# ax.set_xlim(0, 1.3)
# ax.set_ylim(0, 50)
# ax.set_xlabel(r'Density / $kg/m^3$', color='darkgray', labelpad=10, fontsize=12)

# Calc speed of sound

a = np.sqrt(1.4*R*(temps+273.15))

ax.plot(a, heights, color='w', zorder=4)

ax.set_xlim(min(a)-10, max(a)+10)
ax.set_ylim(0, max(heights))
ax.set_xlabel(r'Speed of Sound / $m/s$', color='darkgray', labelpad=10, fontsize=12)

# plt.show()
# plt.savefig('int_std_atm_sound.png', dpi=200)