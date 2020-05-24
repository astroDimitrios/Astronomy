import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as ticker
import numpy as np
import numpy.ma as ma
from math import degrees
from scipy.stats import linregress
from sunpy.net import Fido, attrs as a
import sunpy.map
import astropy.units as u
from stara import stara
from itertools import cycle, islice
import time
import pickle
from astropy.utils.exceptions import AstropyWarning
import warnings
warnings.simplefilter('ignore', category=AstropyWarning)

# Search the database
results = Fido.search(a.Time('2015/05/05 12:00', '2015/05/11 12:00'),a.Instrument('HMI'),a.vso.Sample(0.5*u.day),a.vso.Physobs("intensity"))
# print(results)

# Get the results
files = Fido.fetch(results, path="./images/")
files = sorted(files)
# print(files)

# Save the names of files we downloaded or load them
files = np.asarray(files)
np.save('./data/files.npy', files)
# files = np.load('./data/files.npy')

# Plot the first image
smap = sunpy.map.Map(files[0])
smap = smap.resample((1024, 1024) * u.pix)

fig = plt.figure(1)
ax = fig.add_subplot(projection=smap)
ax.set_axis_off()
smapRot = smap.rotate(order=3)
smapRot.plot(axes=ax, annotate=False)

# # Animation of all images
# fig2 = plt.figure(10)
# mapsequence = sunpy.map.Map('./data/*.fits', sequence=True) 
# def sunspot_anim(i):
#     smap = sunpy.map.Map(mapsequence[i])
#     smap = smap.resample((1024, 1024) * u.pix)
#     smap = smap.rotate(order=3)
#     ax2 = fig2.add_subplot(projection=smap)
#     ax2.set_axis_off()
#     smap.plot(axes=ax2, annotate=False)
# anim = animation.FuncAnimation(fig2, sunspot_anim, frames=len(files), interval=500)
# # anim.save('sunspots.gif', writer='imagemagick', fps=0.5)
# plt.show()

# Find where the sunspots are using stara.py
# returns True for all x,y positions on the image where there is a snunspot
# ie there will be more than one point for one sunspot
spotBool = stara(smap, limb_filter=5 * u.percent)
spots = np.where(spotBool)
# We could plot these now or wait and plot them with which cluster (sunspot) they are in
# ax.scatter(spots[1],spots[0],c='yellow',alpha=0.01)

# Use scikit-learn to identify sunpots
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

spots2D = np.column_stack((spots[0],spots[1]))
clust = DBSCAN(eps=5,min_samples=10).fit(spots2D)
labels = clust.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)
print('Estimated number of sunspots: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)

y_pred = clust.labels_.astype(np.int)
# Colours for up to 9 clusters - black for noise
colors = np.array(['#377eb8','#ff7f00','#4daf4a','#f781bf','#a65628','#984ea3','#999999','#e41a1c','#dede00'])
colors = np.append(colors, ["#000000"])
spots2DRot = 1024 - spots2D
ax.scatter(spots2DRot[:,1], spots2DRot[:,0], s=10, color=colors[y_pred], alpha=0.01)

# plt.show()

def calc_cluster_centre(spots2D,y_pred):
    '''
    Calculates the cluster centre.
    Requires the sunspot points from stara and the cluster id for each point from sklearn
    '''
    clusterPoints = []
    spotsStack = np.column_stack((spots2D,y_pred))
    for i in set(y_pred):
        thisCluster = spotsStack[np.ix_(spotsStack[:,2]==i, (0,1))]
        numCluster = len(thisCluster)
        X = np.sum(thisCluster[:,0])/numCluster
        Y = np.sum(thisCluster[:,1])/numCluster
        clusterPoints.append([X,Y])
    return np.array(clusterPoints)

# Calculates the centre of each cluster
# does not know how to remove outliers etc ie very basic
clusterPoints = calc_cluster_centre(spots2D, y_pred)
clusterPointsRot = 1024 - clusterPoints

ax.scatter(clusterPointsRot[:,1], clusterPointsRot[:,0], color='k', marker='*', s=10, alpha=0.5)

# plt.show() 

# Function to time other functions
def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time()
        print('{} ran in: {:.2f} mins'.format(orig_func.__name__, (t2-t1)/60))
        return result

    return wrapper

# Print function to print out time as well
def printT(string):
    import time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time+' '+string)
    return

