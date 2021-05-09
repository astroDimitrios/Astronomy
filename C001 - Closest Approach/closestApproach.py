import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.transforms import Affine2D
from matplotlib import rc
# You will need latex installed
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

# Creating simple ellipses

def ellipse(A, B):
    '''
    Makes an X and Y array of values to plot to get your ellipse
    '''
    start = 0
    step = 2*np.pi/100
    end = 2*np.pi + step
    phi = np.arange(start, end, step)
    X = A*np.cos(phi)
    Y = B*np.sin(phi)
    return (X, Y, A, B)

def plot_ellipse(E, newplot):
    '''
    Plots the ellipse created by ellipse()
    It does this on a new Figure if newplot == True
    Must be called differently depedning on the value of newplot:

    fig, ax = make_plot_ellipse(A,B,True)
    make_plot_ellipse(A,B,False)
    '''
    X = E[0]
    Y = E[1]
    A = E[2]
    B = E[3]
    if newplot == True:
        fig = plt.figure()
        ax = plt.subplot()
        ax.plot(X, Y, label='A = {}, B = {}'.format(A,B))
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.axis('equal')
        ax.xaxis.set_major_locator(plt.MultipleLocator(A))
        ax.xaxis.set_minor_locator(plt.MultipleLocator(A/2))
        ax.yaxis.set_major_locator(plt.MultipleLocator(B))
        ax.yaxis.set_minor_locator(plt.MultipleLocator(B/2))
        ax.legend(loc="upper right")
        return fig, ax
    else:
        ax = plt.gca()
        ax.plot(X, Y, label='A = {}, B = {}'.format(A,B))
        ax.legend(loc="upper right")
        return

def make_plot_ellipse(A, B, newplot):
    '''
    Creates the ellipse and plots it in one step
    '''
    thisEllipse = ellipse(A, B)
    thisPlot = plot_ellipse(thisEllipse, newplot)
    return thisPlot

# Create the first ellipse then add another on the same axis
fig1, ax1 = make_plot_ellipse(1,2,True)
make_plot_ellipse(2,3,False)

# plt.show()

# -----------------------------------------------------------------------------

# Plotting elliptical orbits
# Finding dist between two planets
# https://www.space.com/16875-how-far-away-is-mars.html

# Constants
AU = 1.495978707*10**11 # m

# Data for planets
planets = np.array(['Earth', 'Mars'])
perihelion = np.array([147.1, 206.6])*10**9 # m
aphelion = np.array([152.1, 249.2])*10**9 # m
period = np.array([365.2, 687.0]) # days

# Convert to AU
perihelion /= AU
aphelion /= AU

def orbitPeri(perihelion, aphelion, period, extend):
    '''
    Calculate orbit assuming planet starts at Perihelion
    '''
    step = 0.1
    stoptime = period*extend
    t = np.arange(0, stoptime+step, step)
    X = aphelion*np.sin(2*np.pi*t/period)
    Y = perihelion*np.cos(2*np.pi*t/period)
    return np.array([t, X, Y])

def orbitAph(perihelion, aphelion, period, extend):
    '''
    Calculate orbit assuming planet starts at Aphelion
    '''
    step = 0.1
    stoptime = period*extend
    t = np.arange(0, stoptime+step, step)
    X = perihelion*np.sin(2*np.pi*t/period)
    Y = aphelion*np.cos(2*np.pi*t/period)
    return np.array([t, X, Y])

# Example use of orbit
Earth = orbitAph(perihelion[0], aphelion[0], period[0], 1)
Mars = orbitPeri(perihelion[1], aphelion[1], period[1], 1)

def deltaR(planet1, planet2, t=None):
    '''
    Calculate distance between planets
    Optional time arg which is the end time to calculate orbital positions
    If not specified it will use the longest period of the two planets
    '''
    p1ind = np.where(planets==planet1)
    p2ind = np.where(planets==planet2)
    if t==None: t = max(period[p1ind],period[p2ind])
    else: t=t
    p1orbit = orbitAph(perihelion[p1ind],aphelion[p1ind],period[p1ind],t/period[p1ind])
    p2orbit = orbitPeri(perihelion[p2ind],aphelion[p2ind],period[p2ind],t/period[p2ind])
    delX = p2orbit[1]-p1orbit[1]
    delY = p2orbit[2]-p1orbit[2]
    deltaR = np.sqrt(delX**2 + delY**2)
    return np.array([t, deltaR, min(deltaR), p1orbit, p2orbit, planet1, planet2])

