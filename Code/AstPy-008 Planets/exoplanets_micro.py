import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec 

file = 'planets.csv'

df = pd.read_csv(file)

print(df.head())
print(df.columns)

AU = 1.495978707*10**11

names = df['planet'].values
moon = df['moon'].values
colors = ['silver', 'papayawhip', 'forestgreen', 'dimgrey', 'crimson', 'peachpuff', 'navajowhite', 'lightskyblue', 'cornflowerblue', 'slategrey', 'khaki', 'lightcyan', 'burlywood', 'lemonchiffon', 'darkslategrey']
sizes = df['diameter'].values/12756*100
mass = df['mass'].values/5.97
avg_dist = df['aphelion'].values*10**9/AU

fig = plt.figure(num=1, figsize=(15, 6))
gs1 = gridspec.GridSpec(1, 1)
ax = fig.add_subplot(gs1[0])

radii = df['diameter'].values/2/(12756/2)

for i in range(len(names)):
    if (moon[i] == 'n') and (names[i] != 'Pluto'):
        ax.scatter(avg_dist[i], mass[i], color=colors[i], label=names[i], sizes=[sizes[i]], alpha=0.75, ec='None', zorder=5)

ax.set_yscale('log')
ax.set_xscale('log')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# ax.set_ylim(0, 100)
ax.set_xlabel('Orbital distance relative to the Earth', labelpad=10, color='grey')
ax.set_ylabel('Mass relative to the Earth', color='grey', labelpad=5)
ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_color('grey')
ax.tick_params(axis='both', which='both', colors='darkgrey')

###
exofile = 'exoplanets.csv'
exofile2 = 'exoplanets_microlensing.csv'

df2 = pd.read_csv(exofile)
df3 = pd.read_csv(exofile2)

print(df2['pl_discmethod'].unique())
# ex_rad = df2['pl_radj'].values/(12756/2)*(142984/2)
# ex_orb = df2['pl_orbsmax'].values
# disc_meth = df2['pl_discmethod'].values

# d = {ni: indi for indi, ni in enumerate(set(disc_meth))}
# ex_colors = [d[ni] for ni in disc_meth]

# ax.scatter(ex_orb, ex_rad, alpha=0.1, ec='None', c=ex_colors, cmap='viridis')

colors = ['b', 'g', 'r', 'gold', 'crimson', 'khaki', '#87a736', 'k', 'orange', 'plum', 'deeppink']
disc_meths = df2.pl_discmethod.unique()
scatters = []
labels2 = []
for i in range(len(disc_meths)):
    newdf = df2.loc[df2['pl_discmethod'] == disc_meths[i]]
    ex_rad = newdf['pl_bmassj'].values*1898/5.97
    ex_orb = newdf['pl_orbsmax'].values
    if disc_meths[i] not in ['Transit', 'Radial Velocity']:
        alpha=0.5
        zorder=1
    else:
        alpha=0.1
        zorder=0
    if disc_meths[i] not in ['Radial Velocity', 'Transit', 'Imaging', 'Orbital Brightness Modulation']:
        zorder=2
        size=60
    else:
        size=10
    if disc_meths[i] in ['Radial Velocity', 'Transit', 'Imaging']:
        scatter = ax.scatter(ex_orb, ex_rad, alpha=alpha, ec='None', color=colors[i], zorder=zorder, s=size)
        labels2.append(disc_meths[i])
        scatters.append(scatter)

exM_rad = df3['mlmassplne'].values
exM_orb = df3['mlsmaproj'].values
scatter = ax.scatter(exM_orb, exM_rad, alpha=0.2, ec='None', color='k', zorder=1, s=10)
labels2.append('Microlensing')
scatters.append(scatter)

ax.set_title('Mass relative to the Earths vs semi-major axis, Kepler exoplanet data is also shown', color='grey', pad=20)

leg2 = ax.legend(scatters, labels2, frameon=False, loc='center', bbox_to_anchor=(1.25, 0.5), handletextpad=1, labelspacing=1.25)
plt.setp(leg2.get_texts(), color='grey')
for lh in leg2.legendHandles: 
    lh.set_alpha(.5)
leg = ax.legend(frameon=False, loc='center', bbox_to_anchor=(1.1, 0.5), handletextpad=1, labelspacing=1.25)
plt.setp(leg.get_texts(), color='grey')
plt.gca().add_artist(leg2)
# plt.tight_layout()
gs1.tight_layout(fig, rect=[0, 0, .88, 1])

# plt.show()
plt.savefig('mass_vs_distance_exoplanets.png', dpi=150)