<p align="center">
    <!-- ![AstroWelcome](/DesignAssets/Ai/LogoMain@2x.png | width=400) -->
    <img width="50%" src="https://github.com/astroDimitrios/AstronomyClass/blob/main/DesignAssets/Ai/LogoMain%402x.png">
</p>

# Astronomy and Python Coding Activities

**Website** - [astropython.com](https://www.astropython.com)
Be sure to check out my website for details on the code, the [astroedu](https://github.com/astroDimitrios/astroedu) package, ways to get involved, and other teaching resources.

My YouTube channel [astroDimitrios](https://www.youtube.com/channel/UCf8Sg-cgLNubyCM5Em8eDZg/featured) has videos of some activities and challenges as well as beginner intro videos.

## Intro

This directory contains code on various Astronomy topics.

The goal of the coding activities are mainly to **process** and **visualise** data and **extract physical insights** from them (as described in the AAPT report below). Although by performing the activities students will inevitably also learn debugging, how to convert theory/models into code, and how to present data formally in a document or presentation.

The outputs (figures etc) were designed to be a starting point for my students to put their own data and visualisations in their reports and presentations. My hope is this will promote a deeper understanding of the topic and better engage the students/encourage ownership and pride in their work.  

Some are best done in pairs like the intro activities. Activities are designed to take at most an hour with some taking an hour and a half (AstPy-004 and AstPy-006 for instance).

Each code has a teacher version with all outputs. These have the suffix Teacher. The student file is much smaller as it is missing the outputs and has code completition tasks for the students to complete.

**Inspiration taken from:**

Adam LaMee - Scientific Computing Resources [https://adamlamee.github.io/CODINGinK12/](https://adamlamee.github.io/CODINGinK12/)    
Brown & Wilson, Ten quick tips for teaching programming, PlosCompBiol, [https://doi.org/10.1371/journal.pcbi.1006023](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006023)  
American Association of Physics Teachers (AAPT), [Computational Physics Report](https://www.aapt.org/Resources/upload/AAPT_UCTF_CompPhysReport_final_B.pdf)  
PICUP, Integrating computing into physics, [https://www.compadre.org/PICUP/webdocs/About.cfm](https://www.compadre.org/PICUP/webdocs/About.cfm)  
astronomycenter resources, [https://www.compadre.org/astronomy/index.cfm](https://www.compadre.org/astronomy/index.cfm)

...and many others, see [here](https://www.astropython.com/code.html).

# Table of code contents

Difficulty based on a three star system. Bear in mind all of these can be adapted to make them harder or easier!

AstPy Number | Difficulty | Description     | Data Files  | Comments
------------ | ---------- | -------------   | ----------- | --------
1 | :star: | Introductory Activities || 10 Intro Activities (in progress)
2 | :star::star: | Intermediate introductory activities || planned
3 | :star::star: | Stellar Fusion | Nuclear masses and binding energies (csv) |  Binding energy anim and calcs including coulomb potential well.
4 | :star: | Solar Images | Various SDO HMI and AIA FITS | Getting and potting SDO/SOHO Images.
5 | :star: | Solar Radiation | | Blackbody rad, Wien's law etc. Effective temperature of planets.
6 | :star::star::star: | Sunspots | SDO HMI Fits | Calculation of solar rotation period (interactive and automatic). Sunspot identification and sunspot tracking (automatic).
7 | :star::star::star: | Lunar Surface | LOLA DEM, LOLA Raw Topographic Data for Catalan Crater | Annotating your image of the moon from a telescope. Calculating resolution, crater heights and diameters. Comparing to Lunar Reconnaissance Orbiter (LRO) and Lunar Orbiter Laser Altimeter (LOLA) data.
8 | :star: | Planets | Orbital data, density, radius, mass etc. | Comparing planets by looking at data from the NASA Planetary Factsheet such as mass and radius etc. Looking briefly at exoplanet detection and observational bias.
9 | :star: | Planetary Interiors | Structure of the planets csv and chemcial composition of the Earth csvs. | Visualising the interiors of planets, visualise the chemical composition of the Earth's interior.
10 | :star::star: | Planetary Atmospheres | Chemical composition of planetary atmospheres. Exobase altitudes and temperatures (with escape velocities).  | Visualising and comparing the chemical composition of planetary atmospheres. Calculating whether a planet can hold onto a gas using escape velocities and kinetic theory.
11 | :star::star: | Earth's Heat| Geothermal gradient data and pressure data.  | Visualise the thermal gradient of the Earth. Model the geotherm of the lithosphere. Calculate energy transfer via conduction and latent heat.
12 | :star::star: | Earth's Atmosphere | Data to construct the international standard atmosphere (ISA) model. | Visualising the temperature, pressure, density, and speed of sound variation with altitude using the ISA model.
13 |  | Martian Surface | | COMING SOON!
14 | :star::star: | Planetary Rings | Data on the ring structure for all gas giants and data on their moons. | Visualising the ring structure of Saturn and the other gas giants. Calculating roche limits for some moons.
15 | :star::star::star:+ | Ring Dynamics | Data on Saturns moons. | Visualising the Roche limit with an N-body simulation. Calculating the locations of mean-motion resonances. Looking at bending and density waves, and the effects of shepherd moons.

# Specials

A folder with an S then a number (S001 for instance) is a special activity.

Special Number |  Description  | Data Files  | Comments
------------ | -----------| -------------   | ----------- 
1 | Celebrate the landing of the Mars 2020 Perseverance Rover by calculating launch windows to Mars with a Hohmann transfer orbit. | Ecliptic longitude and distance data for Earth and Mars | Also includes a notebook which makes the Hohmann transfer rover gif [here](https://github.com/astroDimitrios/Astronomy/blob/master/Code/S001%20-%20Mars%202020%20Launch%20Windows/GIF%20Files/social.gif).
2 | Team Seas - Analyse plastic discharge by rivers using data from the Ocean Cleanup Project | Shapefile of river plastic discharge data |

# Challenges

Astronomy and Python challenge excercises are now stored in the ***Challenges*** directory. As of the 2022 Maintenance Update 1 no new challenges will be issued as I work towards a more impactful way to engage the community, see [here](https://www.astropython.com/challenge.html).

## How to run the code

**2022 Maintenance Update 1**: A basic conda environment file ***env.yml*** is provided which most activities will run in, which is just a normal scientific Python stack with astropy. Some activities have their own ***.yml*** file with extra dependencies.

<p><strong>Testing Activites:</strong>If you would like to test any activities online you can email me and I will activate our JupyterHub server for 48 hours. Unfortunately I can no longer keep it running 24/7 due to running costs. When the server is up - Sign up <a href="https://hub.astropython.com/hub/signup">here</a> with a username and password then head over to <a href="https://hub.astropython.com/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FastroDimitrios%2FLaunch&urlpath=lab%2Ftree%2FLaunch%2FWelcome.ipynb&branch=main">hub.astropython.com</a> and log in! (It's important to use the second link after signing up so you get sent to the Welcome document)

**NOTE:** The server may go down periodically. If you want to keep your work please download it to your local computer, do NOT assume it is safe forever on the hub. 

The welcome document has links which pull the activities you want to try from my GitHub. If something doesn't work please let me know! The server is built for my students so it can only handle 20-30 people at a time. If you do test out some of the activities let me know what you think.</p>

**Alternate ways of running notebooks**

The .ipynb files can be run my going to https://jupyter.org/try.  
Click on **Try JupyterLab** and wait for it to load.  
Upload the **.ipynb** file using the Upload File button (little upwards arrow in the top right).

Or you could install JupyterLab on your local machine.

The **.ipynb** files contain tasks for students. The Teacher **.ipynb** file contains the solutions.

**NOTE** - Sometimes there is a **.py** file with solutions and code to create more complex figures. I have NOT checked that these will run on JupyterLab. They were used to test my code before creating the interactive JupyterLab Notebooks.

## Data

There is now a ***Data*** directory where all data is stored. I will continue to keep all data files needed in their respective assignment directories as well. Some activity data is stored on Google Drive due to large file sizes. Links are given inside the individual activity directories if applicable.

## Assignment grading

**nbgrader**

[nbgrader](https://nbgrader.readthedocs.io/en/stable/index.html) is a tool to make assignments out of notebooks and mark them.

I have integrated this easily with the notebooks - email me for more info. As of 2022 Maintenance Cycle 1 nbgrader files are no longer tracked/uploaded t o this repo.