# Specify planets to look at
p1 = 'Earth'
p2 = 'Mars'

# Calculate the distance between the two planets
dR = deltaR(p1,p2)
print(dR[2]) # Actual value ~0.36497845688 AU very close!

# Setup plot and background lines
fig = plt.figure(num=2, figsize=(15,5))
a1 = plt.subplot2grid((1,2), (0,0), colspan=1)
a2 = plt.subplot2grid((1,2), (0,1), colspan=1)
plt.subplots_adjust(wspace=0.8)
plt.suptitle(r'$Mars\ +\ Earth\ Orbits\ and\ Distance$', y=0.99, fontsize=18)
a1.spines['right'].set_visible(False)
a1.spines['top'].set_visible(False)
a1.spines['bottom'].set_visible(False)
a1.spines['left'].set_visible(False)
a1.tick_params(axis='both', which='both', bottom=False, left=False, labelbottom=False, labelleft=False)
a1.axis('equal')
a2.spines['right'].set_visible(False)
a2.spines['top'].set_visible(False)
a2.set_xlim(0, max(dR[3][0]))
a2.set_xlabel(r'$Time\ /\ days$', labelpad=10)
a2.set_ylabel(r'$\Delta r\ /\ AU$', labelpad=15)
base = a1.transData # Rotate data so orbit is ellipse on its side
rot = Affine2D().rotate_deg(90)
a1.plot(dR[3][2], dR[3][1], transform= rot + base, alpha=0.025, zorder=0)
a1.plot(dR[4][2], dR[4][1], transform= rot + base, alpha=0.025, zorder=0)
a1.scatter(0,0,s=70,c='gold',label=r'$Sun$')
a2.plot(dR[3][0], dR[1], alpha=0.25, zorder=0)
p1ind = np.where(planets==p1)
p2ind = np.where(planets==p2)
theoryMin = perihelion[p2ind] - aphelion[p1ind]
theoryMax = aphelion[p2ind] + perihelion[p1ind]
# minLabel = r'$\Delta r_{min}\ =\ $'+r'${:.3f}$'.format(theoryMin[0])+r'$\ AU$'
# maxLabel = r'$\Delta r_{max}\ =\ $'+r'${:.3f}$'.format(theoryMax[0])+r'$\ AU$'
minLabel = r'${:.3f}$'.format(theoryMin[0])+r'$\ AU$'
maxLabel = r'${:.3f}$'.format(theoryMax[0])+r'$\ AU$'
a2.axhline(theoryMin, ls='--', lw =1, c='grey', alpha=0.2)
a2.axhline(theoryMax, ls='--', lw =1, c='grey', alpha=0.2)
a2.text(max(dR[3][0])*9.5/10,theoryMin,minLabel,size=10,backgroundcolor='w',ha='center',va='center')
a2.text(max(dR[3][0])*9.5/10,theoryMax,maxLabel,size=10,backgroundcolor='w',ha='center',va='center')

# Initialise scatters for animation
planet1 = a1.scatter([],[])
planet2 = a1.scatter([],[])
currentR = a2.scatter([],[])

# Calc dR for a longer time then find the time where dR is max
dRLONG = deltaR(p1,p2,1000000)
buffer = 0.00001
timeToMax = dRLONG[3][0][np.argmax(dRLONG[1]>(theoryMax-buffer))]/365.25

# Initialise plot text
textpos = (0.485,0.54)
textpos2 = (0.485,0.46)
tsize = 14
text = r'$Time\ =\ {:.0f}\ days$'.format(0)+'\n'+r'$\Delta r\ =\ {:.3f}\ AU$'.format(dR[1][0])
text2 = r'$Time\ to\ \Delta r_{max}\ =\ $'+r'${:.0f}\ yrs$'.format(timeToMax)
figText = fig.text(textpos[0],textpos[1],text, ha='center', va='center', size=tsize, multialignment="center", linespacing=1.5)
figText2 = fig.text(textpos2[0],textpos2[1],text2, ha='center', va='center', size=tsize, multialignment="center", linespacing=1.5)

