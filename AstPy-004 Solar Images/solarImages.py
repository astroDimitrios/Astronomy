# © Dimitrios Theodorakis GNU General Public License v3.0 https://github.com/DimitriosAstro/Astronomy
## Introduction to the Sun

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.gridspec as gridspec
import matplotlib.colors as colors
import astropy.units as u
from astropy.utils.exceptions import AstropyWarning
import warnings
import glymur
warnings.simplefilter('ignore', category=AstropyWarning)


## Today's Sun

# We are going to use a python package called SunPy to look at images of the sun from SDO and other telescopes.
# Let's load SunPy now:

# conda install -c sunpy glymur
# pip install sunpy zeep drms sqlalchemy
import sunpy.map
from sunpy.database.tables import display_entries
from sunpy.net import Fido, attrs as a
from sunpy.database import Database
from sunpy.io.file_tools import read_file
from sunpy.timeseries import TimeSeries
from sunpy.data.sample import NOAAINDICES_TIMESERIES as noaa_ind
import sunpy.data.sample as sample_data

# We can use the Helioviewer to get a Jpeg of the Sun from today:

from sunpy.net.helioviewer import HelioviewerClient
hv = HelioviewerClient()  
sun = hv.download_jp2('2020/05/06', observatory="SDO", instrument="HMI", measurement="continuum") 
hmiC = sunpy.map.Map(sun)
hmiC.peek()

# Here we have specified the telescope, SDO, the instrument/camera, HMI, and the measurement to plot, continuum.
# To view the full list of options we can print the data sources available to us like this:

print(hv.data_sources)

# Let's clean up this plot and make it the orange/yellow colour we see visually.

fig = plt.figure(1)
ax = plt.subplot(111, projection=hmiC)
ax.set_axis_off()
cmap = plt.get_cmap('afmhot')
hmiC.plot(cmap=cmap, annotate=False)
plt.clim(0,300)
plt.show()

# Now compare your awesome image with the HMI Intensitygram on https://sdo.gsfc.nasa.gov/data/.
# Intensitygrams show how bright the sun is over it's surface. You'll also see a flattened version on the SDO website.
# The flattened image takes into account the fact that most of the light from the sides of the sun as we see it is not directed towards us. 
# This makes the sun look darker near the edges like in our image. This effect is called limb darkening.

## Multiwavelength Images

# We know that the sun emits many wavelengths of electromagnetic radiation lets get some images for the different parts of the EM spectrum.
# We've already seen a continuum or white light image of the sun that we colourised at the begining of the Notebook.
# To store our new data we are going to start a database which wil help us manage the observations we download:

db = Database('sqlite:///sunpydata.sqlite')
db.default_waveunit = 'angstrom' 

# You'll notice a file called sunpydata.sqlite has appeared in our directory.
# This is our database. Let's download something to fill it.
# Science ready data from spacecraft is not available instantly so we will have to get information from a while back.

result = Fido.search(a.Time('2019/05/06 12:00', '2019/05/06 12:01'),a.Instrument('aia'),a.vso.Sample(2*u.minute),a.Wavelength(94*u.angstrom)|a.Wavelength(131*u.angstrom)|a.Wavelength(171*u.angstrom)|a.Wavelength(193*u.angstrom)|a.Wavelength(211*u.angstrom)|a.Wavelength(304*u.angstrom)|a.Wavelength(335*u.angstrom)|a.Wavelength(1600*u.angstrom)|a.Wavelength(4500*u.angstrom))
print(result)

# You should see a load of tables with the results from our search.
# Each table is for a different wavelength we specified in Angstrom (10E-10 m).
# We searched images from the SDO instrument AIA, and set a.vso.Sample() greater than the time period we searched.
# This meant we only get one image for each wavelength in that time period (which is only 2 minutes to begin with!).
# We can now download the data.

download = Fido.fetch(result,path="./data/")

# Now the data is downloaded you should see a folder called data with a bunch of fits files inside.
# FITS stands for Flexible Interchangeable Transport System. It is the de facto image format for astronomy.
# The image contains a "header" which contains information about the image.
# HMI images have been downloaded for you and are already in the folder (using the online search form https://vso.nascom.nasa.gov/cgi-bin/search).
# Let's add the fits in our folder to the database.

db.add_from_dir("./data/", ignore_already_added=True,time_string_parse_format="%d/%m/%Y") 

# Let's see what's now in our database:

for database_entry in db:
    if database_entry.observation_time_start is None and database_entry.observation_time_end is None:
        db.remove(database_entry)
