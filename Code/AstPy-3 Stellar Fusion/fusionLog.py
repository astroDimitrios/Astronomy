# © Dimitrios Theodorakis GNU General Public License v3.0 https://github.com/DimitriosAstro/Astronomy
# Introduction to nuclear fusion

import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc


## Units and Particles

# Before we look at fusion we need to know about some elementary particles
# An atom is made up of protons and neutrons in a central nucleus, and electrons which orbit the nucleus
# These three particles are very small! The mass of a proton is defined below

pMass = 1.6726219236951*10**(-27) # kg

# This is a super small number! Lets introduce the atomic mass unit, u.
# This lets us convert our proton mass to a larger number which is easier to work with.

atomicMassUnit = 1.66054*10**(-27) # kg
pMassInAMU = pMass/atomicMassUnit

print("Proton's mass in atomic mass units: "+str(pMassInAMU)+" u")

# This number is a lot easier to work with!

# Particles also have a rest energy associated with their mass by Einsteins famous equation E = mc^2

c = 299792458 # m/s
pEnergy = pMass*c**2

print("Proton's rest energy: "+str(pEnergy)+" J")

# Hold on we used the mass in kg here but we converted the mass into u to make the numbers easier.
# Let's se if we can change the energy into more workable units as well.

# We will change Joules to electron volts (eV). 1 eV = 1.602176634*10**(-19) J (1.602176634*10**(-19) is also the charge of an electron in Coloumbs!)

eV = 1.602176634*10**(-19) # J
pEnergyeV = pEnergy/eV

print("Proton's rest energy: "+str(pEnergyeV/1000000)+" MeV")

# You'll notice I also divided by a miliion to print the answer in MeV.

# Actually we can skip a few steps if we define the proton's mass in u from the beginning:

pM = 1.00727646662153 # u

print(str(round(pM,5)==round(pMassInAMU,5)) + " - Yay! The accepted value is close to our calculate mass.")

# We can then use the atomic mass unit energy equivalence to covert u to MeV.

u = 931.4941024228 # MeV/c^2
pE = pM*u
print("Proton's rest energy: "+str(pE)+" MeV")

print(str(round(pE,5)==round(pEnergyeV/1000000,5)) + " - Yay! Our two values are in agreement.")

# Over to you: 

# Caculate the mass of a neutron in u and its rest energy in MeV.
# Are the numbers the same for protons and neutrons?

# electron mass = 9.109383701528*10**(-31) kg

## Mass Excess and Binding Energy

# Now we know about the different units we are going to use let's start looking at nuclei.
# Why nuclei? The temperatures needed to fuse elements are so high that fusion occurs in a plasma where electrons are striped from the atom.
# It is these nuclei that fuse together.

# Lets look at the 1.0078250321 1 H+ nuclei. It has an Atomic Number (Z) of 1 and a Mass Number of 1.0078250321 (A). Z is the number of protons in our nucleus (and the number of electrons in an atom).
# A is the number of protons and neutrons in the nucleus.
# Later we'll need the number of neutrons in a nucleus which we can find using A-Z.

# Notice how A is greater than Z? You might think A should be 1 right, after all it only has 1 proton and 0 neutrons.
# The actual mass is 1! This extra mass is called the mass excess. Let's calculate this mass excess.

# m = Am(u) + deltaM
# deltaM = m - Am(u)

deltaM_H = (1.0078250321-np.floor(1.0078250321))*u*1000
print("Mass excess for 1H nucleus: "+str(deltaM_H)+" keV")

# This mass excess is related to the binding energy. Nuclear binding energy is the energy needed to break a nucleus into protons and neutrons.
# Electron binding energy is the energy needed to break the electrons free from the atom.

# Think of it this way:

# Hydrogen + electron binding energy = proton + neutron
# 4He2+ + nuclear binding energy = 2 proton + 2 neutron

# Since fusion deals with nulei we will only consider nuclear binding energy which is commonly expressed as Binding energy per nucleon in keV (nucleon being a proton or neutron).
# The binding energy per nucleon for H is 0 because there is only one nucleon.

## Visualising Binding Energy

# Before we move on let's look at the binding energy per nucleon for the elements. We can use the library pandas to analyse data from the Atomic Mass Data Center which is in the csv "mass16Abundant.csv"

import pandas as pd

df = pd.read_csv('mass16Abundant.csv')

