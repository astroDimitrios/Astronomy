# Ring Dynamics

## ringDynamics.ipynb
## AIM - Visualise the Roche limit, identify resonances, and explain shepherding

**Predict**

Have a think about these questions and make some predictions! Be sure to tell someone else what you predict.

1) What effects the shape of the rings?  
2) How are gaps in the rings made?  
3) Do the outer moons of Saturn have an effect on the rings?  

## Intro

Visualise the roche limit using an N-body simulation.  
Calculate the resonances between moons and the resonance locations between moons and ring particles for Saturn.  
Briefly look at shepherd moons!

**res.py** has my test code for calculating resonances  
***testing*** has code and figures from my N-body simulations  
***Images*** has useful images for the activity  
***Articles*** has two articles - the Larson article and the Shane presentation (see the references)  

***myimages*** contains images that the students create during the activity when visualising the roche limit

## Challenges:

1) Identify features related to resonances with Enceladus. Are there any?  
2) Use the OPUS tool to find images to make a gif of the ripples or a moon moving!  
3) Use rebound or another N-body simulation package to simulate a shepherd moon.  
4) Follow the two ring simulation articles in the references below to create your own ring simulation from first principles.  

## References

Phil Nicholson - Resonances and Rings [http://hosting.astro.cornell.edu/specialprograms/reu2012/workshops/rings/](http://hosting.astro.cornell.edu/specialprograms/reu2012/workshops/rings/)  
Outer Planets Data Search Tool (OPUS3) PDS Ring-Moons Node NASA/SETI [https://opus.pds-rings.seti.org/opus/](https://opus.pds-rings.seti.org/opus/)  
Rebound N-body simulator [https://rebound.readthedocs.io/en/latest/](https://rebound.readthedocs.io/en/latest/)  

Chris Mihos - Ring Dynamics [http://burro.astr.cwru.edu/Academics/Astr221/SolarSys/Rings/dynamics.html](http://burro.astr.cwru.edu/Academics/Astr221/SolarSys/Rings/dynamics.html)  
Matthew Hedman - Planetary Ring Dynamics [https://webpages.uidaho.edu/mhedman/papers_published/UNESCO_dynamics.pdf](https://webpages.uidaho.edu/mhedman/papers_published/UNESCO_dynamics.pdf)     
Shane Byrne - Rings and Moons of Saturn [http://www.lpl.arizona.edu/~shane/PTYS_206/lectures/PTYS_206_saturns_rings_moons.pdf](http://www.lpl.arizona.edu/~shane/PTYS_206/lectures/PTYS_206_saturns_rings_moons.pdf)  

Simulations:  
Cole Kendrick - Computer Simulation of Saturn's Rings [http://courses.physics.ucsd.edu/2018/Winter/physics141/Assignments/SaturnRingSimulation.pdf](http://courses.physics.ucsd.edu/2018/Winter/physics141/Assignments/SaturnRingSimulation.pdf)  
Kirsten Larson - The Effects of Moons on Saturn's Ring System [http://physics.wooster.edu/JrIS/Files/Larson_Web_article.pdf](http://physics.wooster.edu/JrIS/Files/Larson_Web_article.pdf)

## Acknowledgements

Thanks to [Matthew M. Hedman](https://webpages.uidaho.edu/mhedman/) for his advice on ring simulation and locating moon data.

# Data Files

## saturn_moons.csv

Contains data on the moon of Saturn from the rings and moons node of the planetary data system PDS/NASA/SETI. See the corresponding ***txt*** file for more info.

# Outputs

Simulation of the Roche Limit
![AstroWelcome](./Images/roche.gif)

Simulation of a Shepherd Moon
![AstroWelcome](./Images/shepherd.gif)