print(display_entries(db,['id', 'observation_time_start','instrument', 'wavemin']))

# We can now search the database. Here we are searching for images in wavelengths between 1-2 nm or 10-20 Angstrom.
# We have also chosen to sort our results by wavlength!

print(display_entries(db.search(a.Wavelength(1.0*u.nm, 2.0*u.nm)),['id', 'observation_time_start', 'instrument', 'wavemin'], sort=True))

# Another way to fetch data is to use:
# entries = db.fetch(a.Time('2019/05/06 12:00', '2019/05/06 12:01'),a.Instrument('aia'),a.vso.Sample(2*u.minute),a.Wavelength(94*u.angstrom))
# This automatically adds the observations to our database and downloads files checking for duplicates.

# Now we have our images let's plot them!

AIA = db.search(a.Wavelength(.1*u.nm, 60.0*u.nm))
AIAplotDic = {}
for obs in AIA:
    AIAplotDic[int(obs.wavemin*10)] = [obs.path,"sdoaia"+str(int(obs.wavemin*10))]

# fig = plt.figure(num=3, figsize=(len(AIA)*2,2))
# count = 1
# for im in sorted(AIAplotDic.keys()):
#     smap = sunpy.map.Map(AIAplotDic[im][0])
#     fig.add_subplot(1,len(AIA),count,projection=smap).set_axis_off()
#     ax = plt.gca()
#     ax.set_title(str(im)+r" $\AA$",pad=5)
#     cmap = plt.get_cmap(AIAplotDic[im][1])
#     smap.plot(cmap=cmap, annotate=False)
#     count +=1
#
# fig.subplots_adjust(hspace=0, wspace=0)

# or
# whitespace seems to be to do with sunPy ...

fig = plt.figure(num=3, figsize=(len(AIA)*2,2))
count = 0
gs1 = fig.add_gridspec(1,len(AIA), wspace=0.00, hspace=0.0)
for im in sorted(AIAplotDic.keys()):
    smap = sunpy.map.Map(AIAplotDic[im][0])
    ax1 = plt.subplot(gs1[count],projection=smap)
    ax1.set_title(str(im)+r" $\AA$",pad=5)
    cmap = plt.get_cmap(AIAplotDic[im][1])
    smap.plot(axes=ax1, cmap=cmap, annotate=False, clip_interval=(0.1, 99.9)*u.percent)
    ax1.set_axis_off()
    count +=1

plt.show()
# plt.savefig("sunAIA.png", dpi=300, bbox_inches='tight')

# Wow! Look at all those images. We have false coloured the data using the SDO colourmaps SunPy provides.
# Let's load one which has been edited in photoshop so they're not all on one row:

# Load image sunAIAstacked.png

# The shortest uv wavelength of 94 Angstrom (9.4 nm, on the verge of being a soft x-ray) is on the top left with the longest on the bottom right.
# All of these images are uv except the botto left which at 450 nm is in the purple/blue end of the visisble spectrum.
# You can see the granules most clearly in the 1600 Angstrom image. You should also be able to see a sunspot on the left side of the disk.
# We know that sunspots are seen in areas with strong magnetic fields (high magnetic field flux - see more), let's now plot the HMI instrument's magnetogram data that was provided for you.

HMI = db.search(a.vso.Instrument("HMI_FRONT2"))
HMIplotDic = {}
cmapCount = 0
cmaps = ['afmhot', 'hmimag', 'kcor']
for obs in HMI:
    HMIplotDic[obs.path.split(".")[-2]] = [obs.path,cmaps[cmapCount]]
    cmapCount += 1

fig = plt.figure(num=4, figsize=(len(HMI)*2,2))
count2 = 0
gs1 = fig.add_gridspec(1,len(HMI), wspace=0.00, hspace=0.0)
for im in HMIplotDic.keys():
    hmi_map = sunpy.map.Map(HMIplotDic[im][0])
    ax2 = plt.subplot(gs1[count2],projection=hmi_map)
    ax2.set_title(im,pad=5)
    cmap = plt.get_cmap(HMIplotDic[im][1])
    hmi_rotated = hmi_map.rotate(order=3)
    if im == "continuum":
        cont = hmi_rotated.plot(axes=ax2, cmap=cmap, annotate=False, clip_interval=(0.1, 99.9)*u.percent)
        cont.set_clim(0,70000)
    elif im == "magnetogram":
        hmi_rotated.plot_settings['norm'] = plt.Normalize(-1000, 1000)
        hmi_rotated.plot(axes=ax2, cmap=cmap, annotate=False)
    else:
        hmi_rotated.plot(axes=ax2, annotate=False, clip_interval=(0.1, 99.9)*u.percent)
    ax2.set_axis_off()
    count2 +=1

