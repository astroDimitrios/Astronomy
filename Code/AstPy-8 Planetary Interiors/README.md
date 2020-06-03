# Planetary Interiors

## lunar.ipynb
## AIM - To compare our moon image to known data and work out some feature sizes

**Predict**

Have a think about these questions and make some predictions! Be sure to tell someone else what you predict.

1) Do the near and far sides of the moon look the same?    
2) What sort of surface features do you think you can find on the moon?    
3) How do we measure the height of the moon's surface?

## Intro

Annotating your image of the moon based off known data.
Calculating crater heights and depths by first calculating our telescope/camera setups resolution.
Comparing your image to Lunar Reconnaissance Orbiter (LRO) and Lunar Orbiter Laser Altimeter (LOLA) data.

**lunar.ipynb** is the main code to do the three things above.

**catalan.py** creates the gif of the Catalan crater topography using LOLA data stored in ***RDR_272E273E_46p130529S45SPointPerRow_csv_table***. Images used to make the gif outputted by this python script are in the directory ***catalan***.

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
***reference*** - reference for the data

Note Venus and the Gas Giants have no mechanical entries in the csv.
Colours are chosen so the plots look nice.

## geotherm.csv

Data taken from - Professor Bob Downs, University of Arizona, https://www.geo.arizona.edu/xtal/geos306/fall06-10.htm

Used to construct/plot the Earth's geothermal gradient.
***r*** - depth (km)
***r* ***- distance from the center of the Earth (km)
***P*** - pressure at r (GPa)
***T*** - temperature at r (K)

Example output - annotated lunar image
![AstroWelcome](mymoonAnnotated.png)

Example output - crater comparison
![AstroWelcome](theophilusCraterComparison.png)

LROC/LOLA Digital Elevation Model made using GMT
![AstroWelcome](Lunar_LROC_WAC_GLD100_ClrShade_79s79n_9216.jpg)

Gif of the catalan crater topography using LOLA data
![AstroWelcome](catalan.gif)