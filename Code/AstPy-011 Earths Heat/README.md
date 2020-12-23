# Earth's Heat

## thermal.ipynb
## AIM - Explore the Earth's thermal gradient, describe how heat is transferred and where it's from, perform simple thermal calculations

**Predict**

Have a think about these questions and make some predictions! Be sure to tell someone else what you predict.

1) How hot is the Earth's interior?  
2) Where does this thermal energy come from?  
3) How does the heat get transferred throughout the Earth? 

## Intro

Explore a model of the geothermal gradient for the lithosphere.  
Visualise the whole geothermal gradient.  
Perform simple calculations on the energy transferred via conduction and latent heat.

**thermal.py** makes the figure of the Earth's thermal gradient (geotherm figure).

## Challenge

1) Use structure.csv to recreate my figure of the geotherm that we loaded earlier (use structure.csv to plot the layers).  
2) Calculate the Rayleigh number for the mantle (and possibly the crust).  
3) Simulate conduction from the mantle to a rigid lithosphere using Newton's Law of Cooling (see an example with a teacup [here](http://greenteapress.com/modsimpy/ModSimPy3.pdf) - some beginning guidance is in **thermal.py**).

## References

Cameron Davidson - Geothermal Gradients Activity [https://serc.carleton.edu/NAGTWorkshops/petrology/teaching_examples/24418.html](https://serc.carleton.edu/NAGTWorkshops/petrology/teaching_examples/24418.html)  
John Merck - Sources and movement of heat within planets [https://www.geol.umd.edu/~jmerck/geol212/lectures/10.html](https://www.geol.umd.edu/~jmerck/geol212/lectures/10.html)  
Marcus Bursik - The Earth's Heat and Temperature [http://www.glyfac.buffalo.edu/mib/class/325/Lecture/14/1401Thermal/thermal.html](http://www.glyfac.buffalo.edu/mib/class/325/Lecture/14/1401Thermal/thermal.html)  
Professor Bob Downs, University of Arizona, [https://www.geo.arizona.edu/xtal/geos306/fall06-10.htm](https://www.geo.arizona.edu/xtal/geos306/fall06-10.htm)  
Antoine Rozel - Thermal Structure of the Earth [http://jupiter.ethz.ch/~gfdteaching/dymali/2017/downloads/dymali-Lecture1-ThermalStructure.pdf](http://jupiter.ethz.ch/~gfdteaching/dymali/2017/downloads/dymali-Lecture1-ThermalStructure.pdf)

## Acknowledgements

Thanks to [Cameron Davidson](https://apps.carleton.edu/profiles/cdavidso/) for help understanding his geothermal gradients activity and answering all my questions.

# Data Files

## geotherm.csv

Data taken from - Professor Bob Downs, University of Arizona, https://www.geo.arizona.edu/xtal/geos306/fall06-10.htm

Used to construct/plot the Earth's geothermal gradient.  
***r*** - depth (km)  
***r\****- distance from the center of the Earth (km)  
***T*** - temperature at r (K)  

I have altered the T profile from the original to be consistent with the D" layer depth (In the original file the core mantle boundary temp change occurred at too low a depth). The original data is in **geotherm_original.csv**. The original also has pressure vs depth data.

## structure.csv

Contains information about the layers of the planets.
See ***AstPy-9 Planetary Interiors*** for more information or the ***Data*** directory.

# Outputs

Geothermal Gradient of the Earth
![AstroWelcome](./geotherm.png)
