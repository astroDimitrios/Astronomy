# © Dimitrios Theodorakis GNU General Public License v3.0 https://github.com/DimitriosAstro/Astronomy
## Introduction to the Sun's Radiation

import numpy as np
import matplotlib.pyplot as plt

## The Multi-Wavelength Sun

# We can approximate the sun as a black body (an object that absorbs and emits radiation at all frequencies). 
# The sun emits black-body radiation. This is radiation of all frequencies in the electromagnetic spectrum.
# It doesn't emit the same amount of radiation for each frequency though - we know this because hot stars look blue and cooler stars red.
# Each black body has a peak of its radiation curve - this peak tells us what frequency of radiation is emitted the most.

# Let's visualise the black-body radiation from the sun:

T = 5772 # K
kb = 1.380649*10**(-23) # J/K
c = 299792458 # m/s
h = 6.62607015*10**(-34) # Js

l = np.arange(0.01,3,0.01)*10**(-6)
B = np.zeros(len(l))

for i in range(len(l)):
    B[i] = 2*h*c**2/l[i]**5 * 1/(np.exp(h*c/(l[i]*kb*T))-1)

fig = plt.figure(2)
ax = plt.subplot(xlim=(0,3),ylim=(0,3))
ax.plot(l*10**6, B/10**13, c="gold")
ax.set_xlabel("Wavelength / micrometer")
ax.set_ylabel("Spectral Intensity / 10^13 W/sr/m^3")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.show()

# Great now let's load an image I made earlier:

# blackbodyCurves.png

# You can see a shift to higher intensity and lower wavelength (higher energy) radiation for higher temperature curves.
# The peak wavelength shown on the graph can be calculated using Wein's law:
# lambda_peak = b / T b where b = 2.897771955×10−3 m⋅K
# Let's calculate the lambda+peak for our sun and check the graph is correct:

b = 2.897771955*10**(-3) # m K
lp = b/T
print("The peak wavelength is : {:.0f} nm".format(lp*10**9))

# 502 nm just as expected! But wait, this is a wavlength of green blue not yellow like our sun is.
# Don't forget the sun radiates other wavelengths as well. The longer tail on the right of the graph to the redder wavelengths means even though the peak wavelength is green overall the sun looks yellow.

# Before we move on to get more images let's look at the Stefan-Boltzmann Law.
# We saw in the last graph that hotter stars radiate more and are therefore more luminous. But by how much?
# The Stefan-Boltzmann Law relates a star's temperature and radius to it's luminosity (the amount of energy emitted per second usually):
# L = 4 pi R^2 sigma Te^4
# Here sigma is the Stefan-Boltzman constant and Te is the effective temperature. Te is the temperature of a blackbody that would emit the same amount of radiation as the object or star.
# Let's calculate the luminosity of the sun using this law:

sigma = 5.670374419*10**(-8) # W m^-2 K^-4
R = 6.957*10**8 # m
Lsun = 4*np.pi*R**2*sigma*T**4
print("The Luminosity of the sun is : {:.2e} W".format(Lsun))

# We get very close to the accepted value of 3.828*10**26 W.
# https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html

# Of course the sun is not a perfect black body which we have assumed throughout this section.
# If were to plot observational data for the sun on our graph from earlier it would follow the gold curve but with dips and spikes.
# These are atomic absorption and emissions lines which we will look at in a future Notebook.

## Warming the Planets

# The sun's radiation warms the planets. If we approximate the planets also as black bodies we can calculate their equilibrium temperature.
# This is the temperature a planet would be from just solar heating by absorbing all incident solar radiation and emitting it all as well (remember blackbodies emit and absorb radiation perfectly).
# The equilibrium temperature is achieved when the absorbed radiation is equal to the emitted radiation of the planet (gaining energy from radiation as fast as it is loosing it).
# The power the planet recieves is:
# The power radiated from the planet is found using the stefan boltzmann law.
# Equating Pin and Pout we get:
# Tp = Tsun(1-a)^1/4 sqrt(Rsun/2D)
# Here a is the albedo of the planet which is how much incident radiation is reflected back into space and not absorbed.
# Objects with icier or whiter surfaces have a higher albedo since ice and white objects reflect more light than darker objects.

aEarth = 0.306
Tsun = T
Rsun = R
AU = 149597870700 # m
KtodegC = 273.15
degSymb = '\u00b0'

dEarth = 1 * AU
TeqEarth = Tsun*(1-aEarth)**0.25*np.sqrt(Rsun/2/dEarth)

print("The Equilibrium Tmperature of the Earth is: {:.0f} K".format(TeqEarth))
print("The Equilibrium Tmperature of the Earth is: {:.0f} {}C".format(TeqEarth-KtodegC,degSymb))

# Wow chilly! This temperature doesn't take into account internal planetary heating or the greenhouse effect so it is lower than expected.

## Challenge

# 1) Recreate my blackbody curve image
# 2) Plot the actual solar spectrum using data from https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc:C00899
#    You will get something like this: https://en.wikipedia.org/wiki/File:EffectiveTemperature_300dpi_e.png
# 3) Calculate the temperature at Mars, Venus, and Jupiter like we did for the Earth
#    How do the values compare with the actual average surface temperatures?

## References and Resources

# Mihos, C. (2020) Stars and Planets, Url: http://burro.case.edu/Academics/Astr221/SolarSys/equiltemp.html