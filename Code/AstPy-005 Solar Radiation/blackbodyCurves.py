import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import rc
# You will need latex installed
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

# define constants
T = 5772 # K
kb = 1.380649*10**(-23) # J/K
c = 299792458 # m/s
h = 6.62607015*10**(-34) # Js

# set wavelength array and B arrays
l = np.arange(0.01,3,0.01)*10**(-6)
B = np.zeros(len(l))
BHigh = np.zeros(len(l))
BLow = np.zeros(len(l))
BLower = np.zeros(len(l))
BLower2 = np.zeros(len(l))


# calculate B's for the different Temps
for i in range(len(l)):
    B[i] = 2*h*c**2/l[i]**5 * 1/(np.exp(h*c/(l[i]*kb*T))-1)
    BHigh[i] = 2*h*c**2/l[i]**5 * 1/(np.exp(h*c/(l[i]*kb*6000))-1)
    BLow[i] = 2*h*c**2/l[i]**5 * 1/(np.exp(h*c/(l[i]*kb*5000))-1)
    BLower[i] = 2*h*c**2/l[i]**5 * 1/(np.exp(h*c/(l[i]*kb*4000))-1)
    BLower2[i] = 2*h*c**2/l[i]**5 * 1/(np.exp(h*c/(l[i]*kb*3000))-1)

fig = plt.figure(num=1, figsize=(10,8))
ax = plt.subplot(xlim=(0,2000),ylim=(0,3.5))
ax.set_title(r"$Radiation\ Curves\ for\ different\ Temperatures$", pad=20, fontsize=20)
ax.set_xlabel(r'$\lambda\ /\ nm$', labelpad=10, fontsize=14)
ax.set_ylabel(r"$Spectral\ Intensity\ /\ 10^{4}\ Wsr^{-1}m^{-2}nm^{-1}$", labelpad=10, fontsize=14)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
spectrum = plt.imread("spectrum.png")
ax.imshow(spectrum, extent=[380,740,0,3.5], alpha=0.4)
ax.set_aspect('auto')

# wein's law to calculate the peak wavelengths for an array of temperatures
b = 2.897771955*10**(-3) # m K
TR = np.arange(1000, 7000)
lpR = b/TR
Bmax = np.zeros(len(lpR))

for i in range(len(lpR)):
    Bmax[i] = 2*h*c**2/lpR[i]**5 * 1/(np.exp(h*c/(lpR[i]*kb*TR[i]))-1)

# ax.plot(lpR*10**6, Bmax/10**13, c="k", alpha=0.5, zorder=-1)

# weins law but for just the 5 peaks for the curves
Temps = np.array([6000,T,5000,4000,3000])
lpoints = b/Temps
Bpoints = 2*h*c**2/lpoints**5 * 1/(np.exp(h*c/(lpoints*kb*Temps))-1)

# construct legend labels
labels = []
for i in range(len(Temps)):
    labels.append(r"${:.0f}$".format(Temps[i])+r"$\ K,\ \ $"+r'$\lambda_{peak}$ = '+r"${:.0f}$".format(lpoints[i]*10**9)+r' $nm$')

ax.plot(l*10**9, BHigh/10**13, c="powderblue", label=labels[0])
ax.plot(l*10**9, B/10**13, c="gold", label=labels[1])
ax.plot(l*10**9, BLow/10**13, c="orange", label=labels[2])
ax.plot(l*10**9, BLower/10**13, c="orangered", label=labels[3])
ax.plot(l*10**9, BLower2/10**13, c="firebrick", label=labels[4])
plt.scatter(lpoints*10**9,Bpoints/10**13,c="k", s=10, zorder=6)

plotText = r"$Planck's\ Law$"+"\n"+r"$B(\lambda,T) = \frac{2hc^2}{\lambda^5} \frac{1}{e^{\frac{hc}{\lambda k_BT}}-1}$"
ax.text(.65, .85, plotText, size=18, va="center", ha="center", multialignment="center", linespacing=2, transform=ax.transAxes)

plt.legend(frameon=False, borderpad=2, labelspacing=1, loc=7, fontsize=14)
# plt.show()
# plt.savefig("blackbodyCurves.png", dpi=160)