@my_timer
def id_sunspots(files, v=False):
    '''
    Function to ID sunspots in a series of fits files
    These should be HMI continuum fits
    Will create a visulaisation of the sunspots if v is given
    v is a string which is the gif filename
    '''
    printT('Function id_sunspots starting')
    ids = {}
    noSunspots = []
    # Mapsequence seems to need a list
    mapsequence = sunpy.map.Map(files.tolist(), sequence=True) 
    printT('Map Sequence Created')
    if v!=False:
        spots2DRots = {}
        y_preds = {}
    printT('Set Up Complete')
    num_files = len(files)
    printT('Number of Files to process: {}'.format(num_files))
    printT('Mapsequence has length: {}'.format(len(mapsequence)))
    for i in range(num_files):
        printT('Processing file {}/{} \n {}'.format(i+1,num_files,files[i]))
        smap = sunpy.map.Map(mapsequence[i])
        smap = smap.resample((1024, 1024) * u.pix)
        spotBool = stara(smap, limb_filter=5 * u.percent)
        if (spotBool==True).any():
            printT('Identified Sunspots')
            spots = np.where(spotBool)
            spots2D = np.column_stack((spots[0],spots[1]))
            # printT('Performing Cluster Analysis')
            clust = DBSCAN(eps=5,min_samples=10).fit(spots2D)
            # printT('Finished Cluster Analysis')
            labels = clust.labels_
            n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
            if n_clusters_ != 0:
                print('Estimated number of sunspots: %d' % n_clusters_)
                # n_noise_ = list(labels).count(-1)
                # print('Estimated number of noise points: %d' % n_noise_)
                y_pred = clust.labels_.astype(np.int)
                # printT('Calculating Cluster Centres')
                clusterPoints = calc_cluster_centre(spots2D,y_pred)
                clusterPointsRots = 1024 - clusterPoints
                ids[files[i]] = clusterPointsRots
                # printT('Cluster centres at:')
                # print(clusterPointsRots)
                # printT('Finished file {}'.format(files[i]))
                if v!=False:
                    spots2DRotate = 1024 - spots2D
                    spots2DRots[files[i]] = spots2DRotate
                    y_preds[files[i]] = y_pred
            else:
                noSunspots.append(files[i])
                printT('NO Sunspots were identified by scikit-learn!')
        else:
            noSunspots.append(files[i])
            printT('NO Sunspots were identified!')
    if v!=False:
        fig = plt.figure(3)
        def sunspot_anim(i):
            smap = sunpy.map.Map(mapsequence[i])
            smap = smap.resample((1024, 1024) * u.pix)
            smap = smap.rotate(order=3)
            ax = fig.add_subplot(projection=smap)
            ax.set_axis_off()
            smap.plot(axes=ax, annotate=False)
            colors = np.array(list(islice(cycle(['#377eb8', '#ff7f00', '#4daf4a',
                                             '#f781bf', '#a65628', '#984ea3',
                                             '#999999', '#e41a1c', '#dede00']),
                                      int(max(y_preds[files[i]]) + 1))))
            ax.scatter(spots2DRots[files[i]][:,1], spots2DRots[files[i]][:,0], s=10, color=colors[y_preds[files[i]]], alpha=0.01)
            ax.scatter(ids[files[i]][:,1], ids[files[i]][:,0], color='k', marker='*', s=10, alpha=0.5)
        anim = animation.FuncAnimation(fig, sunspot_anim, frames=num_files, interval=500)
        anim.save(v, writer='imagemagick', fps=0.5)
    printT('Function id_sunspots finished')
    return ids, noSunspots

