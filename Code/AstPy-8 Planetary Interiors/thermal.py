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

# plt.savefig('./figures/geotherm.png', dpi=200)
# plt.show()