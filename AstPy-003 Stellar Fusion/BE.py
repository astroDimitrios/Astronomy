# © Dimitrios Theodorakis GNU General Public License v3.0 https://github.com/astroDimitrios/Astronomy
# Visualising Binding Energy

import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# from matplotlib.ticker import ScalarFormatter, FixedLocator  # Log

import pandas as pd

df = pd.read_csv('mass16Abundant.csv')
print(df.head())

fig = plt.figure(num=1, figsize=(15,5))
# ax = plt.axes(xlim=(0,102), ylim=(0,10))   # per n with Z
# ax = plt.axes(xlim=(0,102), ylim=(0,2000)) # not per n with Z
# ax = plt.axes(xlim=(0,260), ylim=(0,2000)) # not per n with A not Z
ax = plt.axes(xlim=(0,260), ylim=(0,10))    # per n with A not Z
# ax = plt.axes(ylim=(0,10)) # All below for Log per n with Z
# ax.set_xscale("log")
# ax.set_xticks([1, 10, 100])
# ax.get_xaxis().set_major_formatter(ScalarFormatter())
# ax.get_xaxis().set_minor_locator(FixedLocator([2,3,4,5,6,7,8,9,20,30,40,50,60,70,80,90]))

# random colours - set up size for normal small marker and enlarged marker
rng = default_rng()
colors = rng.random(len(df))
small = 50
large = 200
sizes = np.ones(len(df))*small

# convert to MeV for plot
df["BINDING ENERGY (keV)"] = df["BINDING ENERGY (keV)"]/1000                # per Nucleon (n)
# df["BINDING ENERGY (keV)"] = df["BINDING ENERGY (keV)"]/1000*df["A"]       # total nuclear BE   

