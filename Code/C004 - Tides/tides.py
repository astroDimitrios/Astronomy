"""
tides.py calculates the tidal forces on an object due to any number of bodies
If you share, use or modify this activity in any way use the citation found here:
https://github.com/astroDimitrios/Astronomy/blob/master/CITATION.txt
Please contact me at astrodimitrios@gmail.com with any suggestions, mistakes found, or general questions about teaching astronomy with Python.

© Dimitrios Theodorakis GNU General Public License v3.0 https://github.com/astroDimitrios/Astronomy
"""

import numpy as np

G = 6.67408*10**-11

class Body:
    """Create a body which tidally influences the Main body"""

    def __init__(self, name, mass, dist, offset_angle):
        """Initialises the body

        Args:
            name -- string, name of the object
            mass -- float, mass of the object in kg
            dist -- float, distance to the object in m
            offset_angle -- float, angle offset from +x axis counterclockwise in radians 

        Example:
            >>> moon = Body('Moon', 7.34767309*10**22, 384400000, 0)
        """
        self.name = name
        self.m = mass
        self.dist = dist
        self.off = offset_angle

class Main:
    """Create the Main body which is tidally influenced by the other Body/s"""

    def __init__(self, name, mass, radius, step, scale):
        """Initialises the body

        Args:
            name -- string, name of the object
            mass -- float, mass of the object in kg
            radius -- float, distance to the object in m
            step -- float, angular step to make when calculating surface points - in terms of pi
                 -- used to calculate the angles of each point, each point is +step*np.pi
            scale -- float, scale to divide forces by in kg
                  -- set to mass of Main object for acceleration in ms-2

        Example:
            This example creates the Earth with scale equal to its mass to get tidal acceleration
            Scale is 1/4 so calculations are at 8 points over sphere, pi/4 apart
            >>> earth = Main('Earth', 5.972*10**24, 6371000, 1/4, 5.972*10**24)
        """
        self.name = name
        self.m = mass
        self.radius = radius
        self.step = step              # in terms of pi
        self.thetas = np.arange(0, 2*np.pi, step*np.pi)
        self.scale = scale

    # dict to store tidal forces in
    tide_f = {

    }

    def force_centre(self, body):
        """ Calculates the gravitational attraction on the main object
        due to the other body. Unit: N

        Args:
            body -- Body class object

        Returns:
            force_c -- float, the gravitational force at the centre of the Main body due to body

        Example:
            >>>  force_c = earth.force_centre(moon)
            >>>  print(force_c)
            3.31874952061913e-05
        """
        force_c = G*self.m*body.m/body.dist**2 / self.scale
        return force_c

    def force_points(self, body):
        """ Calculates the gravitational attraction at points on the surface
        of the Main body due to the other body. Unit: N

        Args:
            body -- Body class object

        Returns:
            force_p_h -- NumPy array of floats, hor. component of grav force at each surface point
            force_p_v -- NumPy array of floats, vert. component of grav force at each surface point

        Example:
            >>>  force_p_h, force_p_v = earth.force_points(moon)
            >>>  print(force_p_h)
            array([3.43155527e-05, 3.39721024e-05, 3.31738253e-05, 3.24165524e-05,
                   3.21141611e-05, 3.24165524e-05, 3.31738253e-05, 3.39721024e-05])
        """
        c = np.sqrt(self.radius**2 + body.dist**2 - 2*self.radius*body.dist*np.cos(self.thetas-body.off))
        force_p = G*self.m*body.m/c**2 / self.scale
        sin_b = (body.dist - self.radius*np.cos(self.thetas-body.off))/c
        b = np.arcsin(sin_b)
        force_p_h = force_p*np.cos(b+body.off-np.pi/2) 
        force_p_v = force_p*np.sin(b+body.off-np.pi/2)
        # fix the signs of our vectors
        if abs(body.dist*np.cos(body.off)) < self.radius:
            signs_h = np.sign(-np.cos(self.thetas))
            force_p_h = np.absolute(force_p_h)*signs_h
            sign_v = np.sign(np.sin(body.off))
            force_p_v = np.absolute(force_p_v)*sign_v
        elif abs(body.dist*np.sin(body.off)) < self.radius:
            signs_v = np.sign(-np.sin(self.thetas))
            force_p_v = np.absolute(force_p_v)*signs_v
            sign_h = np.sign(np.cos(body.off))
            force_p_h = np.absolute(force_p_h)*sign_h
        else:
            sign_h = np.sign(np.cos(body.off))
            force_p_h = np.absolute(force_p_h)*sign_h
            sign_v = np.sign(np.sin(body.off))
            force_p_v = np.absolute(force_p_v)*sign_v
        return force_p_h, force_p_v

    def forces(self, body):
        """ Calculates the tidal force at each surface point.

        Args:
            body -- Body class object

        Returns:
            A list containing:
            force_c -- float, the gravitational force at the centre of the Main body due to body
            force_p_h -- NumPy array of floats, hor. component of grav force at each surface point
            force_p_h_diff -- NumPy array of floats, hor. comp. of tidal force at each surface point
            force_p_v -- NumPy array of floats, vert. component of grav force at each surface point
            force_p_v_diff -- NumPy array of floats, vert. comp. of tidal force at each surface point

        Example:
            >>>  t_forces = earth.forces(moon)
            >>>  print(t_forces)
            [3.31874952061913e-05, array([3.43155527e-05, 3.39721024e-05, 3.31738253e-05, 3.24165524e-05,
             3.21141611e-05, 3.24165524e-05, 3.31738253e-05, 3.39721024e-05]), array([ 1.12805754e-06,  7.84607232e-07,  0.00000000e+00, -7.70942821e-07,
             -1.07333414e-06, -7.70942821e-07,  0.00000000e+00,  7.84607232e-07]), array([ 0.00000000e+00, -4.02857477e-07, -5.49819045e-07, -3.75505178e-07,
             -0.00000000e+00,  3.75505178e-07,  5.49819045e-07,  4.02857477e-07]), array([ 0.00000000e+00, -4.02857477e-07, -5.49819045e-07, -3.75505178e-07,
             0.00000000e+00,  3.75505178e-07,  5.49819045e-07,  4.02857477e-07])]
        """
        force_c = self.force_centre(body)
        force_p_h, force_p_v = self.force_points(body)
        force_p_h_diff = force_p_h - force_c*np.cos(body.off)
        force_p_v_diff = force_p_v - force_c*np.sin(body.off)
        # set low numbers to zero - to set hor diff to zero at pi/2 and 3pi/2 for instance
        zero_cut = 5*10**-8      # specific to Moon and Earth
        force_p_h_diff[np.abs(force_p_h_diff) < zero_cut] = 0
        force_p_v_diff[np.abs(force_p_v_diff) < zero_cut] = 0
        return [force_c, force_p_h, force_p_h_diff, force_p_v, force_p_v_diff]

    def update_tides(self, key1, key2, off, offsets,  tide_vals=None, use_prev=False):
        """ Updates the tidal forces contained in the tide_f dictionary.

        Called by self.tides() - should not be called independently
        If use_prev is passed as True then tide_vals is not used

        Use previously calculated values for a body if they are already in the dictionary tide_f
        Otherwise update the tide values for the combined effect of all the bodies
        using the passed tide_vals list which is from self.forces()

        Args:
            key1 -- str, the final key of all tidal effects combined, eg 'Sun+Moon'
            key2 -- str, name of the body object, eg 'Sun'
            off -- str, offset_angle of the Body object as a string
            offsets -- str, offset angles of all Body object combined
                    -- eg, '0+0' for two Bodys with offset angles of 0
            tide_vals -- NumPy array of floats from self.forces(), default None
                      -- Is not neccessary when using use_prev=True
            use_prev -- boolean, whether to use values already calculated in tide_f, default False

        Example:
            self.update_tides(tide_f_key, body.name, this_off, tide_f_offs, use_prev=True)
            self.update_tides(tide_f_key, body.name, this_off, tide_f_offs, tide_vals=self.forces(body))
        """
        # check if the final key exists
        if key1 not in self.tide_f:
            self.tide_f[key1] = {}
            self.tide_f[key1][offsets] = []
        # if offsets key not in nested dictionary add it 
        elif offsets not in self.tide_f[key1]:
            self.tide_f[key1][offsets] = []
        # use prev calculated values
        if use_prev:
            # if the final key is empty zip won't work!
            if self.tide_f[key1][offsets] != []:                         
                update = [new_tide+old_tide for new_tide, old_tide in zip(self.tide_f[key2][off], self.tide_f[key1][offsets])]
                self.tide_f[key1][offsets] = update
            else:
                self.tide_f[key1][offsets] = self.tide_f[key2][off]
        # use newly calculated values
        else:
            # add key for single body and its offset
            self.tide_f[key2] = {}
            self.tide_f[key2][off] = tide_vals
            # If there is only 1 body the keys are the same so don't double numbers  
            if key1!=key2: 
                # if the final key is empty zip won't work!
                if self.tide_f[key1][offsets] != []:                         
                    update = [new_tide+old_tide for new_tide, old_tide in zip(tide_vals, self.tide_f[key1][offsets])]
                    self.tide_f[key1][offsets] = update
                else:
                    self.tide_f[key1][offsets] = tide_vals

    def tides(self, *args):
        """Calculates the tides on Main due to the bodies passed as arguments.

        Checks to see whether the tidal force from each individual body has been
        calculated previously so it doesn't repeat calculations

        Args:
            Any number of Body class objects can be passed.

        Returns:
            A list containing:
            force_c -- float, the gravitational force at the centre of the Main body due to bodies
            force_p_h -- NumPy array of floats, hor. component of grav force at each surface point
            force_p_h_diff -- NumPy array of floats, hor. comp. of tidal force at each surface point
            force_p_v -- NumPy array of floats, vert. component of grav force at each surface point
            force_p_v_diff -- NumPy array of floats, vert. comp. of tidal force at each surface point

        Example:
            >>> forces = earth.tides(moon)
            >>> print(forces)
            [3.31874952061913e-05, array([3.43155527e-05, 3.39721024e-05, 3.31738253e-05, 3.24165524e-05,
             3.21141611e-05, 3.24165524e-05, 3.31738253e-05, 3.39721024e-05]), array([ 1.12805754e-06,  7.84607232e-07,  0.00000000e+00, -7.70942821e-07,
             -1.07333414e-06, -7.70942821e-07,  0.00000000e+00,  7.84607232e-07]), array([ 0.00000000e+00, -4.02857477e-07, -5.49819045e-07, -3.75505178e-07,
             -0.00000000e+00,  3.75505178e-07,  5.49819045e-07,  4.02857477e-07]), array([ 0.00000000e+00, -4.02857477e-07, -5.49819045e-07, -3.75505178e-07,
             0.00000000e+00,  3.75505178e-07,  5.49819045e-07,  4.02857477e-07])]
        """
        # get all body names then join them to make the dictionary key
        body_names = [body.name for body in args]
        tide_f_key = "+".join(body_names)
        # get all offset angles then join them to make the nested dictionary key
        list_offsets = [str(body.off) for body in args]
        tide_f_offs = "+".join(list_offsets)
        for body in args:
            this_off = str(body.off)
            # if the tidal force for this body has been calculated before use stored values
            if body.name in self.tide_f:
                # check if the calculated values were for the same offset_angle
                if this_off in self.tide_f[body.name]:
                    self.update_tides(tide_f_key, body.name, this_off, tide_f_offs, use_prev=True)
            # else calculate the tidal force from the new body and pass it to self.update_tides()
            else:
                this_body_tide = self.forces(body)
                self.update_tides(tide_f_key, body.name, this_off, tide_f_offs, tide_vals=this_body_tide)
        return self.tide_f[tide_f_key][tide_f_offs]

