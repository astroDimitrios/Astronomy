#################################################################
#
# This code won't run! It only contains code snippets to put in the ipynb notebook
# if you're trying to use the Exeter method described in the references
#
#################################################################

#### This cell in the ipynb now has the sun object loaded

# Your code here:
ts = load.timescale(builtin=True)
# Change this to the time of your observation - year, month, day, hour, min
t = ts.utc(2019, 12, 3, 17, 32)

eph = load('de421.bsp')
earth, moonSky, sun = eph['earth'], eph['moon'], eph['sun']

pc = PlanetaryConstants()
pc.read_text(load('moon_080317.tf'))
pc.read_text(load('pck00008.tpc'))
pc.read_binary(load('moon_pa_de421_1900-2050.bpc'))

frame = pc.build_frame_named('MOON_ME_DE421')
# Change the name of the next variable to the name of the crater you chose
# look up its latitude and longitude and enter them on the line below
# remember South lats and W longs are entered as negative numbers
theophilus = moonSky + pc.build_latlon_degrees(frame, 26.4, -11.4)

# Change the crater name in the next line
apparent = earth.at(t).observe(theophilus).apparent()
ra, dec, distance = apparent.radec(epoch='date')
distance

#### This new cell calculates sub-Earth and sub-Solar points on the moon

p = (earth - moonSky).at(t)
latSubE, lonSubE, distanceSubE = p.frame_latlon(frame)
lonSubE_degrees = (lonSubE.degrees - 180.0) % 360.0 - 180.0
print('sub-Earth point latitude: {:.3f}'.format(latSubE.degrees))
print('sub-Earth point longitude: {:.3f}'.format(lonSubE_degrees))

p2 = (sun - moonSky).at(t)
latSubS, lonSubS, distanceSubS = p2.frame_latlon(frame)
lonSubS_degrees = (lonSubS.degrees - 180.0) % 360.0 - 180.0
print('sub-Solar point latitude: {:.3f}'.format(latSubS.degrees))
print('sub-Solar point longitude: {:.3f}'.format(lonSubS_degrees))

#### This new cell calculates the angle alpha and then the height from it

cos_90alpha =  np.cos((90--13.8)*np.pi/180)*np.cos((90-latSubS.degrees)*np.pi/180)+np.sin((90--13.8)*np.pi/180)*np.sin((90-latSubS.degrees)*np.pi/180)*np.cos((lonSubS_degrees-13.9)*np.pi/180)
#cos(90-alpha) = cos(90-lat crater)*cos(90 - lat sub solar) + sin(90-lat crater)*sin(90 - lat sub solar)*cos(long sub solar - long crater)
alpha = 90 - np.arccos(cos_90alpha)*180/np.pi
h = L*np.tan(alpha*np.pi/180)
h