import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

# file = 'earth_chem_interior.csv'

# df = pd.read_csv(file)

# print(df.head())

# names = df['name'].values
# Si = df['Si'].values
# Fe = df['Fe'].values
# Ni = df['Ni'].values

# fig = plt.figure(num=1, figsize=(10,5))
# ax = plt.subplot()

# X = np.arange(len(names))-1
# width = .25
# bar1 = ax.bar(X - width, Si, color='tan', width=width, label='Si')
# bar2 = ax.bar(X, Fe, color='silver', width=width, label='Fe')
# bar3 = ax.bar(X + width, Ni, color='lightslategray', width=width, label='Ni')
# plt.xticks(X, tuple(names))

# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
# ax.spines['left'].set_visible(False)
# leg = ax.legend(frameon=False, handlelength=1, handleheight=1)
# plt.setp(leg.get_texts(), color='darkgrey')
# ax.get_yaxis().set_visible(False)
# ax.tick_params(axis='x', which='both', bottom=False, labelcolor='darkgrey')

# def autolabel(rects):
#     """
#     Attach a text label above each bar displaying its height
#     """
#     for rect in rects:
#         height = rect.get_height()
#         ax.text(rect.get_x() + rect.get_width()/2., height+2,
#                 '{:.2f}'.format(height),
#                 ha='center', va='bottom', color='darkgrey', fontsize=8)
# autolabel(bar1)
# autolabel(bar2)
# autolabel(bar3)

# ax.set_title('Percentage of total composition for elements Si, Fe, and Ni in different layers of the Earth', color='darkgrey', pad=25)

# # plt.show()
# plt.savefig('./figures/elem_comp_Si+Fe+Ni_earth.png')

file2 = 'earth_chem_crust.csv'

df2 = pd.read_csv(file2)

print(df2.head())

z = df2['z']
names = df2['element']
symbols = df2['symbol']
perc = df2['%']
rel = perc/28.2

fig = plt.figure(num=2, figsize=(20,10))
ax = plt.subplot()

ax.scatter(z, rel, ec='None', alpha=0.8, zorder=1, color='k')
ax.set_yscale('log')

prev = 1
holdz = []
holdrel = []
for i in range(len(z)):
    if i == 0:
        holdz.append(z[i])
        holdrel.append(rel[i])
    if z[i] - 1 == prev:
        holdz.append(z[i])
        holdrel.append(rel[i])
        prev = z[i]
    elif (z[i]-1 != prev) and (i!=0):
        ax.plot(holdz, holdrel, lw=1, color='darkgrey', zorder=0, alpha=0.4)
        holdz = [z[i]]
        holdrel = [rel[i]]
        prev = z[i]

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(0, max(z)+2)
ax.set_xlabel('z', color='darkgrey', fontsize=18)
ax.set_ylabel(r'% abundance relative to Si', color='darkgrey', fontsize=14, labelpad=10)

ax.tick_params(axis='x', which='both', bottom=True, labelcolor='darkgrey', color='lightgrey')
ax.tick_params(axis='y', which='both', left=True, labelcolor='darkgrey', color='lightgrey')

ax.spines['left'].set_edgecolor('darkgrey')
ax.spines['bottom'].set_edgecolor('darkgrey')

