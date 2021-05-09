import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

file = 'planets.csv'

df = pd.read_csv(file)

print(df.head())
print(df.columns)

AU = 1.495978707*10**11

names = df['planet'].values
moon = df['moon'].values
colors = ['silver', 'papayawhip', 'forestgreen', 'dimgrey', 'crimson', 'peachpuff', 'navajowhite', 'lightskyblue', 'cornflowerblue', 'slategrey', 'khaki', 'lightcyan', 'burlywood', 'lemonchiffon', 'darkslategrey']
sizes = df['diameter'].values/12756*100

fig = plt.figure(num=1, figsize=(8, 4))
ax = plt.subplot(111)

mass = df['mass'].values/5.97
avg_dist = df['avg_dist'].values*10**9/AU

# ax.scatter(mass, avg_dist)
for i in range(len(names)):
    if (moon[i] == 'n') and (names[i] != 'Pluto'):
        ax.scatter(avg_dist[i], mass[i], color=colors[i], label=names[i], sizes=[sizes[i]], alpha=0.75, ec='None')

ax.set_yscale('log')
ax.set_xscale('log')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_ylim(0, 1000)
ax.set_xlabel('Orbital distance relative to the Earth', labelpad=10, color='grey')
ax.set_ylabel('Mass relative to the Earth', color='grey')
ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_color('grey')
ax.tick_params(axis='both', which='both', colors='darkgrey')

leg = ax.legend(frameon=False, loc='center', bbox_to_anchor=(1.2, 0.5), handletextpad=1, labelspacing=1.25)
plt.setp(leg.get_texts(), color='grey')
plt.tight_layout()

# plt.show()
plt.savefig('mass_vs_distance_planets.png', dpi=200)

fig = plt.figure(num=2, figsize=(8, 4))
ax = plt.subplot(111)

radii = df['diameter'].values/2/(12756/2)

for i in range(len(names)):
    if (moon[i] == 'n') and (names[i] != 'Pluto'):
        ax.scatter(avg_dist[i], radii[i], color=colors[i], label=names[i], sizes=[sizes[i]], alpha=0.75, ec='None')

ax.set_yscale('log')
ax.set_xscale('log')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_ylim(0, 100)
ax.set_xlabel('Orbital distance relative to the Earth', labelpad=10, color='grey')
ax.set_ylabel('Radius relative to the Earth', color='grey', labelpad=5)
ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_color('grey')
ax.tick_params(axis='both', which='both', colors='darkgrey')

leg = ax.legend(frameon=False, loc='center', bbox_to_anchor=(1.2, 0.5), handletextpad=1, labelspacing=1.25)
plt.setp(leg.get_texts(), color='grey')
plt.tight_layout()

# plt.show()
plt.savefig('radius_vs_distance_planets.png', dpi=200)

fig = plt.figure(num=3, figsize=(8, 4))
ax = plt.subplot(111)

density = df['density'].values/5514

for i in range(len(names)):
    if (moon[i] == 'n') and (names[i] != 'Pluto'):
        ax.scatter(avg_dist[i], density[i], color=colors[i], label=names[i], sizes=[sizes[i]], alpha=0.75, ec='None')

ax.set_yscale('log')
ax.set_xscale('log')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# ax.set_ylim(-0.1, 1.1)
ax.set_xlabel('Orbital distance relative to the Earth', labelpad=10, color='grey')
ax.set_ylabel('Density relative to the Earth', color='grey', labelpad=10)
ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_color('grey')
ax.tick_params(axis='both', which='both', colors='darkgrey')

leg = ax.legend(frameon=False, loc='center', bbox_to_anchor=(1.2, 0.5), handletextpad=1, labelspacing=1.25)
plt.setp(leg.get_texts(), color='grey')
plt.tight_layout()

# plt.show()
plt.savefig('density_vs_distance_planets.png', dpi=200)

fig = plt.figure(num=4, figsize=(8, 4))
ax = plt.subplot(111)

for i in range(len(names)):
    if (moon[i] == 'n') and (names[i] != 'Pluto'):
        ax.scatter(radii[i], density[i], color=colors[i], label=names[i], sizes=[sizes[i]], zorder=1, alpha=0.75, ec='None')

fit = np.polyfit(radii[1:4], density[1:4], 1)
rad = np.arange(0.35, 1.5, 0.05)
den = fit[0]*rad + fit[1]
ax.plot(rad, den, color='silver', alpha=0.5, zorder=0, lw=1, ls='--')

ax.set_yscale('log')
ax.set_xscale('log')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# ax.set_ylim(-0.1, 1.1)
ax.set_xlabel('Radius relative to the Earth', labelpad=10, color='grey')
ax.set_ylabel('Density relative to the Earth', color='grey', labelpad=10)
ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_color('grey')
ax.tick_params(axis='both', which='both', colors='darkgrey')

leg = ax.legend(frameon=False, loc='center', bbox_to_anchor=(1.2, 0.5), handletextpad=1, labelspacing=1.25)
plt.setp(leg.get_texts(), color='grey')
plt.tight_layout()

# plt.show()
plt.savefig('density_vs_radius_planets.png', dpi=200)