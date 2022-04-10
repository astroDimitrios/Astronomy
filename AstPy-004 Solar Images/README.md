# Solar Images

***Note*** - might not work on tryJupyter since it requires the SunPy module. Works well on a local environment built for SunPy or with a custom JupyterHub env! - use the ***sun.yml*** file for an example conda environment.

## AIM - To access image data on the sun and visualise it in different wavelengths

**Predict**

Have a think about these questions and make some predictions! Be sure to tell someone else what you predict.

1) Do you think the sun looks the same in all wavelengths?  
2) Are there parts of the sun we can only see in certain wavelengths?    
3) How do astronomers deal with such a large amount of data?  

## Intro

Getting data from SDO and SOHO using the SunPy module.

**solarImages.py** creates all the images.

**sun.yml** is a basic env setup that I used to test the code.

The lasco data is separate because it's not in the standard FITS format.

Some images you can make with the code:

SDO AIA:

![AstroWelcome](sunAIAstacked.png)

SDO HMI:

![AstroWelcome](sunHMI.png)

SOHO LASCO C3:

![AstroWelcome](sunLASCOC3.png)