for i, txt in enumerate(symbols):
    color = 'darkgrey'
    if txt not in ['Mg', 'Al', 'Ti', 'Mn', 'Fe', 'Cr', 'Cu', 'Ni', 'Zn', 'Mo', 'Sn', 'W', 'Pb']:
        weight = 'normal'
    else:
        weight = 'bold'
        color = 'k'
    if txt not in ['Ru', 'Rh', 'Pd', 'Ag', 'Os', 'Ir', 'Pt', 'Au']:
        style = 'normal'
    else:
        style = 'oblique'
        color = 'k'
    if txt in ['Y', 'La', 'Ce', 'Pr', 'Nd', 'Sm', 'Tb', 'Eu', 'Gd', 'Dy', 'Ho', 'Er', 'Yb', 'Tm', 'Lu']:
        color = 'dodgerblue'
    if txt not in ['B', 'Na', 'Mg', 'Mn', 'Ru', 'Pd', 'Ag', 'Cd', 'In', 'Os', 'Pt', 'Hg', 'Tl', 'Al']:
        if i == len(z)-1:
            ax.annotate(txt, (z[i]+.3, rel[i]*1.15), zorder=2, weight=weight, style=style, color=color)
        elif rel[i+1]-rel[i] < 0:
            ax.annotate(txt, (z[i]+.3, rel[i]*1.15), zorder=2, weight=weight, style=style, color=color)
        elif z[i+1]-z[i]!=1:
            ax.annotate(txt, (z[i]+.3, rel[i]*1.15), zorder=2, weight=weight, style=style, color=color)
        else:
            ax.annotate(txt, (z[i]-.5, rel[i]*0.55), zorder=2, weight=weight, style=style, color=color)
    else:
        if txt=='B':
            ax.annotate(txt, (z[i]+.2, rel[i]*0.55), zorder=2, weight=weight, style=style, color=color)
        elif txt=='Na':
            ax.annotate(txt, (z[i]-1., rel[i]*1.3), zorder=2, weight=weight, style=style, color=color)
        elif txt=='Mg':
            ax.annotate(txt, (z[i]+.0, rel[i]*0.55), zorder=2, weight=weight, style=style, color=color)
        elif txt=='Mn':
            ax.annotate(txt, (z[i]+.0, rel[i]*0.55), zorder=2, weight=weight, style=style, color=color)
        elif txt=='Ru':
            ax.annotate(txt, (z[i]-1, rel[i]*0.55), zorder=2, weight=weight, style=style, color=color)
        elif txt=='Pd':
            ax.annotate(txt, (z[i]-1.5, rel[i]*1.3), zorder=2, weight=weight, style=style, color=color)
        elif txt=='Ag':
            ax.annotate(txt, (z[i]+0, rel[i]*0.55), zorder=2, weight=weight, style=style, color=color)
        elif txt=='Cd':
            ax.annotate(txt, (z[i]-1.5, rel[i]*1.3), zorder=2, weight=weight, style=style, color=color)
        elif txt=='In':
            ax.annotate(txt, (z[i]+0, rel[i]*0.55), zorder=2, weight=weight, style=style, color=color)
        elif txt=='Os':
            ax.annotate(txt, (z[i]-0.5, rel[i]*1.3), zorder=2, weight=weight, style=style, color=color)
        elif txt=='Pt':
            ax.annotate(txt, (z[i]-0.5, rel[i]*1.3), zorder=2, weight=weight, style=style, color=color)
        elif txt=='Hg':
            ax.annotate(txt, (z[i]-1.5, rel[i]*0.6), zorder=2, weight=weight, style=style, color=color)
        elif txt=='Tl':
            ax.annotate(txt, (z[i]-1.5, rel[i]*0.6), zorder=2, weight=weight, style=style, color=color)
        elif txt=='Al':
            ax.annotate(txt, (z[i]-1.5, rel[i]*0.7), zorder=2, weight=weight, style=style, color=color)

verts1 = [
    (42, 1.07*10**(-9)),
    (37, 1.35*10**(-9)),
    (40, 10*10**(-7)),
    (62.7, 5*10**(-8)),
    (90, 5.8*10**(-8)),
    (90, 2*10**(-10)),
    (71, 4*10**(-10)),
    (62, 2*10**(-9)),
    (42, 1.07*10**(-9)),
]

codes1 = [
    Path.MOVETO,
    Path.CURVE4,
    Path.CURVE4,
    Path.CURVE3,
    Path.CURVE4,
    Path.CURVE4,
    Path.CURVE4,
    Path.CURVE3,
    Path.CURVE3
]

path1 = Path(verts1, codes1)
patch1 = patches.PathPatch(path1, facecolor='orange', zorder=0, lw=0, alpha=.2)
ax.add_patch(patch1)

verts2 = [
    (-10, 0.007),
    (5, 40),
    (25, 30),
    (35, 0.02),
    (25, 0.0009),
    (20.2, 0.00065),
    (13.7, 5*10**(-5)),
    (3.2, 0.00033),
    (-10, 0.007),
]

codes2 = [
    Path.MOVETO,
    Path.CURVE4,
    Path.CURVE4,
    Path.CURVE3,
    Path.CURVE4,
    Path.CURVE4,
    Path.CURVE4,
    Path.CURVE3,
    Path.CURVE4,
]

path2 = Path(verts2, codes2)
patch2 = patches.PathPatch(path2, facecolor='palegreen', zorder=0, lw=0, alpha=.2)
ax.add_patch(patch2)

verts3 = [
    (3.8, 0.007),
    (4.2, 70),
    (20, 50),
    (35, 0.02),
    (25, 0.07),
    (20.2, 0.06),
    (13.7, 0.012),
    # (3.2, 0.011),
    (4, 0.007),
]

codes3 = [
    Path.MOVETO,
    Path.CURVE4,
    Path.CURVE4,
    Path.CURVE3,
    Path.CURVE4,
    Path.CURVE4,
    Path.CURVE4,
    # Path.CURVE3,
    Path.CLOSEPOLY,
]

path3 = Path(verts3, codes3)
patch3 = patches.PathPatch(path3, facecolor='limegreen', zorder=0, lw=0, alpha=.2)
ax.add_patch(patch3)

ax.text(27, 8.8, 'Rock-forming\n elements', fontsize=14, color='limegreen', multialignment='center', ha='center')
ax.text(67, 0.0002, 'Rare Earth\nelements', fontsize=14, color='dodgerblue', multialignment='center', ha='center')
ax.text(62, 8.2*10**(-9), 'Rarest \'metals\'', fontsize=14, ha='center', color='darkgrey')
ax.text(4, 4*10**(-9), r'Major industrial metals are in $\bf{Bold}$'+'\n'+r'Precious metals are in $Italic$', fontsize=12, color='darkgrey')

ax.set_title('Abundance of elements in Earth\'s continental crust', color='darkgrey', fontsize=22, pad=20)

# plt.show()
plt.savefig('./figures/elem_comp_crust_earth.png')