# Planetary Atmospheres

## atmosphere.ipynb
## AIM - Visualise the atmospheric composition of planets

**Predict**

Have a think about these questions and make some predictions! Be sure to tell someone else what you predict.

1) How do we know what the atmospheres of other planets contain?    
2) Do all the rocky planets have similar atmospheres?     
3) Do all planets have atmospheres?  

## Intro

Creating figures of the composition of planetary atmospheres.  
Comparing the compositions of planetary atmospheres.  
Calculating whether certain gases are retained by the planet or whether they escape into space.

**atmospheres.py** makes all the stacked bar chart compositional plots for the planets.  
**chemical_dist.py** makes the plots of the abundance of one gas in the atmospheres of all planets.  
**exobase.py** makes the plot of escape velocity vs temperature.

## Challenges

1) Tidy up your plots to make them more readable.  
2) Find data for the Galilean moons and perhaps also Titan (Saturn's moon). What are their atmospheres made of?  
3) Calculate the lightest gas particle which can remain in Mercurys atmosphere.

## References

Data from:  
Rauf KM et al. (2015) Comparing the Atmospheric Compositions of All Planets and Giant Moons in Solar System [https://www.longdom.org/open-access/comparing-the-atmospheric-compositions-of-all-planets-and-giant-moons-in-solar-system-2332-2519-1000136.pdf](https://www.longdom.org/open-access/comparing-the-atmospheric-compositions-of-all-planets-and-giant-moons-in-solar-system-2332-2519-1000136.pdf)  

Exobase data from:  
A. Garcia Munoz et al - Upper Atmospheres and Ionospheres of Planets and Satellites [https://arxiv.org/ftp/arxiv/papers/1712/1712.02994.pdf](https://arxiv.org/ftp/arxiv/papers/1712/1712.02994.pdf)

Galileo Probe:  
Alvin Seiff et al. (1998) Thermal structure of Jupiter's atmosphere near the edge of a 5‐μm hot spot in the north equatorial belt [https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/98JE01766](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/98JE01766)

Further Reading:  
The Composition of the Atmosphere of Jupiter [https://lasp.colorado.edu/home/mop/files/2015/08/jupiter_ch4-1.pdf](https://lasp.colorado.edu/home/mop/files/2015/08/jupiter_ch4-1.pdf)  
David A. Weintraub - Escape Velocity [https://www.vanderbilt.edu/AnS/physics/astrocourses/ast201/esc_vel_atmospheres.html](https://www.vanderbilt.edu/AnS/physics/astrocourses/ast201/esc_vel_atmospheres.html)  
Peter Gallagher - Planetary Atmospheres [https://www.tcd.ie/Physics/people/Peter.Gallagher/lectures/PY4A03/pdfs/PY4A03_lecture12n13_amospheres.ppt.pdf](https://www.tcd.ie/Physics/people/Peter.Gallagher/lectures/PY4A03/pdfs/PY4A03_lecture12n13_amospheres.ppt.pdf)  
A. J. Coates - Atmospheric escape [https://sci.esa.int/documents/33745/35957/1567258799920-Weihai-093-Coates-escape.pdf](https://sci.esa.int/documents/33745/35957/1567258799920-Weihai-093-Coates-escape.pdf)  
Catling and Zahnle (2009) The escape of planetary atmospheres [https://geosci.uchicago.edu/~kite/doc/Catling2009.pdf](https://geosci.uchicago.edu/~kite/doc/Catling2009.pdf)  
Nick Strobel (2020) Escape Velcoity [http://www.astronomynotes.com/solarsys/s3.htm](http://www.astronomynotes.com/solarsys/s3.htm)

# Data Files

## atmospheres.csv

Data from Rauf KM et al. (2015) Comparing the Atmospheric Compositions of All Planets and Giant Moons in Solar System [https://www.longdom.org/open-access/comparing-the-atmospheric-compositions-of-all-planets-and-giant-moons-in-solar-system-2332-2519-1000136.pdf](https://www.longdom.org/open-access/comparing-the-atmospheric-compositions-of-all-planets-and-giant-moons-in-solar-system-2332-2519-1000136.pdf) 

Contains percentage compositions for different gases in the atmospheres of the planets + Pluto.

## exobase.csv

From A. Garcia Munoz et al - Upper Atmospheres and Ionospheres of Planets and Satellites [https://arxiv.org/ftp/arxiv/papers/1712/1712.02994.pdf](https://arxiv.org/ftp/arxiv/papers/1712/1712.02994.pdf)

Contains data on the exobase (bottom layer of the exosphere) for the planets and Titan.

***object*** - name of the object
***exobase alt*** - altitude in the atmosphere of the exobase (km)
***exobase alt range*** - if the value in the paper was given as a range ***exobase alt*** is the center value and this column contains the range either side of possible values (similar to a +- error but I hesitate to call it that) in km
***exobase temp high*** - max temp of the exobase in K (daytime)
***exobase temp low*** - min temp of the exobase in K (nightime) - sometimes this is the same as the high value
***esc vel*** - the escape velocity of the planet in km/s

Note the temperatures for Mercury are average surface temperatures since it has no appreciable atmosphere.

For information on the **planets.csv** which is present here see the ***Data*** or ***AstPy-8 Planets*** directories.

## earth_chem_crust.csv

Chemical composition of the crust.
Taken from: CRC Handbook of Chemistry and Physics, 97th Edition (2016-2017)

# Outputs

Atmospheric composition of the Earth
![AstroWelcome](./figures/Earths_Atm_comp.png)

Percentage composition of water vapour in planetary atmospheres
![AstroWelcome](./figures/chem_H2O_atm_planet_comp.png)

Escape velocity vs temperature
![AstroWelcome](./figures/atm_retention.png)