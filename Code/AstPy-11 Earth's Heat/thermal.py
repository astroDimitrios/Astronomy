import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Lithosphere geothermal gradient

Ts = 15 # surface temp (deg C)
Q = 30 # mantle heat flow (mW/m^2)
K = 2.5 # thermal conductivity (W/m/deg)
Ao = 2.0 # heat production (microW/m^3)
b = 10 # characteristic depth of Ao (km)

z = np.arange(0,100,.1)
T = []

for i in z:
    if i < b:
        T.append(Q*i/K + Ao*i*(b-i/2)/K + Ts)
    else:
        T.append(Q*i/K + Ao*b**2/(2*K) + Ts)

# fig = plt.figure(num=1, figsize=(6, 10))
# plt.plot(T, -z)

# # plt.show()

# axins = inset_axes(plt.gca(), width="40%", height="40%")
# axins.plot(T, -z)
# axins.set_ylim(-35, 0)
# axins.set_xlim(0, 500)

# # plt.show()

# Constructing the whole Geotherm

file = 'geotherm.csv'

df = pd.read_csv(file)

print(df.head())

df['z'] = df['r']-6371
df['Tdeg'] = df['T']-273.15

print(df.head())

fig2 = plt.figure(num=2, figsize=(6, 10))
ax = plt.subplot(111)
ax.plot(df['Tdeg'], df['z'], zorder=2, color='w')

ax.set_ylim(min(df['z']), max(df['z']))
ax.set_xlim(min(df['Tdeg']), max(df['Tdeg']))
ax.xaxis.tick_top()
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_color('grey')
ax.spines['left'].set_color('grey')
ax.tick_params(axis='both', which='both', colors='lightgrey')
ax.set_xlabel(r'Temperature / $\degree C$', labelpad=10, color='darkgrey')
ax.xaxis.set_label_position('top')
ax.set_ylabel(r'Depth / $km$', labelpad=10, color='darkgrey')

file2 = 'structure.csv'
df2 = pd.read_csv(file2)

dfE = df2.loc[df2['object'] == 'earth']
dfE = dfE.loc[dfE['layer_type'] == 'mechanical']
dfE = dfE.loc[dfE['atm'] == 'n']
dfE['z'] = dfE['depth_from_center']-dfE['depth_from_center'].values[-1]
zE = dfE['z'].values
depths = dfE['depth'].values
colors = dfE['color'].values
names = dfE['name'].values

rects=[]
for i in range(len(dfE)):
    if names[i] == 'mesosphere':
        ax.axhline(zE[i]-depths[i]+250, 0, 1, color='lightgrey', ls='--', lw=1, zorder=1, alpha=0.5)
    rect = Rectangle((min(df['Tdeg']), zE[i]-depths[i]), max(df['Tdeg']), depths[i], fc=colors[i], zorder=0, label=names[i])
    ax.add_patch(rect)
    rects.append(rect)

leg = fig2.legend(rects, names, loc='upper center', bbox_to_anchor=(0.57, 0.1), ncol=2, frameon=False, handlelength=1, handleheight=1)
plt.setp(leg.get_texts(), color='darkgrey')
fig2.subplots_adjust(left=0.2)

plt.savefig('./geotherm.png', dpi=200)
# plt.show()

# Heat sources Earth:
# Primordial heat from formation
# Radioactivity

# Methods transfer heat:
# Convection
# Conduction
# Advection

# Conduction

# water 4180 J/kg/K
# iron 447
# olivine 815
# mantle 1260
# rock typical 700
# periclase (MgO) 924

# Energy needed to raise 1 kg of mantle material from temp top mantle to temp bottom
# (assume const P and no phase change)

E = 1*1260*2000/10**6
print(E) # MJ

# Compare to the energy needed to boil water from room temp (1kg)

Ew = 1*4180*100/10**6
print(Ew) # MJ

# Thermal conductivity - how easily heat is transported
# Q = k dT/dz

# diamond 1600 W/mK
# sed rock 1.2 - 4.2
# granite 2.4 - 3.8
# basalt 1.3 - 2.9
# upper mantle 6.7
# lower mantle 20

# Why difference between upper and lower mantle?

# Calc therm gradient in upper mantle (take gradient in athenosphere)
# Then calc the thermal conductivity 
# Do same for lower mantle (mesosphere) and compare

ThermC_Upper = 6.7*(1600-1300)/(750000-110000) # W/m^2

print(ThermC_Upper)

ThermC_Lower = 20*(2500-1600)/(2700000-750000)

print(ThermC_Lower)

# hard to get gradient since it's not same over all of the athenosphere/lithosphere (plus T not well known anyway)

# Advection - lava cooling to basalt

# Water to ice 335 kJ/kg
# Molten Fe to Solid Fe 275
# Basalt (Hawaii) 400

# Energy released when lava cools to basalt (5 kg volcanic bomb)

E_lav_bas = 400*5/10**3

# number energy rel. total much higher due to conduction we saw earlier (cooling before and after phase change)

print(E_lav_bas)

# Can you work out energy needed to melt Fe (5 kg) at the core mantle boundary?

E_fe_melt = 275*5/10**3

print(E_fe_melt)

# Of course Earth's structure not uniform / techtonics upperlayers so heat flow varies

## Challenge mantle exchanges heat with the lithosphere (assume lithosphere starts 20 C) - calculate the change in temp of the surrounding rock
# Visualise the results
# take a grid (array)
# each cell needs a temp
# each cell has a mass of 1 kg
# assume lithos and asthenos c = 1260
# You will need Newton's law of cooling dT/dt = -r(T-Tenv) take a guess at r
# (you can try and work out a good r afterwards http://greenteapress.com/modsimpy/ModSimPy3.pdf)

# Convection? Look up Rayleigh num and try calc it for mantle
# Hard to simulate have to use differential equations