data = df["Z"]
# data = df["A"]
marks = plt.scatter(data, df["BINDING ENERGY (keV)"], marker='o', alpha=0.75, c=colors, cmap="viridis", zorder=2, s=sizes)
lines = plt.plot(data, df["BINDING ENERGY (keV)"], color="k", alpha=0.5, zorder=1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel("A")
ax.set_ylabel("B/A (MeV/nucleon)")
# ax.set_ylabel("B (MeV)")
ax.xaxis.labelpad=10.0
ax.yaxis.labelpad=15.0
ax.set_title("Binding Energy per Nucleon vs Mass Number", pad=20.)
# ax.set_title("Binding Energy vs Mass Number", pad=20.)

# annotate first five most abundant elements and iron
indFe = df[df["EL"]=="Fe"].index.values[0]
ax.annotate("Fe", xy=(data[indFe], df["BINDING ENERGY (keV)"][indFe]-.24), xytext=(data[indFe], df["BINDING ENERGY (keV)"][indFe]-1.74), arrowprops=dict(arrowstyle="->", fc="grey", ec="grey"))
ax.annotate("H", xy=(data[0], df["BINDING ENERGY (keV)"][0]), xytext=(data[0]+1.25, df["BINDING ENERGY (keV)"][0]+.25))
ax.annotate("He", xy=(data[1], df["BINDING ENERGY (keV)"][1]), xytext=(data[1], df["BINDING ENERGY (keV)"][1]+.35))
ax.annotate("Li", xy=(data[2], df["BINDING ENERGY (keV)"][2]), xytext=(data[2]+1.25, df["BINDING ENERGY (keV)"][2]-.35))
ax.annotate("Be", xy=(data[3], df["BINDING ENERGY (keV)"][3]), xytext=(data[3]+1.25, df["BINDING ENERGY (keV)"][3]-.4))
ax.annotate("B", xy=(data[4], df["BINDING ENERGY (keV)"][4]), xytext=(data[4]+1.25, df["BINDING ENERGY (keV)"][4]-.2))

# # LOG
# # annotate first five most abundant elements and iron
# indFe = df[df["EL"]=="Fe"].index.values[0]
# ax.annotate("Fe", xy=(df["Z"][indFe], df["BINDING ENERGY (keV)"][indFe]-.2), xytext=(df["Z"][indFe], df["BINDING ENERGY (keV)"][indFe]-1.5), arrowprops=dict(arrowstyle="->", fc="grey", ec="grey"))
# ax.annotate("H", xy=(df["Z"][0], df["BINDING ENERGY (keV)"][0]), xytext=(df["Z"][0]+.1, df["BINDING ENERGY (keV)"][0]+.25))
# ax.annotate("He", xy=(df["Z"][1], df["BINDING ENERGY (keV)"][1]), xytext=(df["Z"][1], df["BINDING ENERGY (keV)"][1]+.45))
# ax.annotate("Li", xy=(df["Z"][2], df["BINDING ENERGY (keV)"][2]), xytext=(df["Z"][2]+.2, df["BINDING ENERGY (keV)"][2]-.3))
# ax.annotate("Be", xy=(df["Z"][3], df["BINDING ENERGY (keV)"][3]), xytext=(df["Z"][3]+.2, df["BINDING ENERGY (keV)"][3]-.45))
# ax.annotate("B", xy=(df["Z"][4], df["BINDING ENERGY (keV)"][4]), xytext=(df["Z"][4]+.4, df["BINDING ENERGY (keV)"][4]-.25))


# set element text to animate the element symbol
element = ax.annotate("", xy=(0,0))
alreadyAnnotated = ["H","He","Li","Be","B","Fe","N"]
# alreadyAnnotated = [] # for Log?
BETextini = df["EL"][0]+" = "+str(round(df["BINDING ENERGY (keV)"][0], 2))+" MeV"
# set binding energy value text - original 0.9, 0.9
BEText = ax.text(0.9,0.9,BETextini, fontsize=12, transform=ax.transAxes, color="grey", horizontalalignment='center', verticalalignment='center')

def animate(i):
    global marks, element, BEText
    # new size array with larger size for new highlighted element
    nSizes = sizes
    nSizes[i-1] = small
    nSizes[i] = large
    marks.remove()
    marks = plt.scatter(data, df["BINDING ENERGY (keV)"], marker='o', alpha=0.75, c=colors, cmap="viridis", zorder=2, s=nSizes)
    # element symbol annotations only if not already annotated, special for N due to plot position
    if not df["EL"][i] in alreadyAnnotated:
        element.remove()
        element = ax.annotate(df["EL"][i], xy=(data[i], df["BINDING ENERGY (keV)"][i]), xytext=(df["Z"][i], df["BINDING ENERGY (keV)"][i]+100)) # was +.5
    elif df["EL"][i]=="N":
        element.remove()
        element = ax.annotate(df["EL"][i], xy=(data[i], df["BINDING ENERGY (keV)"][i]), xytext=(df["Z"][i]-0.75, df["BINDING ENERGY (keV)"][i]+.5))
    else:
        element.remove()
        element = ax.annotate("", xy=(0,0))
    BEText.remove()
    BETextnew = df["EL"][i]+" = "+str(round(df["BINDING ENERGY (keV)"][i], 2))+" MeV"
    BEText = ax.text(0.9,0.9,BETextnew, fontsize=12, transform=ax.transAxes, color="grey", horizontalalignment='center', verticalalignment='center')
    return marks, element, BEText

anim = animation.FuncAnimation(fig, animate, frames=len(df), interval=1000)
anim.save('BE Media/bindingEnergyperNwithA.mp4', writer='imagemagick', fps=2)
# plt.show()


## References and Resources

# Atzeni, S. and Meyer-ter-Vehn, J. (2004) The Physics of Inertial Fusion, OUP, ISB: 9780198562641, Url: http://www.fisicanucleare.it/documents/0-19-856264-0.pdf
# Shatz, H. (2020) The mass of a nucleus, Url: https://people.nscl.msu.edu/~schatz/PHY983_13/Lectures/mass.pdf
# Mihos, C. (2020) Stars and Planets, Url: http://burro.astr.cwru.edu/Academics/Astr221/StarPhys/nuclear.html
# 
# Nuclear Data from the Atomic Mass Data Center (AMDC) - https://www.jinaweb.org/science-research/scientific-resources/data
# Table of Isotopic Masses and Natural Abundances - http://www.sophphx.caltech.edu/Physics_6/Mathematica%20Notebooks/Mass%20Spectrometer%20Exp%209/element%20data/atomic_mass_abund.pdf
# For above data is from data is from G. Audi, A. H. Wapstra Nucl. Phys A. 1993, 565, 1-65 and G. Audi, A. H. Wapstra Nucl. Phys A. 1995,595, 409-480.
# For above the percent natural abundance data is from the 1997 report of the IUPAC Subcommittee for IsotopicAbundance Measurements by K.J.R. Rosman, P.D.P. Taylor Pure Appl. Chem.1999, 71, 1593-1607.