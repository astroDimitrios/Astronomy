# Planetary Interiors

## interior.ipynb
## AIM - Visualise the interiors of planets, know how scientists build a picture of planetary interiors, explore the chemical composition of Earth

**Predict**

Have a think about these questions and make some predictions! Be sure to tell someone else what you predict.

1) How do we know what the interiors of planets look like?  
2) Are all planets interiors the same? Can you compare the rocky and gas giant planets?    
2) What layers does the moon have? Is it similr to any of the planets? 

## Intro

Creating figures of compositional and mechanical layers for all the planets and the moon.  
Comparing the interiors of the planets.  
Comparing the abundance of elements in the Earth's layers.

**structure_plots.py** makes all the plots in the ***figures*** directory (minus the chemical abundace figures).  
**int_chem.py** creates the chemical abundace plots shown at the end of this readme.

## Challenges

1) Re-create any of the images above (my code can be found in **structure_plots.py** if you need help).  
2) Find data for the Galilean Moons and make similar interior plots for them.  
3) Make a plot that shows the difference between oceanic and continental crust clearly.  
4) Plot some chemical data for the moon and other rocky planets using Chapter 8 of Planetary Science: A Lunar perspective [here](https://www.lpi.usra.edu/publications/books/planetary_science/chapter8.pdf)

## References

Ken Rubin - How do scientists know what's in the core of the Earth? [https://www.soest.hawaii.edu/GG/ASK/earths_core.html](https://www.soest.hawaii.edu/GG/ASK/earths_core.html)  
Eleanor Lutz- Topographic Maps of the Planets and Moons, [https://github.com/eleanorlutz/topography_atlas_of_space](https://github.com/eleanorlutz/topography_atlas_of_space)  
Katharina Lodders - Composition of planets and properties of protoplanetary disks (2009), [https://www.tat.physik.uni-tuebingen.de/~fgp/Conf09/Contributions/talk_Lodders_Tuebingen09.pdf](https://www.tat.physik.uni-tuebingen.de/~fgp/Conf09/Contributions/talk_Lodders_Tuebingen09.pdf)

## Acknowledgements

Thanks to Cameron Davidson for his help identifying the difference between compositional and mechanical layers and sending over helpful figures [https://apps.carleton.edu/profiles/cdavidso/](https://apps.carleton.edu/profiles/cdavidso/).

# Data Files

## structure.csv

Adapted from - Eleanor Lutz, Tabletop Whale, https://github.com/eleanorlutz/topography_atlas_of_space

Data on the thickness of layers in the planets.  
***object*** - name of object  
***color*** - hex colour (for plotting)  
***layer_type*** - ```'compositional'``` or ```'mechanical'``` (NA for Gas Giants)  
***atm*** - ```'y'``` or ```'n'``` is the layer an atmospheric layer  
***name*** - name of layer  
***color_simp and name_simp*** - simplified names and colours for multiplanet plotting (leads to less legend entries)  
***depth_order*** - layer number with 0 for the core  
***depth*** - height/depth of that layer (km)  
***depth_from_core*** - the distance from the centre of the object to the top of the current layer (km)  
***reference*** - reference for the data (Earth data not too sure on taken from hyperphysics mainly)  

Note Venus and the Gas Giants have no mechanical entries in the csv.
Colours are chosen so the plots look nice.
Earth radius is just aboe the actual radius if you google it but this is because the Earth isn't a perfect sphere and I used a value for continental crust in the csv not oceanic (which is ~10 km not 30 km).

## earth_chem_interior.csv

The chemical compostion of the Earth.
Only some elements included. Some Oxygen data is missing. Values in %.

Rows for:  
Bulk  
Core  
Lower Mantle  
Upper Mantle  
Crust

Data taken from:  
Don L. Anderson (1998) Theory of the Earth, Chapter 8, [https://authors.library.caltech.edu/25018/9/TOE08.pdf](https://authors.library.caltech.edu/25018/9/TOE08.pdf)  
Claude J. Allegre et al (1995) The chemical composition of the Earth, [https://www.researchgate.net/publication/222035431_The_Chemical-Composition_of_the_Earth](https://www.researchgate.net/publication/222035431_The_Chemical-Composition_of_the_Earth)  
Frederick K. Lutgens and Edward J. Tarbuck (2000) Essentials of Geology 7th Edition

## earth_chem_crust.csv

Chemical composition of the crust.
Taken from: CRC Handbook of Chemistry and Physics, 97th Edition (2016-2017)

# Outputs

Do not make **structure_plots.py** create all the figures as once as it might overplot some axes and give a matplotlib depreciation warning.

Interior Comparisons (Compositional Layers)
![AstroWelcome](./figures/rocky_interiors_compositional_simpLegend.png)

Compositional and Mechanical Layers Comparison
![AstroWelcome](./figures/comp_vs_mech/earth_comp_vs_mech.png)

Compositional Layers (right side is adjusted so all layers are visible)
![AstroWelcome](./figures/compositional/earth_compositional_interior_both.png)

Mechanical Layers (right side is adjusted so all layers are visible)
![AstroWelcome](./figures/mechanical/earth_mechanical_interior_both.png)

Abundance of elements in the Earth's continental crust made using **int_comp.py**
![AstroWelcome](./figures/elem_comp_crust_earth.png)

Inspiration for this last figure was taken from this USGS fact sheet on Rare Earth Elements - [https://pubs.usgs.gov/fs/2002/fs087-02/](https://pubs.usgs.gov/fs/2002/fs087-02/)