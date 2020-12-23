import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker

file = 'exobase.csv'

df = pd.read_csv(file)

print(df.head())

df['exobase mean temp'] = (df['exobase temp high'] + df['exobase temp low'])/2

print(df.head())

names = df['object'].values
escVelSixth = df['esc vel'].values/6

k = 1.38064852*10**(-23) # m^2kgs^-2K-1

u = 1.6605390666050*10**(-27) # kg
m1H = 1.007825*2 # u
m4He = 4.002602 # u
m16O = 15.99491461956*2 # u
mH2O = (18/10**3)/(6.022137*10**(23)) # kg
mCO2 = (44.01/10**3)/(6.022137*10**(23)) # kg

T = np.arange(0, 1100, 1)

vH = (3*k*T/(m1H*u))**.5 / 1000
v4He = (3*k*T/(m4He*u))**.5 / 1000
v16O = (3*k*T/(m16O*u))**.5 / 1000
vH2O = (3*k*T/mH2O)**.5 / 1000
vCO2 =  (3*k*T/mCO2)**.5 / 1000

fig = plt.figure(num=1, figsize=(10, 6))
ax = plt.subplot(111)

ax.plot(T, vH, zorder=0, lw=1, alpha=.4)
ax.plot(T, v4He, zorder=0, lw=1, alpha=.4)
ax.plot(T, v16O, zorder=0, lw=1, alpha=.4)
ax.plot(T, vH2O, zorder=0, lw=1, alpha=.4)
ax.plot(T, vCO2, zorder=0, lw=1, alpha=.4)

rot = 8
txtcol = 'gray'
ax.text(100, vH[100], '$Hydrogen$', rotation=rot, ha='center', color=txtcol)
ax.text(100, v4He[100], '$Helium$', rotation=rot, ha='center', color=txtcol)
ax.text(100, v16O[100], '$Oxygen$', rotation=rot, ha='center', color=txtcol)
ax.text(100, vH2O[100], '$Water$', rotation=rot, ha='center', color=txtcol)
ax.text(100, vCO2[100]-0.055, r'$Carbon\ Dioxide$', rotation=rot, ha='center', color=txtcol)

colors = {
    'Mercury': 'silver', 
    'Venus': 'papayawhip', 
    'Earth': 'forestgreen',
    'Mars': 'crimson',
    'Jupiter': 'peachpuff',
    'Saturn': 'navajowhite',
    'Uranus': 'lightskyblue',
    'Neptune': 'cornflowerblue',
    'Titan': 'khaki'
}

pos = {
    'Mercury': [410, .65], 
    'Venus': [320, 1.65], 
    'Earth': [790, 1.7],
    'Mars': [290, .75],
    'Jupiter': [700, 11],
    'Saturn': [380, 7],
    'Uranus': [890, 4.2],
    'Neptune': [610, 5],
    'Titan': [160, .39]
}

sizes = np.array([38.24866729,94.88867984,100.,
         53.24553151, 1120.91564754,  944.93571653,  400.73690812,
        388.27218564,40.])

for i in range(len(names)):
    temp = df['exobase mean temp'][i]
    if names[i] == 'Venus':
        temp = df['exobase mean temp'][i]+100
    ax.scatter(temp, escVelSixth[i], color=colors[names[i]], sizes=[sizes[i]], alpha=0.75, ec='None', zorder=2)
    t = ax.text(pos[names[i]][0], pos[names[i]][1], '$'+names[i]+'$', zorder=1, color='gray')
    # t.set_bbox(dict(facecolor='w', alpha=1, edgecolor='None'))

ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlim(75, 1090)
ax.set_ylim(0.1, 20)
ax.set_xticks([100, 200, 400, 600, 1000])
ax.set_xticklabels([100, 200, 400, 600, 1000])
ax.xaxis.set_minor_locator(mticker.MultipleLocator(100))
ax.set_yticks([0.1, 0.2, 0.4, 0.6, 1.0, 2.0, 4.0, 6.0, 10.0, 20.0])
ax.set_yticklabels([0.1, 0.2, 0.4, 0.6, 1.0, 2.0, 4.0, 6.0, 10.0, 20.0])
ax.yaxis.set_minor_locator(mticker.NullLocator())
ax.tick_params(axis='both', which='both', direction='in', right=True, top=True, pad=5, colors='darkgrey')

ax.set_ylabel(r'Escape velocity / $kms^{-1}$', color=txtcol)
ax.set_xlabel(r'Temperature / $K$', color=txtcol)
ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_color('grey')
ax.spines['right'].set_color('grey')
ax.spines['top'].set_color('grey')

ax.text(0.05, 0.82, 'Planets are plotted at one sixth of their escape velocity.\nGases are plotted at their escape velocity.\nIf a gas line falls above the planet for the same\ntemperature then the planet cannot hold onto that gas.', transform=ax.transAxes, color='lightgray', fontsize=8)

# plt.show()
plt.savefig('./figures/atm_retention.png', dpi=200)