# This loads the nuclear data for the most abundant isotope for each element.
# We can have a look at it using the following command:

print(df.head())

# This printed out the header and the first five rows. You can see data for the elements Hydrogen to Boron.
# Let's plot the binding energy per nucleon (keV) against the atomic number (Z):

fig = plt.figure(num=1, figsize=(15,5))
ax = plt.axes(ylim=(0,10))

# random colours - set up size for normal small marker and enlarged marker
rng = default_rng()
colors = rng.random(len(df))
small = 50
large = 200
sizes = np.ones(len(df))*small

# convert to MeV for plot
df["BINDING ENERGY (keV)"] = df["BINDING ENERGY (keV)"]/1000

marks = plt.scatter(df["Z"], df["BINDING ENERGY (keV)"], marker='o', alpha=0.75, c=colors, cmap="viridis", zorder=2, s=sizes)
lines = plt.plot(df["Z"], df["BINDING ENERGY (keV)"], color="k", alpha=0.5, zorder=1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel("Z")
ax.set_ylabel("B/A (MeV/nucleon)")
ax.xaxis.labelpad=10.0
ax.yaxis.labelpad=15.0
ax.set_title("Binding energy per nucleon vs Atomic Number", pad=20.)
ax.set_xscale("log")

# annotate first five most abundant elements and iron
indFe = df[df["EL"]=="Fe"].index.values[0]
ax.annotate("Fe", xy=(df["Z"][indFe], df["BINDING ENERGY (keV)"][indFe]-.2), xytext=(df["Z"][indFe], df["BINDING ENERGY (keV)"][indFe]-1.5), arrowprops=dict(arrowstyle="->", fc="grey", ec="grey"))
ax.annotate("H", xy=(df["Z"][0], df["BINDING ENERGY (keV)"][0]), xytext=(df["Z"][0]+.1, df["BINDING ENERGY (keV)"][0]+.25))
ax.annotate("He", xy=(df["Z"][1], df["BINDING ENERGY (keV)"][1]), xytext=(df["Z"][1], df["BINDING ENERGY (keV)"][1]+.45))
ax.annotate("Li", xy=(df["Z"][2], df["BINDING ENERGY (keV)"][2]), xytext=(df["Z"][2]+.2, df["BINDING ENERGY (keV)"][2]-.3))
ax.annotate("Be", xy=(df["Z"][3], df["BINDING ENERGY (keV)"][3]), xytext=(df["Z"][3]+.2, df["BINDING ENERGY (keV)"][3]-.45))
ax.annotate("B", xy=(df["Z"][4], df["BINDING ENERGY (keV)"][4]), xytext=(df["Z"][4]+.4, df["BINDING ENERGY (keV)"][4]-.25))

# set element text to animate the element symbol
element = ax.annotate("", xy=(0,0))
alreadyAnnotated = ["H","He","Li","Be","B","Fe","N"]
BETextini = df["EL"][0]+" = "+str(round(df["BINDING ENERGY (keV)"][0], 2))+" keV"
# set binding energy value text
BEText = ax.text(0.1,0.9,BETextini, fontsize=12, transform=ax.transAxes, color="grey", horizontalalignment='center', verticalalignment='center')

def animate(i):
    global marks, element, BEText
    # new size array with larger size for new highlighted element
    nSizes = sizes
    nSizes[i-1] = small
    nSizes[i] = large
    marks.remove()
    marks = plt.scatter(df["Z"], df["BINDING ENERGY (keV)"], marker='o', alpha=0.75, c=colors, cmap="viridis", zorder=2, s=nSizes)
    # element symbol annotations only if not already annotated, special for N due to plot position
    if not df["EL"][i] in alreadyAnnotated:
        element.remove()
        element = ax.annotate(df["EL"][i], xy=(df["Z"][i], df["BINDING ENERGY (keV)"][i]), xytext=(df["Z"][i], df["BINDING ENERGY (keV)"][i]+.500))
    elif df["EL"][i]=="N":
        element.remove()
        element = ax.annotate(df["EL"][i], xy=(df["Z"][i], df["BINDING ENERGY (keV)"][i]), xytext=(df["Z"][i]-0.75, df["BINDING ENERGY (keV)"][i]+.500))
    else:
        element.remove()
        element = ax.annotate("", xy=(0,0))
    BEText.remove()
    BETextnew = df["EL"][i]+" = "+str(round(df["BINDING ENERGY (keV)"][i], 2))+" keV"
    BEText = ax.text(0.1,0.9,BETextnew, fontsize=12, transform=ax.transAxes, color="grey", horizontalalignment='center', verticalalignment='center')
    return marks, element, BEText

anim = animation.FuncAnimation(fig, animate, frames=len(df), interval=1000)
# anim.save('bindingEnergyLog.gif', writer='imagemagick', fps=2)
plt.show()
plt.close(1)

df["BINDING ENERGY (keV)"] = df["BINDING ENERGY (keV)"]*1000

## Stellar Fusion

# The main fusion reaction in the sun is the following:
# 4 H+ --> 4He2+ + 2e+ + 2ve
# Where H+ is a hydrogen nucleus (a proton), 4He2+ is a Helium nucleus, e+ is a positron, and ve is an electron neutrino.
# There are other steps to this within this overall reaction which we have ignored (look up the p-p chain).

# We can use this equation to calcualte a Q value for the reaction.
# If energy is released Q > 0. If energy is used Q < 0.

# Q/c^2 = 4 deltaH - deltaHe - 4 me

# This is the initial mass excess - the final mass excess (minus the mass of those pesky electrons).
# If we use mass excess in terms of eV we can ignore the /c^2 term.

me = 511 # keV
Q = 4*df["MASS EXCESS (keV)"][0] - df["MASS EXCESS (keV)"][1] - 4*me
Q /= 1000
print("Q = "+str(round(Q,3))+" MeV")

# That's a lot of energy per reaction!
# If the two positrons annihilate with two electrons in the plasma (which they most likely will) then an extra 4 me of energy is produced.
# This brings the Q value to:

Q = 4*df["MASS EXCESS (keV)"][0] - df["MASS EXCESS (keV)"][1]
Q /= 1000
print("Q = "+str(round(Q,3))+" MeV")

# This Q value is approximately 0.7% the energy of the original 4 Hydrogen atoms. We can use this fact to estimate how long the sun can shine by fusing Hydrogen.
# We have to assume that:
# - The sun was initially 100% Hydrogen
# - The sun can only convert the inner 10% to Helium

mSun = 1.989*10**30 # kg
Enuclear = 0.007*(0.1*mSun)*c**2
print("Total Energy from fusing Hydrogen in the Sun = {:.2e} J".format(Enuclear))
Lsun = 3.828*10**26 # W (J/s)
# Divide the total energy by the energy radiated per second (the luminosity of the sun)
tnuclear = Enuclear/Lsun # This gives us a time in seconds
print("Sun's Hydrogen fusing lifetime = {:.1e} years".format(tnuclear/3600/24/365.25))


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

## Challenge

# 1) Recreate my Binding Energy Plot (or create the more common B/A vs A plot)
# 2) Calculate the energy released for each step of the p-p chain
# 3) Create a barrier plot for the next step of the p-p chain

# Write your code here!


## References and Resources

# Atzeni, S. and Meyer-ter-Vehn, J. (2004) The Physics of Inertial Fusion, OUP, ISB: 9780198562641, Url: http://www.fisicanucleare.it/documents/0-19-856264-0.pdf
# Shatz, H. (2020) The mass of a nucleus, Url: https://people.nscl.msu.edu/~schatz/PHY983_13/Lectures/mass.pdf
# Mihos, C. (2020) Stars and Planets, Url: http://burro.astr.cwru.edu/Academics/Astr221/StarPhys/nuclear.html
# 
# Nuclear Data from the Atomic Mass Data Center (AMDC) - https://www.jinaweb.org/science-research/scientific-resources/data
# Table of Isotopic Masses and Natural Abundances - http://www.sophphx.caltech.edu/Physics_6/Mathematica%20Notebooks/Mass%20Spectrometer%20Exp%209/element%20data/atomic_mass_abund.pdf
# For above data is from data is from G. Audi, A. H. Wapstra Nucl. Phys A. 1993, 565, 1-65 and G. Audi, A. H. Wapstra Nucl. Phys A. 1995,595, 409-480.
# For above the percent natural abundance data is from the 1997 report of the IUPAC Subcommittee for IsotopicAbundance Measurements by K.J.R. Rosman, P.D.P. Taylor Pure Appl. Chem.1999, 71, 1593-1607.