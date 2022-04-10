# Planets

## planets.ipynb
## AIM - Analyse data on planets and exoplanets, make predictions from our plots, visualise Kepler data

**Predict**

Have a think about these questions and make some predictions! Be sure to tell someone else what you predict.

1) Are the densities of the rocky planets similar?  
2) Why are Jupiter, Saturn, Uranus, and Neptune split into two groups?  
3) Do you think it's easier for Kepler to detect Earth or Jupiter size exoplanets?

## Intro

Comparing planets by looking at data from the NASA Planetary Factsheet such as mass and radius etc.  
Looking briefly at exoplanet detection.

## Challenge

1) Recreate any of the last three plots.  
2) Make similar plots but for the moons in the data file or include Pluto and see where it fits in.  
3) There are more exoplanet detection methods in the Kepler data files. Make plots of the exoplanets discovered with them and note what sort of planet they are biased towards finding (large Jupiter like, far from the host or perhaps very close - a so called hot Jupiter).

## References

Cynthia Phillips - Planets and Satellites activities [https://www.noao.edu/jagi/sepo/education/plansat/ssgraph1.html](https://www.noao.edu/jagi/sepo/education/plansat/ssgraph1.html)    
Cynthia Phillips - Solar System Parameters [https://www.noao.edu/jagi/sepo/education/plansat/table.html](https://www.noao.edu/jagi/sepo/education/plansat/table.html)    
David R. Williams - NASA Planetary Factsheet [https://nssdc.gsfc.nasa.gov/planetary/factsheet/](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)    
NASA Exoplanet archive, IPAC/Caltech [here - https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html](https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html)

# Data Files

## planets.csv

Data about the planets taken from: David R. Williams - NASA Planetary Factsheet [https://nssdc.gsfc.nasa.gov/planetary/factsheet/](https://nssdc.gsfc.nasa.gov/planetary/factsheet/). See the details on the website for the columns etc.

It also includes data on the Galilean Moons, and Charon from: Cynthia Phillips - Solar System Parameters [https://www.noao.edu/jagi/sepo/education/plansat/table.html](https://www.noao.edu/jagi/sepo/education/plansat/table.html).

## exoplanets.csv and exoplanets_microlensing.csv
These are in the ***exoplanets*** directory

Kepler data from the NASA exoplanet archive see here: NASA Exoplanet archive, IPAC/Caltech [here - https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html](https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html).

# Outputs

Made by **planets.py** found in the ***planets*** directory
![AstroWelcome](radius_vs_distance_planets.png)

Made by **planets.py**
![AstroWelcome](mass_vs_distance_planets.png)

Made by **planets.py**
![AstroWelcome](density_vs_distance_planets.png)

Made by **planets.py**
![AstroWelcome](density_vs_radius_planets.png)

Made by **exoplanets.py** found in the in the ***exoplanets*** directory
![AstroWelcome](radius_vs_distance_exoplanets.png)

Made by **exoplanets_microlensing.py** found in the ***exoplanets*** directory
![AstroWelcome](mass_vs_distance_exoplanets.png)