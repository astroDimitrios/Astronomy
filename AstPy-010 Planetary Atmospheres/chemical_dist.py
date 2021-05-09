import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib.patches import Circle
# import os

file = 'atmospheres.csv'

df = pd.read_csv(file)

print(df.head())

# From Comparing the Atmospheric Compositions of All Planets and Giant Moons inSolar 
# SystemRauf KM, Hossieni H*, Majeed D and Ibrahim R
# upper limit taken for <400 values and errors ignored for other values
# CO2 for Earth is lower than present

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

chem_name = 'O2'
textx = 0.8
texty = 0.8

chem = df.loc[df['Chemical'] == chem_name].values[0]
print(chem)

def chem_names(names):
    '''
    Takes a list or array of chemical names and returns them as LaTex/mathsmode strings
    For labels in matplotlib
    '''
    pretty_names = []
    for name in names:
        chars = list(name)
        pretty_name = '$'
        for i in range(len(chars)):
            if chars[i].isdigit() and i==0:
                pretty_name += '^{'+chars[i]+'}'
            elif chars[i].isalpha():
                pretty_name += chars[i]
            else:
                pretty_name += '_{'+chars[i]+'}'
        pretty_name += '$'
        pretty_names.append(pretty_name)
    return pretty_names

name = chem_names([chem_name])[0]
print(name)

vals = chem[1:]
print(vals)

colors = {
    'N2': '#3489AC',
    'O2': '#92AE33',
    'Ar': '#D06D6D',
    'CO2': '#B34A17',
    'Na': '#979695',
    'H2': '#4462AB',
    '4He': '#D7880A',
    'CH4': '#D1BB3F',
    'SO2': 'maroon',
    'GeH4': 'sandybrown',
    'HD': 'mediumseagreen',
    'H2O': 'lightskyblue',
    'CO': 'peru',
    'Other': '#B3947E'
}

fig = plt.figure(num=1, figsize=(10, 5))
ax = plt.subplot(111)

ax.bar(planets, vals, width=0.75, color=colors[chem_name])

for i, v in enumerate(vals):
    if v > .5:
        txt = '{:.1f} %'.format(v)
    elif v > 1/100000:
        txt = '{:.1f} ppm'.format(v*10000)
    elif v> 1/100000000:
        txt = '{:.1f} ppb'.format(v*10000000)
    else:
        txt = '{:.1f} ppt'.format(v*10000000000) 
    ax.text(i, v*1.3, txt, color='darkgray', fontweight='bold', ha='center', fontsize=6)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_color('grey')
ax.tick_params(axis='both', which='both', colors='darkgrey')
ax.set_yscale('log')
ax.set_ylabel(r'$\%$ of '+name+' in the atmosphere', labelpad=10, color='darkgray')

ax.text(textx, texty, 'No bar or value'+'\n'+r'indicates a $\%$ of 0', color='darkgray', transform=ax.transAxes, multialignment='center')

ax.set_title(r'$\%$ of '+name+' in the atmospheres of the planets and Pluto', ha='center', color='darkgray', fontsize=16, pad=20)

# plt.show()
plt.savefig('./figures/chem_'+chem_name+'_atm_planet_comp.png', dpi=200)