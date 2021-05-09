''' potential.py
Calculates the gravitational potential in a 2D plane from Body objects.

If you share, use or modify this code in any way use the citation found here:
https://github.com/astroDimitrios/Astronomy/blob/master/CITATION.txt
Please contact me at astrodimitrios@gmail.com with any suggestions, mistakes found, or general questions about teaching astronomy with Python.

© Dimitrios Theodorakis GNU General Public License v3.0 https://github.com/astroDimitrios/Astronomy

Radius is volumetric Mean Radius
Sun data from - https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
Earth data from - https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
'''

import numpy as np
import timeit

G = 6.67408*10**-11        # m^3 kg^-1 s^-2
AU = 1.495978707*10**11    # m

class Body:
    '''Object to calculate gravitational field of'''

    def __init__(self, name, x, y, r, m):
        '''Initialised the body
        
        Args:
            name -- string, name of the body
            x    -- float, x position of the object (AU)
            y    -- float, y position of the object (AU)
            r    -- float, radius of the object (km)
            m    -- float, mass of the object (kg)

        Example:
            >>> Moon = Body('Moon', 0, 0, 384400000, 7.34767309*10**22)
        '''
        self.name = name
        self.x = x
        self.y = y
        self.r = r
        self.m = m

    def __str__(self):
        return '{} at ({:.2f}, {:.2f}) AU with r = {:.2f} km and m = {:.2f} kg'.format(self.name,self.x,self.y,self.r,self.m)

    def __repr__(self):
        return 'Body({}, {:f}, {:f}, {:f}, {:f})'.format(self.name,self.x,self.y,self.r,self.m)

    # Sun and Earth data is built in
    @classmethod
    def Sun(cls, x, y):
        return cls('Sun', x, y, 695700, 1988500*10**24)

    @classmethod
    def Earth(cls, x, y):
        return cls('Earth', x, y, 6371, 5.9724*10**24)

def single_potential(X, Y, body):
    '''Calculates potential energy for a single body

    Args:
        X    -- NumPy meshgrid array
        Y    -- NumPy meshgrid array, same size as X
        body -- Body class object
    
    Example:
        >>> x = np.linspace(-2, 2, 100)
        >>> y = np.linspace(-2, 2, 100)
        >>> X, Y = np.meshgrid(x, y, indexing='ij')
        >>> Earth = Body.Earth(1, 0)
        >>> U_Earth = single_potential(X, Y, Earth)
    '''
    radius = body.r*1000 # convert to m
    dists = np.hypot(X-body.x, Y-body.y)*AU
    U_single = np.where(dists > radius, -G*body.m/dists, G*body.m*(dists**2-3*radius**2)/(2*radius**3))
    return U_single

def potential(X, Y, bodies):
    '''Calculates potential energy due to several bodies

    Args:
        X       -- NumPy meshgrid array
        Y       -- NumPy meshgrid array, same size as X
        bodyies -- List of Body class objects
    
    Example:
        >>> x = np.linspace(-2, 2, 100)
        >>> y = np.linspace(-2, 2, 100)
        >>> X, Y = np.meshgrid(x, y, indexing='ij')
        >>> Earth = Body.Earth(0, 0)
        >>> Sun = Body.Sun(0, 0)
        >>> U_Comb = potential(X, Y, [Earth, Sun])
    '''
    U = np.zeros(X.shape)
    for body in bodies:
        U_single = single_potential(X, Y, body)
        U = U + U_single
    return U

if __name__ == "__main__":

    # Initialise bodies
    Earth = Body.Earth(1, 0)
    Sun = Body.Sun(0, 0)
    Moon = Body('Moon', 1.001, 0, 384400000, 7.34767309*10**22)

    # Create a 2D grid
    x_min, x_max = (-2, 2)                   # min and max x values 
    y_min, y_max = (-2, 2)                   # min and max y values
    # x_min, x_max = (0.999, 1.001)            # zoom Earth
    # y_min, y_max = (-0.001, 0.001)           # zoom Earth
    # increase values for finer resolution
    x_res, y_res = (1000, 1000)                  # x, y shape of grid
    x = np.linspace(x_min, x_max, x_res)
    y = np.linspace(y_min, y_max, y_res)
    
    X, Y = np.meshgrid(x, y, indexing='ij')

    # calculate single potential
    U_Earth = single_potential(X, Y, Earth)
    print(U_Earth)

    # # calculate combined potential
    # U_Comb = potential(X, Y, [Earth, Sun, Moon])

    # # timing the potential function
    # def wrapper(func, *args, **kwargs):
    #     def wrapped():
    #         return func(*args, **kwargs)
    #     return wrapped
    # wrap = wrapper(potential, X, Y, [Earth, Sun, Moon])
    # print(timeit.timeit(wrap, number=10))
    # # 0.121105 s with x_res, y_res = 100, 100
    # # 13.5439045 s with x_res, y_res = 1000, 1000