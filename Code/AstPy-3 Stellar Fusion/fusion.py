# © Dimitrios Theodorakis GNU General Public License v3.0 https://github.com/DimitriosAstro/Astronomy
# Introduction to nuclear fusion

import numpy as np
import matplotlib.pyplot as plt

# Particle masses and fundamental charge
e = 1.602176634*10**(-19) # C
eM = 9.109383701528*10**(-31) # kg
pM = 1.6726219236951*10**(-27) # kg
nM = 1.6749274980495*10**(-27) # kg

# Speed of light, electron Volts conversion, conversion to Mega
c = 299792458 # m/s
eV = e # J per eV
toMega = 10**6

# E = mc^2
# Energy of proton
pE = pM*c**2 # J
print(pE)

# Energy in eV
pEeV = pE/eV # eV
print(pEeV/toMega) # MeV

# Atomic mass units
u = 931.4941024228 # MeV/c^2
H_AMU = 1.0078250321 # u
eAMU = 5.4857990906516*10**(-4) # u
pAMU = 1.00727646662153 # u
nAMU = 1.0086649159549 # u
# https://physics.nist.gov/cuu/pdf/wall_2018.pdf

# Energy of proton
# more accurate but in agreement with earlier vale (rounding errors)
print(pAMU*u)

# a hydrogen atom is 1 electron and 1 proton
hydrogenMass = pAMU + eAMU
# this doesn't equal the measured mass of Hydrogen!
print(hydrogenMass==H_AMU)

# What's the energy difference (here convert to eV from Mega)
# The actual value should be -13.6 eV
print((H_AMU-hydrogenMass)*u*toMega)
# This is the binding energy. 13.6 eV is required to break a Hydrogen into a proton and an electron (ionise the atom)
# So when you fuse a proton and an electron you get Hydrogen and energy

# e + p = 1H + 13.6eV

He_AMU = 4.002602 # u

# Helium is 2 protons and two neutrons and two electrons
heliumMass = 2*pAMU + 2*nAMU + 2*eAMU
print((He_AMU-heliumMass)*u)

# 4 1H+ --> 4He2+ + 2e+ +2ve
print((4*H_AMU-He_AMU)*u) # ignoring electrons and lighter particles
# Near actual value of -26.73 MeV
# print((4*pAMU-2*pAMU-2*nAMU)*u)

# delta m = (zmp + Nmn) - M
# print((pAMU-H_AMU)*u)
# print((2*pAMU+2*nAMU-He_AMU)*u)
print((pAMU+eAMU-H_AMU)*u*toMega)
print((2*pAMU+2*nAMU+2*eAMU-He_AMU)*u)

# print(4*u-2*pAMU*u-2*nAMU*u)