# © Dimitrios Theodorakis GNU General Public License v3.0 https://github.com/DimitriosAstro/Astronomy

import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc

## Coloumb Barrier

# Nucleons attract each other via the strong force.
# Charged particles repel each other with the Coulomb force.

# Since the first stage of fusion in a star is two protons colliding they need to overcome their repulsion.
# More precisely they need to overcome the Coulomb Barrier by having a certain energy.

# The potential barrier is approximated by the electric potential energy:
# Vc(r) = 14.3996 (unit eV Angstrom e^(-2)) *Z1Z2e^2/r 
# at distance greater than
# rn approx equal 1.44*10**(-13)(A1^1/3 + A2^1/3) cm
# Using units of eV and Angstrom we get Vc(r) in eV.
# The top of the barrier is:
# Vb approx = Vc(rn) = Z1*Z2 / (A1^1/3 + A2^1/3) MeV
# At distances closer than rn the nuclei fuse and drop into the "nuclear well".

# We can visualise the barrier for two protons like this:

rn = 1.44*(1**(1/3)+1**(1/3)) # fm

# array of distance values, find the index where r=rn
r = np.arange(0,10.01,0.01)
indrn = np.where(r==rn)[0][0]
# initialise the Vc(r) array
Vc = np.zeros(len(r))
# for r greater than rn calculate the electric potential energy
for i in range(indrn+1,len(r)):
    # here we convert r to Angstrom and then divide by a million to get MeV
    Vc[i] = 14.3996 / (r[i]/100000) / 1000000 # MeV
# set the barrier potential energy at rn
Vb = 1/(1**(1/3)+1**(1/3))
Vc[indrn] = Vb # MeV
# set the nuclear well potential energy to the binding energy of the product (in this case deuterium)
bEDeuterium = -1112.283/1000 # MeV
for i in range(0,indrn):
    # this value was taken from the mass16.csv
    Vc[i] = bEDeuterium

fig2 = plt.figure(num=2, figsize=(10,10))
ax2 = plt.axes(xlim=(0,10))
plt.plot(r,Vc,c="k",linewidth=1)
ax2.set_xlabel("r / fm")
ax2.set_ylabel("Energy / MeV")
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_position("zero")
ax2.xaxis.set_label_coords(0.75, 0.64) 
ax2.set_xticks([5,10])
ax2.set_yticks([bEDeuterium,0,Vb])
ax2.set_yticklabels([r"$U_{0}$",0,r"$V_{b}$"])
ax2.hlines(y=Vb, xmin=0, xmax=rn, color="grey", alpha=0.6, linestyles="--", linewidth=1)
ax2.annotate(r"$r_{n}$", xy=(rn+.01,-0.01), xytext=(rn+1,-0.1), arrowprops=dict(arrowstyle="->", fc="grey", ec="grey", alpha=0.6))
ax2.set_title("proton - proton Coulomb Barrier", pad=20)
plotText = r"$r_{n}$ = "+"{:.2f}".format(rn)+r" fm"+"\n"+r"$V_{b}$ = "+"{:+.1f}".format(Vb)+r" MeV"+"\n"+r"$U_{0}$ = "+"{:+.1f}".format(bEDeuterium)+r" MeV"
ax2.text(7.5,-.5, plotText, size=14, va="center", ha="center", multialignment="left", linespacing=2)

plt.show()

# In reality quantum tunneling allows the nuclei to 'tunnel' through the peak of the barrier.
# This means they need a lower Energy to fuse.
# Since energy is related to temperature a lower required energy means the required temperature is also lower.
# If it weren't for quantum tunneling the probability of fusion in our sun would be very small.