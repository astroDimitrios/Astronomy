# Data

Description of the data files kept in this directory.

To keep this readme short you can find column descriptions in the datas associated **.txt** file or linked below.

## Catalan - now stored [here](https://drive.google.com/drive/folders/1kXCnfm2d2YGzs8HBQrQYu388HK6nvkzc?usp=sharing)

Lunar Orbiter Laser Altimeter (LOLA) data for the Catalan crater on the moon.
Individual .lbl files are in the directory for each .csv file.
[https://ode.rsl.wustl.edu/moon/indextools.aspx](https://ode.rsl.wustl.edu/moon/indextools.aspx)

## LOLA DEM - now stored [here](https://drive.google.com/drive/folders/1kXCnfm2d2YGzs8HBQrQYu388HK6nvkzc?usp=sharing)

Lunar Orbiter Laser Altimeter (LOLA) digital elevation model of the moon details in directory.

## Nuclear

Atomic data (mass, binding energy etc of isotopes) from the Atomic Mass Data Center ([AMDC](http://amdc.impcas.ac.cn/filel.html)).
**mass16Abundant.csv** is the same but with only the most abundant isotope of each element.

## Planetary

This directory contains csvs on the ring structures of the gas giants and their satellites.

## atmospheres.csv

Data from Rauf KM et al. (2015) Comparing the Atmospheric Compositions of All Planets and Giant Moons in Solar System [https://www.longdom.org/open-access/comparing-the-atmospheric-compositions-of-all-planets-and-giant-moons-in-solar-system-2332-2519-1000136.pdf](https://www.longdom.org/open-access/comparing-the-atmospheric-compositions-of-all-planets-and-giant-moons-in-solar-system-2332-2519-1000136.pdf) 

Contains percentage compositions for different gases in the atmospheres of the planets + Pluto.

## earth_chem_crust.csv

Chemical composition of the crust.
Taken from: CRC Handbook of Chemistry and Physics, 97th Edition (2016-2017)

## earth_chem_interior.csv

The chemical compostion of the Earth.
Only some elements included. Some Oxygen data is missing. Values in %.

Rows for: Bulk, Core, Lower Mantle, Upper Mantle, and the Crust.

Data taken from:  
Don L. Anderson (1998) Theory of the Earth, Chapter 8, [https://authors.library.caltech.edu/25018/9/TOE08.pdf](https://authors.library.caltech.edu/25018/9/TOE08.pdf)  
Claude J. Allegre et al (1995) The chemical composition of the Earth, [https://www.researchgate.net/publication/222035431_The_Chemical-Composition_of_the_Earth](https://www.researchgate.net/publication/222035431_The_Chemical-Composition_of_the_Earth)  
Frederick K. Lutgens and Edward J. Tarbuck (2000) Essentials of Geology 7th Edition

## exobase.csv

From A. Garcia Munoz et al - Upper Atmospheres and Ionospheres of Planets and Satellites [https://arxiv.org/ftp/arxiv/papers/1712/1712.02994.pdf](https://arxiv.org/ftp/arxiv/papers/1712/1712.02994.pdf)

Contains data on the exobase (bottom layer of the exosphere) for the planets and Titan.  
Note the temperatures for Mercury are average surface temperatures since it has no appreciable atmosphere.

## exoplanets.csv

NASA exoplanet archive data.
[https://exoplanetarchive.ipac.caltech.edu/docs/API_exoplanet_columns.html](https://exoplanetarchive.ipac.caltech.edu/docs/API_exoplanet_columns.html)

## exoplanets_microlensing.csv

NASA exoplanet archive data. Exoplanets discovered using microlensing.
[https://exoplanetarchive.ipac.caltech.edu/docs/API_microlensing.html](https://exoplanetarchive.ipac.caltech.edu/docs/API_microlensing.html)

## geotherm.csv

Geothermal and pressure gradient for the Earth. Taken from [here - https://www.geo.arizona.edu/xtal/geos306/fall06-10.htm](https://www.geo.arizona.edu/xtal/geos306/fall06-10.htm) and adapted. Original is in geotherm_original.csv.

## int_std_atm.csv

Data to construct the international standard atmosphere model.  
Taken from the ISA wikipedia page [here](https://en.wikipedia.org/wiki/International_Standard_Atmosphere).

## planets.csv

Planetary data (including our Moon, the Galilean moons, and Pluto/Charon) taken from NASA Planetary factsheet [here](https://nssdc.gsfc.nasa.gov/planetary/factsheet/) and [here - https://www.noao.edu/jagi/sepo/education/plansat/table.html](https://www.noao.edu/jagi/sepo/education/plansat/table.html).

## structure.csv

Layers in planetary interiors and their thicknesses.
Taken from [here - https://github.com/eleanorlutz/topography_atlas_of_space](https://github.com/eleanorlutz/topography_atlas_of_space) and adapted (see other sources in the file).