plt.show()
# plt.savefig("sunHMI.png", dpi=300, bbox_inches='tight')

# The three images we see here are a continuum image (like the intensitygram we plotted at the start) of the photosphere, a map of the photosphere's magnetic field, and a map of the solar surface velocity.
# We had to rotate these images to align them with AIA ones because the two instruments are orientated differently on the spacecraft.

## Solar Corona

# We can also use SunPy to look at pictures of the solar corona.
# The SOHO telescope has three detectors (C1,C2,C3) on its LASCO instrument which image the corona in different wavelengths and distances from the photosphere.
# Let's get an image from the LASCO C1 detector:

coronaSOHO = Fido.search(a.Time('2000/02/27 07:42', '2000/02/27 07:43'), a.Instrument('LASCO'), a.Detector('C3'))
# I is a good idea to print this search before attempting to download it
# This will help you check that you're not downloading tons of files or no files

coronaSOHOdata = Fido.fetch(coronaSOHO[0],path="./lascoData/")
data, header = read_file(coronaSOHOdata[0])[0]

header['CUNIT1'] = 'arcsec'
header['CUNIT2'] = 'arcsec'

coronamap = sunpy.map.Map(data, header)
fig = plt.figure(4)
axSOHO = plt.subplot(111, projection=coronamap)
axSOHO.set_title("LASCO C3")
lasco = coronamap.plot(annotate=False, norm=colors.LogNorm(), clip_interval=(25.0, 99.5)*u.percent)
# lasco.set_clim(0,8000)
axSOHO.set_axis_off()
plt.colorbar()
plt.show()

# The black line in some of the images you see from LASCO are from the arm that holds a disc which blocks out the light from the solar disk.
# If you didn't block out the main light from the sun it would overpower the light from the corona and it wouldn't be visible.
# Look closely enough and you'll see a loop in the corona at the top! Try adjusting some numbers in the clip_interval and adding the set_clim() command to make it pop out more.

## Sunspots and Flares

# Flares are best seen near the edge of the solar disk where we see them extending out into space.
# SunPy can be used to visualise these flares. The following code snippet from the SunPy Docs here shows a M2.5 flare that occured on the 7th of June 2011.

aia_cutout03_map = sunpy.map.Map(sample_data.AIA_193_CUTOUT03_IMAGE)
fig = plt.figure(5)
ax = fig.add_subplot(111, projection=aia_cutout03_map)
aia_cutout03_map.plot()
plt.show()

# I enourage you to delve into the documentation for this code snippet. You will find examples there of plotting the x-ray flux for the event and creating a series of images showing how the flares shape changed over time.
# We saw sunspots on our earlier images. Let's use SunPy to plot NOAA data for the number of sunspots as a function of time.

ts_noaa_ind = TimeSeries(noaa_ind, source='NOAAIndices')

fig = plt.figure(6)
plt.ylabel('Sunspot Number')
plt.xlabel('Time')
plt.title('Sunspots Time Series')
plt.plot(ts_noaa_ind.data['sunspot SWO'])
plt.show()

# The sun has a 11 year cycle which you can see from the graph.
# You can also see that sunspot activity at the peak of the cycle has been decreasing over the last two decades.
# Visit the docs here to see this code snippet and the smoothed (time averaged) version of this series.

## Challenge

# 1) Make LASCO plots for the other detectors
# 2) Make an animation of the flare shown above using the code in the SunPy docs
# 3) Make a graph of sunspot number vs time from the 19th century to today using:
#    http://www.sidc.be/silso/datafiles

## References and Resources

# SunPy - https://sunpy.org/
# Pereria, T. M. D., https://folk.uio.no/tiago/teaching/ast2210/sunpy_aia/ - Sunspot animations
# Sunspot Number Data - SILSO, Royal Observatory of Belgium, http://www.sidc.be/silso/datafiles

# Source keywords for searches - https://sdac.virtualsolar.org/cgi/show_details?keyword=SOURCE
# Instrument keywords for searches - https://sdac.virtualsolar.org/cgi/show_details?instrument=HMI

# SDO Images from today - https://sdo.gsfc.nasa.gov/data/
# HMI Instrument page - http://hmi.stanford.edu/