@my_timer
def track_sunspots(files, files_noSunspots, sunspot_ids, toldx, toldy, link, longest, resCut):
    '''
    Function to track movement of sunspot clusters from id_sunspots
    Takes
    files - array of fits filenames/paths
    files_noSunspots - array of fits filenames/paths which have no identified sunspots
    sunspots_ids - the cluster centres for each file (dictionary)
    toldx - the maximum change in x position between each timestep
    toldy - the maximum change in y position between each timestep
    link - the smallest length of a track, should be 5 or greater
    longest - the longest length of a track
    resCut - max residual to pass the polyfit test
    '''
    finalTracks = []
    tracks = []
    newTracks = []
    printT('Creating initial track points')
    # Get the initial tracks from the first file
    for i in sunspot_ids[files[0]]:
        tracks.append(np.reshape(i, (-1, 2)))
    reset = False
    start = 0
    printT('Number of starting tracks = {}'.format(len(tracks)))
    # Loop over all other files
    for t in range(1, len(files)):
        printT('Searching timestep {}/{}'.format(t,len(files)-1))
        # If the last file had sunspots do this
        if reset == False:
            # If this file has sunspots
            if files[t] not in files_noSunspots:
                thisIDS = sunspot_ids[files[t]]
                # For each track related to that file
                for i in tracks:
                    linked = 0
                    for j in thisIDS:
                        # What if this point starts a new track later
                        newTracks.append(np.reshape(j, (-1, 2)))
                        # Check whether we get a link using positional cuts
                        # If we do add it to newTracks (if less than len 4 do this without polyfit)
                        # This is because polyfit might be poorly conditioned for less than 4 points
                        if (abs(j[1] - i[-1,-1]) < toldx) and (0 < abs(j[0] - i[-1,0]) < toldy):
                            testTrack = np.row_stack((i, j))
                            if len(testTrack) <= 4:
                                newTracks.append(testTrack)
                                linked += 1
                            else:
                                _, res, _, _, _ = np.polyfit(np.linspace(0, 1, num=len(testTrack)), testTrack[:,1], 3, full=True)
                                if res <= resCut:
                                    newTracks.append(testTrack)
                                    linked += 1
                    # If no links were found append to finalTracks
                    # Unless first few iterations where it won't be make sure it has linked something
                    l  = len(i)
                    if linked==0:
                        if l > link:
                            finalTracks.append(i)
                        elif l > (t-start):
                            newTracks.append(i)
                # Make sure tracks are greater than t or link in length
                print('Cleaning up {} tracks'.format(len(newTracks)))
                tracks = []
                for track in newTracks:
                    l = len(track)
                    if ((l > (t-start)) or (l > link)):
                        tracks.append(track)
                newTracks = []
                print('Number of Tracks = {}'.format(len(tracks)))
                print('Number of final Tracks = {}'.format(len(finalTracks)))
            # If this file has no sunspots
            else:
                printT('No sunspots found - dumping final tracks')
                for i in tracks:
                    if len(i) > link:
                        finalTracks.append(i)
                tracks = []
                reset = True
                start = t
        # If the last file had no sunspots do this
        else:
            if files[t] not in files_noSunspots:
                printT('Resetting Tracks')
                for i in sunspot_ids[files[t]]:
                    tracks.append(np.reshape(i, (-1, 2)))
                    reset = False
                    start = t
            else:
                printT('No sunspots in this image either')
                start = t
    for i in tracks:
        if longest > len(i) > link:
            _, res, _, _, _ = np.polyfit(np.linspace(0, 1, num=len(i)), i[:,1], 3, full=True)
            if res <= resCut:
                finalTracks.append(i)
    print('FINAL number of Tracks pre cut= {}'.format(len(finalTracks)))
    finalTracksCut = []
    for track in finalTracks:
        if longest > len(track) > link:
            finalTracksCut.append(track)
        else:
            print('OOPSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
    print('FINAL number of Tracks = {}'.format(len(finalTracksCut)))
    return finalTracksCut

sunspot_ids, files_noSunspots = id_sunspots(files, v=False)

# Save the data
sunspot_ids_file = open('./data/sunspot_ids.pkl', 'wb')
pickle.dump(sunspot_ids, sunspot_ids_file)
sunspot_ids_file.close()
files_noSunspots = np.asarray(files_noSunspots)
np.save('./data/files_noSunspots.npy', files_noSunspots)

# # Load the data if we have saved it from a previous run
# # this lets us skip the time intensive scikit-learn step
# files_noSunspots = np.load('./data/files_noSunspots.npy')
# sunspot_ids_file = open('./data/sunspot_ids.pkl', 'rb')
# sunspot_ids = pickle.load(sunspot_ids_file)
# sunspot_ids_file.close()

toldx, toldy, link, longest, resCut = 80, 50, 5, 36, 5

# Link the cluster centres into sunspot tracks
tracks = track_sunspots(files, files_noSunspots, sunspot_ids, toldx, toldy, link, longest, resCut)
print('Number of tracks found = {}'.format(len(tracks)))
tracks = np.asarray(tracks)
# Save the data or load it
unique_track_filename = './data/tracks_{}_{}_{}_{}_{}.npy'.format(toldx, toldy, link, longest, resCut)
np.save(unique_track_filename, tracks)
# tracks = np.load(unique_track_filename, allow_pickle=True)

# Calculate the time period and latitude for each track
periods = []
latitudes = []
residuals = []

diameter = 943 # pixel diamter of the resampled sun's disk
radius = diameter/2

for i in tracks:
    x = i[:,1] - 512 # displacement from the central vertical axis of the star
    y = np.mean(i[:,0])
    dy = y - 512
    t = np.arange(0, len(x))*12 # hours - one image every 12 hours
    A = np.sqrt(radius**2 - dy**2)
    xAxis = np.arcsin(x/A)
    p = np.polyfit(t, xAxis, 1)
    m = p[0]
    T = 2*np.pi/m / 24 # divide by 24 to get days
    lat = degrees(np.arcsin(dy/radius))
    periods.append(T)
    latitudes.append(lat)
    _, res, _, _, _ = np.polyfit(np.linspace(0, 1, num=len(i)), i[:,1], 3, full=True)
    residuals.append(res)

convert = 360/365.25
deg_per_day = [360/t + convert for t in periods]
periods = [360/dpd for dpd in deg_per_day]

# Final cut remove extreme time periods
periodsCut = []
latitudesCut = []
residualsCut = []
for i in range(len(periods)):
    if 40 > periods[i] > 20:
        periodsCut.append(periods[i])
        latitudesCut.append(latitudes[i])
        residualsCut.append(residuals[i])
periodsCut = np.asarray(periodsCut)
latitudesCut = np.asarray(latitudesCut)
residualsCut = np.asarray(residualsCut)

print('\nFinal number of tracks plotted = {}'.format(len(periodsCut)))

# Plot the latitude vs period
fig = plt.figure(3)
ax = fig.add_subplot()
# Color the points based on the residuals
colors = residualsCut.flatten()/max(residualsCut)
scatter = ax.scatter(periodsCut, latitudesCut, c=colors, cmap='viridis', alpha=0.75)
ax.set_ylim(-90, 90)
ax.set_xlim(23, 40)
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(30))
ax.set_xlabel('Rotation Period / days', labelpad=20, horizontalalignment='right', position=(1,25))
ax.set_ylabel('Latitude / degrees')
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines['bottom'].set_position("zero")
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_alpha(1)
cbar.draw_all()
ax.text(0.3, 0.99, 'max Residual = {:.2f}'.format(max(residualsCut)[0]),
        verticalalignment='center', horizontalalignment='center',
        transform=ax.transAxes,
        color='k', fontsize=10)

# Plot the theoretical rotation curve using SunPy
from sunpy.physics.differential_rotation import diff_rot

latitudesTheory = np.arange(-90, 90, 1) * u.deg
dt = 1 * u.day
rotation_rate = [diff_rot(dt, this_lat) / dt for this_lat in latitudesTheory]
rotation_period = [360 * u.deg / this_rate for this_rate in rotation_rate]
ax.plot([this_period.value for this_period in rotation_period], latitudesTheory, alpha=0.5)

plt.savefig('autoTrackSunspots.png', dpi=200)
# plt.show()

# References

# SunPy - Differential Rotation Code - https://docs.sunpy.org/en/stable/generated/gallery/plotting/simple_differential_rotation.html
# Stuart Mumford - stara.py - https://github.com/Cadair/sunspot_experiments/blob/master/
# scikit-learn - Clustering - https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering
# Roša, D., Brajša, R., Vršnak, B. et al. The relation between the synodic and sidereal rotation period of the Sun. Sol Phys 159, 393–398 (1995). https://doi.org/10.1007/BF00686540
# scienceinschool - Measuring Solar Rotation - https://www.scienceinschool.org/content/sunspots-rotating-sun