if __name__ == "__main__":

    scale = 5.972*10**24    # mass of Earth so tidal force is per unit mass (has units of acceleration)

    # offsets in radians from theta = 0
    off_moon = 0
    off_sun = 0

    # initialise Earth and Moon
    earth = Main('Earth', 5.972*10**24, 6371000, 1/4, scale)
    moon = Body('Moon', 7.34767309*10**22, 384400000, off_moon)

    # calculate tidal forces
    forces = earth.tides(moon)
    # print(forces)

    # # check a value for one side PASS
    # my_a = (earth.tide_f['Moon'][1][0]-earth.tide_f['Moon'][0])
    # their_a = G*7.34767309*10**22*2*6371000/384400000**3
    # print(my_a/their_a)
    # # percentage diff between 2 sides test ~7 % PASS
    # print((earth.tide_f['Moon'][1][0]/earth.tide_f['Moon'][0]*100-100)*2)

    # # Sun and Moon aligned same side - Spring tide
    sun = Body('Sun', 1.989*10**30, 1.495978707*10**11, off_sun)
    double_forces = earth.tides(moon, sun) 

    # # check 44% strength of Sun tide compared to Moon PASS
    # print(earth.tide_f['Moon'][2][0])
    # print(earth.tide_f['Sun'][2][0])
    # print(earth.tide_f['Sun'][2][0]/earth.tide_f['Moon'][2][0]*100)
    # print(earth.tide_f['Moon+Sun'][2][0])

    # # fictitious 3-body test
    sun2 = Body('Sun2', 1.989*10**30, 1.495978707*10**11, 0)
    trip_forces = earth.tides(moon, sun, sun2)