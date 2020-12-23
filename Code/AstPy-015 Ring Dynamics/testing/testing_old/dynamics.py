import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.patches import Circle
import rebound

from datetime import datetime

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Time =", current_time)

sim = rebound.Simulation()

sim.units = ('km', 's', 'kg')
# sim.G = 6.67428e-11 # N m^2/kg^2
sim.dt = 100
sim.softening = 0.2
# sim.integrator = "sei"
# sim.boundary   = "shear"
sim.gravity    = "basic"
sim.collision  = "direct"
sim.collision_resolve = "hardsphere"

# boxsize = 200000000
# sim.configure_box(boxsize)
# sim.configure_ghostboxes(2, 2, 0)

def cor_bridges(r, v):
        eps = 0.32*pow(abs(v)*100.,-0.234)
        if eps>1.:
            eps=1.
        if eps<0.:
            eps=0.
        return eps
sim.coefficient_of_restitution = cor_bridges

# Saturn
sim.add("699")

# Mimas
sim.add("601")

# sim.add("602") # Enceladus
# sim.add("610") # Janus
# sim.add("611") # Epithemius
# sim.add("617") # Pandora
# sim.add("616") # Prometheus
# sim.add("618") # Pan
# sim.particles[-1].m = 4.95e15
# sim.add("615") # Atlas
# sim.add("635") # Daphnis
# left out anthe, methone, and pallene

sim.move_to_com()
sim.status()

def powerlaw(slope, min_v, max_v):
    y = np.random.uniform()
    pow_max = pow(max_v, slope+1.)
    pow_min = pow(min_v, slope+1.)
    return pow((pow_max-pow_min)*y + pow_min, 1./(slope+1.))

particle_density = 1 # kg/m^3
l = 100000
h = 130000

print('Adding ring particles')
count = 0
# while count < 1000:
#     radius = powerlaw(slope=-4, min_v=1, max_v=4)/1000  # m
#     mass = particle_density*4./3.*np.pi*(radius**3)
#     a = np.random.uniform(low=l, high=h)
#     sim.add(m=mass, r=radius, a=a)
#     count += 1
while count < 1000:
    radius = powerlaw(slope=-4, min_v=1, max_v=4)/1000  # [m]
    mass = particle_density*4./3.*np.pi*(radius**3)
    r = np.random.uniform()
    rs = r*(h-l) + l
    theta = np.random.uniform()*2*np.pi
    x = rs*np.cos(theta)
    y = rs*np.sin(theta)
    ts = np.sqrt(r**3)
    v = np.pi*r*2/ts
    # print(v*np.sin(theta))
    sim.add(
        m=mass,
        r=radius,
        x=x,
        # y=np.random.uniform(low=-boxsize/2., high=boxsize/2.),
        y=y,
        z=np.random.normal(),
        # vx = 0.,
        vx = v*np.sin(theta),
        # vy = -3./2.*x*OMEGA*(r+.5),
        vy = v*np.cos(theta),
        vz = 0.)
    count += 1
print('Finished adding ring particles')

def plotParticles(sim, k):
    fig = plt.figure(figsize=(8,8))
    ax = plt.subplot(111, aspect='equal')
    ax.set_ylabel("y / km")
    ax.set_xlabel("x / km")
    ax.set_xlim(-200000, 200000)
    ax.set_ylim(-200000, 200000)
    ax.set_aspect('equal')
    ax.ticklabel_format(axis="both", style="sci", scilimits=(0,0))
    for i, p in enumerate(sim.particles):
        if i == 0:
            fc, ec, a, r = "goldenrod", "None", 1, 58232
        elif i == 2:
            fc, ec, a, r = "dimgrey", "None", 1, 198.2*10/2
        else:
            fc, ec, a, r = "lightgray", "k", 1, p.r*100
        circ = Circle((p.y, p.x), r, facecolor=fc, edgecolor=ec, alpha=a)
        ax.add_patch(circ)
    plt.savefig('./figures6/dynamics_'+str(k)+'.png')
    # plt.show()
    fig.clf()
    plt.close()

def plotHistA(sim, k):
    A = []
    for i, p in enumerate(sim.particles):
        A.append(np.sqrt(p.x**2+p.y**2))
    fig = plt.figure(num=1, figsize=(10,5))
    ax = plt.subplot(111)
    ax.hist(A, 10000, histtype="stepfilled") # 10 km bins
    ax.set_xlim(l, h)
    plt.savefig("./figures6/a_dist_"+str(k)+".png")
    fig.clf()
    plt.close()

# fig, ax = rebound.OrbitPlot(sim, color=True, unitlabel="/ km")
# ax.set_xlim(-200000, 200000)
# ax.set_ylim(-200000, 200000)
# ax.set_aspect('equal')
# ax.ticklabel_format(axis="both", style="sci", scilimits=(0,0))

# plotParticles(sim, 0)
# sim.integrate(28.4/2*60*60)
# plotParticles(sim, 1)

get_time()

plotHistA(sim, 0)
plotParticles(sim, 0)
mimas_orbit = 23*60*60 # s
for i in range(50):
    sim.integrate(sim.t + mimas_orbit/10)
    plotParticles(sim, i+1)
    plotHistA(sim, i+1)

get_time()

sim.save("mimSat5orbits.bin")
# del sim
# sim = rebound.Simulation("checkpointwithMoonsAllOver.bin")

# sim.move_to_com()
# sim.status()

# fig, ax = rebound.OrbitPlot(sim, color=True, unitlabel="/ km")
# ax.set_xlim(-200000, 200000)
# ax.set_ylim(-200000, 200000)
# ax.set_aspect('equal')
# ax.ticklabel_format(axis="both", style="sci", scilimits=(0,0))
# plt.show()