import numpy as np
import matplotlib.pyplot as plt

G = 6.67408*10**-11

class Body:
    def __init__(self, name, mass, dist):
        self.name = name
        self.m = mass
        self.dist = dist

class Main:
    def __init__(self, name, mass, radius, step, scale):
        self.name = name
        self.m = mass
        self.radius = radius
        self.step = step                  # in terms of pi
        self.thetas = np.arange(0, 2*np.pi, step*np.pi)
        self.scale = scale

    tide_f = {

    }

    def force_centre(self, body):
        """ Calculates the gravitational attraction on the main object
        due to the other body
        """
        force_c = G*self.m*body.m/body.dist**2 / self.scale
        return force_c

    def force_points(self, body):
        """ Calculates the gravitational attraction at points on the surface
        of the main body due to the other body
        """
        c = np.sqrt(self.radius**2 + body.dist**2 - 2*self.radius*body.dist*np.cos(self.thetas))
        force_p = G*self.m*body.m/c**2 / self.scale
        sin_a = (body.dist - self.radius*np.cos(self.thetas))/c
        cos_a = np.cos(np.arcsin(sin_a))
        force_p_h = force_p*sin_a 
        force_p_v = force_p*cos_a
        signs = np.sign(np.cos(self.thetas+np.pi/2))
        force_p_v *= signs
        return force_p_h, force_p_v

    def forces(self, body):
        force_c = self.force_centre(body)
        force_p_h, force_p_v = self.force_points(body)
        return [force_c, force_p_h, force_p_h-force_c, force_p_v]

    def update_tides(self, key1, key2, tide_vals=None, use_prev=False):
        if use_prev:
            if key1 in self.tide_f:
                update = [new_tide+old_tide for new_tide, old_tide in zip(self.tide_f[key2], self.tide_f[key1])]
                self.tide_f[key1] = update
            else:
                self.tide_f[key1] = self.tide_f[key2]
        else:
            self.tide_f[key2] = tide_vals
            if key1!=key2:
                # If there is only 1 body the keys are the same so don't double numbers                           
                update = [new_tide+old_tide for new_tide, old_tide in zip(tide_vals, self.tide_f[key1])]
                self.tide_f[key1] = update

    def tides(self, *args):
        body_names = [body.name for body in args]
        tide_f_key = "+".join(body_names)
        for body in args:
            if body.name in self.tide_f:
                self.update_tides(tide_f_key, body.name, use_prev=True)
            else:
                self.update_tides(tide_f_key, body.name, tide_vals=self.forces(body))
        return self.tide_f[tide_f_key]

if __name__ == "__main__":

    scale = 5.972*10**24    # mass of Earth so tidal force is per unit mass (has units of acceleration)

    earth = Main('Earth', 5.972*10**24, 6371000, 1/4, scale)
    moon = Body('Moon', 7.34767309*10**22, 384400000)

    forces = earth.tides(moon)
    # print(forces[0])
    # print(forces[1])
    print(forces[2])
    print(forces[3])
    # print(earth.tide_f)

    # # check a value for one side PASS
    # my_a = (earth.tide_f['Moon'][1][0]-earth.tide_f['Moon'][0])
    # their_a = G*7.34767309*10**22*2*6371000/384400000**3
    # print(my_a)
    # print(their_a)
    # print(my_a/their_a)
    # # percentage diff between 2 sides test ~7 % PASS
    # print((earth.tide_f['Moon'][1][0]/earth.tide_f['Moon'][0]*100-100)*2)

    # sun = Body('Sun', 1.989*10**30, 1.495978707*10**11)
    # double_forces = earth.tides(moon, sun) # Sun and Moon aligned same side - Spring tide

    # # check 44% strength of Sun tide compared to Moon
    # print(earth.tide_f['Moon'][2][0])
    # print(earth.tide_f['Sun'][2][0])
    # print(earth.tide_f['Sun'][2][0]/earth.tide_f['Moon'][2][0]*100)
    # print(earth.tide_f['Moon+Sun'][2][0])

    # sun2 = Body('Sun2', 1.989*10**30, 1.495978707*10**11)
    # trip_forces = earth.tides(moon, sun, sun2) # Fictitious test