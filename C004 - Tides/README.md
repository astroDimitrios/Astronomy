# Winter 2020/2021 Challenge - Tides

Earth has one Moon, Mars two, and Tatooine three! If Mars and Tatooine had oceans of water on them what would the tides be like?

Start by simulating the tides of the Earth - Moon system then move onto Mars!
If you want to stretch to three moons/Tatooine then you will have to make up values for distances etc of the moons.

## Solution

My code is in **tides.py** it has been set up for the Earth, Moon, and Sun system at the moment.

Possible improvements:

* Make code check for previously calculated values of tides from more than one body to use. So if you want the tides from the Sun+Moon+Jupiter it will only look for 'Sun', 'Moon' etc and not 'Sun+Moon' so it's missing an apportunity to use some previously calculated values.

* Add a dict with planets etc and their data inside so people don't have to input values manually.

The **plot_tides.py** code makes this plot and is easily adapted:

<p align="center">
    <img width="80%" src="https://github.com/astroDimitrios/Astronomy/blob/master/Code/C004%20-%20Tides/Tides_Moon_0.png">
</p>

These are some of the figures I made to help me solve the challenge as well as the whiteboard image in the Working Directory (which has some mistakes in relation to the sign preservation section).

<p align="center">
    <img width="80%" src="https://github.com/astroDimitrios/Astronomy/blob/master/Code/C004%20-%20Tides/Images/Tides_Diff-100.jpg">
</p>

<p align="center">
    <img width="80%" src="https://github.com/astroDimitrios/Astronomy/blob/master/Code/C004%20-%20Tides/Images/Tides_Simple_Maths-100.jpg">
</p>

<p align="center">
    <img width="80%" src="https://github.com/astroDimitrios/Astronomy/blob/master/Code/C004%20-%20Tides/Images/Tides_Offset-100.jpg">
</p>

<p align="center">
    <img width="80%" src="https://github.com/astroDimitrios/Astronomy/blob/master/Code/C004%20-%20Tides/Images/Tide_Comp.gif">
</p>