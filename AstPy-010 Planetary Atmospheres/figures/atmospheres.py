import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib.patches import Circle
import os

file = '../atmospheres.csv'

df = pd.read_csv(file)

print(df.head())

print(df.sum())

# From Comparing the Atmospheric Compositions of All Planets and Giant Moons inSolar 
# SystemRauf KM, Hossieni H*, Majeed D and Ibrahim R
# upper limit taken for <400 values and errors ignored for other values
# CO2 for Earth is lower than present

planet_name = 'Earth'

earth = df.loc[df[planet_name] > 0.01].sort_values(by=planet_name, ascending=False)
print(earth)

earthVals = earth[planet_name].values
print(earthVals)

earthChems = earth['Chemical'].values
print(earthChems)

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

earthChemNames = chem_names(earthChems)
print(earthChemNames)

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

fig = plt.figure(num=1, figsize=(8, 8))
ax = plt.subplot(121)
ax2 = plt.subplot(122, aspect='equal', sharey=ax)

width = 20/2

for i in range(len(earth)):
    if i==0:
        bot = 0
    else:
        bot = np.sum(earthVals[:i])
    text = earthChemNames[i]
    if earthVals[i] < .5:
        val = earthVals[i]*10000
        text += '\n{} ppm'.format(int(val))
    else:
        val = earthVals[i]
        text += '\n{:.1f} %'.format(val)
    thisbar = ax.bar(['Earth'], [earthVals[i]], width, label=text, bottom=bot, alpha=0.8, color=colors[earthChems[i]])  
    x = 0.4
    y = 1/len(earth)+0.12*i -0.02 
    circle = Circle((x, y), 0.05, color=colors[earthChems[i]], alpha=0.8, ec='None', transform=fig.transFigure, clip_on=False)
    ax2.add_artist(circle)
    ax2.text(x, y, text, ha='center', va='center', color='w', multialignment='center', transform=fig.transFigure)
    if (i==len(earth)-1) and (np.sum(earthVals) < 100): 
        y = 1/len(earth)+0.12*(i+1) -0.02 
        circle = Circle((x, y), 0.05, color=colors['Other'], alpha=0.8, ec='None', transform=fig.transFigure, clip_on=False)
        ax2.add_artist(circle)
        text = 'Other\n<{} %'.format(100-int(np.sum(earthVals)))
        ax2.text(x, y, text, ha='center', va='center', color='w', multialignment='center', transform=fig.transFigure)

ax.axis('off')
ax2.axis('off')
ax.get_xaxis().set_visible(False) # this removes the ticks and numbers for x axis
ax.get_yaxis().set_visible(False) # this removes the ticks and numbers for y axis
ax2.get_xaxis().set_visible(False) # this removes the ticks and numbers for x axis
ax2.get_yaxis().set_visible(False) # this removes the ticks and numbers for y axis

ax.set_title(planet_name+'s', fontsize=16, color='darkgray', y=1.02, ha='center')
ax.text(0.5, 0.995, 'Atmospheric Composition', fontsize=12, color='darkgray', transform=ax.transAxes, ha='center')

# plt.tight_layout()
fig.tight_layout(rect=[0,0,.85,1])
# plt.show()
plt.savefig('./'+planet_name+'s_Atm_comp.png', bbox_inches='tight', pad_inches=0)

# hack to trim whitespace
os.system('magick convert '+'./figures/'+planet_name+'s_Atm_comp.png'+' -trim '+'./figures/'+planet_name+'s_Atm_comp.png')