def animate(i):
    '''
    Animation function updates text and scatter plots
    '''
    global planet1, planet2, currentR, figText, figText2, dR
    planet1.remove()
    planet2.remove()
    currentR.remove()
    figText.remove()
    figText2.remove()
    j = i+1
    time = dR[3][0][::shorten]
    p1X = dR[3][2][::shorten]
    p1Y = dR[3][1][::shorten]
    p2X = dR[4][2][::shorten]
    p2Y = dR[4][1][::shorten]
    dRshort = dR[1][::shorten]
    beforeIndex = i-prev
    # Check that the indecies for points in the tail aren't negative - if yes shorten tail
    if beforeIndex > 0: 
        planet1 = a1.scatter(p1X[beforeIndex:j], p1Y[beforeIndex:j], s=size, c=p1col, zorder=1, label=r'$Earth$')
        planet2 = a1.scatter(p2X[beforeIndex:j], p2Y[beforeIndex:j], s=size, c=p2col, zorder=1, label=r'$Mars$')
        # planet1 = a1.scatter(p1X[beforeIndex:j], p1Y[beforeIndex:j], s=size, c=p1col, zorder=1, label=dR[5])
        # planet2 = a1.scatter(p2X[beforeIndex:j], p2Y[beforeIndex:j], s=size, c=p2col, zorder=1, label=dR[6])
        trans1 = planet1.get_offset_transform()
        planet1._transOffset = rot+trans1
        planet2._transOffset = rot+trans1
    else:
        beforeIndex = 0
        fixSize = np.zeros((1,j))
        fixSize[:] = size[:j]
        fixSize[0][-1] = 60
        planet1 = a1.scatter(p1X[:j], p1Y[:j], s=fixSize, c=p1col[-j:], zorder=1, label=r'$Earth$')
        planet2 = a1.scatter(p2X[:j], p2Y[:j], s=fixSize, c=p2col[-j:], zorder=1, label=r'$Mars$')
        # planet1 = a1.scatter(p1X[:j], p1Y[:j], s=fixSize, c=p1col[-j:], zorder=1, label=dR[5])
        # planet2 = a1.scatter(p2X[:j], p2Y[:j], s=fixSize, c=p2col[-j:], zorder=1, label=dR[6])
        trans1 = planet1.get_offset_transform()
        planet1._transOffset = rot+trans1
        planet2._transOffset = rot+trans1
    # Text and delta R scatter point
    currentR = a2.scatter(time[i], dRshort[i], s=50, c='k', alpha=1, zorder=1)
    text = r'$Time\ =\ {:.0f}\ days$'.format(time[i])+'\n'+r'$\Delta r\ =\ {:.3f}\ AU$'.format(dRshort[i])
    text2 = r'$Time\ to\ \Delta r_{max}\ =\ $'+r'${:.0f}\ yrs$'.format(timeToMax-time[i]/365.25)
    figText = fig.text(textpos[0],textpos[1],text, ha='center', va='center', size=tsize, multialignment="center", linespacing=1.5)
    figText2 = fig.text(textpos2[0],textpos2[1],text2, ha='center', va='center', size=tsize, multialignment="center", linespacing=1.5)
    i += 1
    # Don't keep updating the legend
    if i == 1:
        a1.legend(loc=(0.,0.9), frameon=False, fontsize=12)

# Sizes and colours for tail
prev = 199
size = np.linspace(0.1,30,prev)
size = np.append(size, 60)
alphas = np.linspace(0.001,0.020,prev)
alphas = np.append(alphas, 1)
p1col = np.zeros((prev+1,4))
p1col[:,0] = 102/255
p1col[:,1] = 255/255
p1col[:,2] = 99/255
p1col[:,3] = alphas
p2col = np.zeros((prev+1,4))
p2col[:,0] = 255/255
p2col[:,1] = 99/255
p2col[:,2] = 99/255
p2col[:,3] = alphas

# Shorten the animation by this much (take a step of 10 not 1)
shorten = 10
numFrames = int(np.floor(len(dR[3][0])/shorten))

anim = animation.FuncAnimation(fig, animate, frames=numFrames, interval=500, repeat=False)
anim.save("EarthMarsDistance_Video.mov", writer="imagemagick", fps=30, dpi=200)
# plt.show()

# ---------------------------------------------------------------------------------------------------------

# Challenge

# 1) Make an animation for a different pair of planets
# 2) Calculate the time to closest approach assuming you start at the farthest approach
# 3) Introduce a third body