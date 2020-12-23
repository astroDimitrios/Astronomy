import rebound
import matplotlib.pyplot as plt
import numpy as np

sim = rebound.Simulation()
# sim.add(m=1.0e-7)
# sim.add(m=1.0e-11, a=0.4)

OMEGA = 0.00013143527 # 1/s corr to a = 130,000 km
# sim.ri_sei.OMEGA = OMEGA

surface_density = 1
particle_density = 1

sim.G = 6.67428e-11 # N m^2/kg^2
# sim.G = 1
# sim.dt = 1e-2*2.*np.pi*OMEGA
sim.dt = 10
sim.softening = 0.2 # m fix num artefacts at small scales

boxsize = 2000
sim.configure_box(boxsize)

sim.configure_ghostboxes(2,2,0)

# sim.integrator = "sei"
# sim.boundary = "shear"
sim.gravity = "tree"
sim.collision = "tree"
sim.collision_resolve = "hardsphere"

sim.automateSimulationArchive("archive.bin", interval=1000, deletefile=True)

def cor_bridges(r, v):
        eps = 0.32*pow(abs(v)*100.,-0.234)
        if eps>1.:
            eps=1.
        if eps<0.:
            eps=0.
        return eps
sim.coefficient_of_restitution = cor_bridges

def powerlaw(slope, min_v, max_v):
    y = np.random.uniform()
    pow_max = pow(max_v, slope+1.)
    pow_min = pow(min_v, slope+1.)
    return pow((pow_max-pow_min)*y + pow_min, 1./(slope+1.))

# total_mass = 0.
# while total_mass < surface_density*(boxsize**2):
#     radius = powerlaw(slope=-3, min_v=1, max_v=4)/100  # [m]
#     mass = particle_density*4./3.*np.pi*(radius**3)
#     x = np.random.uniform(low=-boxsize/2., high=boxsize/2.)
#     sim.add(
#         m=mass,
#         r=radius,
#         x=x,
#         y=np.random.uniform(low=-boxsize/2., high=boxsize/2.),
#         z=np.random.normal(),
#         vx = 0.,
#         vy = -3./2.*x*OMEGA,
#         vz = 0.)
#     total_mass += mass

count = 0
while count < 1000:
    radius = powerlaw(slope=-4, min_v=1, max_v=4)/1000  # [m]
    mass = particle_density*4./3.*np.pi*(radius**3)
    # x = np.random.uniform(low=-boxsize/2., high=boxsize/2.)
    # r = np.random.uniform(low=300, high=400)
    r = np.random.uniform()
    rs = r*10 + 600
    theta = np.random.uniform()*2*np.pi
    x = rs*np.cos(theta)
    y = rs*np.sin(theta)
    sim.add(
        m=mass,
        r=radius,
        x=x,
        # y=np.random.uniform(low=-boxsize/2., high=boxsize/2.),
        y=y,
        z=np.random.normal(),
        # vx = 0.,
        vx = OMEGA*(r+.5)*np.sin(theta),
        # vy = -3./2.*x*OMEGA*(r+.5),
        vy = OMEGA*(r+.5)*np.cos(theta),
        vz = 0.)
    count += 1

sim.add(m=10000, r=2, x=0, y=0, z=0, vx = 0., vy = 0., vz = 0.)

import matplotlib.patches as patches
def plotParticles(sim):
    fig = plt.figure(figsize=(8,8))
    ax = plt.subplot(111,aspect='equal')
    ax.set_ylabel("radial coordinate [m]")
    ax.set_xlabel("azimuthal coordinate [m]")
    ax.set_ylim(-boxsize/2.,boxsize/2.)
    ax.set_xlim(-boxsize/2.,boxsize/2.)

    for i, p in enumerate(sim.particles):
        circ = patches.Circle((p.y, p.x), p.r*100, facecolor='darkgray', edgecolor='black')
        ax.add_patch(circ)
    plt.show()

def plotParticles2(sim, k):
    fig = plt.figure(figsize=(8,8))
    ax = plt.subplot(111,aspect='equal')
    ax.set_ylabel("radial coordinate [m]")
    ax.set_xlabel("azimuthal coordinate [m]")
    ax.set_ylim(-boxsize/2.,boxsize/2.)
    ax.set_xlim(-boxsize/2.,boxsize/2.)

    for i, p in enumerate(sim.particles):
        circ = patches.Circle((p.y, p.x), p.r*100, facecolor='darkgray', edgecolor='black')
        ax.add_patch(circ)
    # plt.show()
    plt.savefig('./figuresnew2/ring_dynamics_'+str(k)+'.png')
    fig.clf()
    plt.close()
    # plt.cla()

sim.move_to_com()
sim.status()
plotParticles2(sim, 0)

# sim.integrate(1000)
print(2.*np.pi/OMEGA/sim.dt)
# gives ~ 478
for i in range(236):
    print(i)
    sim.integrate(sim.t+1000*sim.dt)
    sim.move_to_com()
    plotParticles2(sim, i+1)


# sim.integrate(2*2.*np.pi/OMEGA)

sim.move_to_com()
# fig, ax = rebound.OrbitPlot(sim, unitlabel="/AU", color=True, periastron=True, xlim=[-3, 3], ylim=[-3, 3])
fig, ax = rebound.OrbitPlot(sim, color=True)
# ax.set_xlim(-1000, 1000)
# ax.set_ylim(-1000, 1000)


# plt.show()
# plotParticles(sim)