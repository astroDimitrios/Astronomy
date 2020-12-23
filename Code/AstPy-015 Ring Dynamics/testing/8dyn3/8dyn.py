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
sim.integrator = "mercurius"
sim.dt = 1
sim.testparticle_type = 1
sim.ri_ias15.min_dt = 1e-6
# sim.softening = 0.2
# sim.integrator = "sei"
# sim.boundary   = "shear"
# sim.gravity    = "basic"
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
# sim.particles[-1].r = 58232

# Mimas
sim.add("601")
# sim.particles[-1].r = 198

sim.add("602") # Enceladus
sim.add("610") # Janus
sim.add("611") # Epithemius
sim.add("617") # Pandora
sim.add("616") # Prometheus
sim.add("618") # Pan
sim.particles[-1].m = 4.95e15
sim.add("615") # Atlas
# sim.add("635") # Daphnis
# left out anthe, methone, and pallene

sim.N_active = sim.N

sim.move_to_com()
sim.status()

def powerlaw(slope, min_v, max_v):
    y = np.random.uniform()
    pow_max = pow(max_v, slope+1.)
    pow_min = pow(min_v, slope+1.)
    return pow((pow_max-pow_min)*y + pow_min, 1./(slope+1.))

particle_density = 1 # kg/m^3
l = 70000
h = 200000

print('Adding ring particles')
count = 0
# while count < 1000:
#     radius = powerlaw(slope=-4, min_v=1, max_v=4)/1000  # m
#     mass = particle_density*4./3.*np.pi*(radius**3)
#     a = np.random.uniform(low=l, high=h)
#     sim.add(m=mass, r=radius, a=a)
#     count += 1
mass_tot = 0
while count < 10000:
    radius = powerlaw(slope=-4, min_v=1, max_v=4)  # [m]
    mass = particle_density*4./3.*np.pi*(radius**3)
    r = np.random.uniform()
    rs = r*(h-l) + l
    theta = np.random.uniform()*2*np.pi
    x = rs*np.cos(theta)
    y = rs*np.sin(theta)
    # ts = np.sqrt(r**3)
    # v = np.pi*r*2/ts
    v = np.sqrt(6.67428e-11 * sim.particles[0].m/ (rs*1000)) / 1000 * .8# km/s
    # print(v*np.sin(theta))
    z = np.random.normal()
    # 8dyn2 had no vz and no * .8 in the v and upper lim 130,000 km
    sim.add(
        m=mass,
        r=radius,
        x=x,
        # y=np.random.uniform(low=-boxsize/2., high=boxsize/2.),
        y=y,
        z=z,
        # vx = 0.,
        vx = -v*np.sin(theta),
        # vy = -3./2.*x*OMEGA*(r+.5),
        vy = v*np.cos(theta),
        vz = -z/10)
    count += 1
    mass_tot += mass
print('Finished adding ring particles')
print(mass_tot)

rads = [58232, 198.2, 504/2, 178/2, 116.2/2, 81.4/2, 84.2/2, 14, 15.1, 7.6/2]

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
        elif i < 9:
            fc, ec, a, r = "dimgrey", "None", 1, rads[i]*10
        else:
            fc, ec, a, r = "lightgray", "k", 1, p.r/100
        circ = Circle((p.x, p.y), r, facecolor=fc, edgecolor=ec, alpha=a)
        ax.add_patch(circ)
    plt.savefig('./8dyn3/dynamics_'+str(k)+'.png', dpi=300)
    # plt.show()
    fig.clf()
    plt.close()

def plotHistA(sim, k):
    A = []
    for i, p in enumerate(sim.particles):
        A.append(np.sqrt(p.x**2+p.y**2))
    fig = plt.figure(num=1, figsize=(10,5))
    ax = plt.subplot(111)
    freq, bins = np.histogram(A[9:], bins=range(l, h+10, 10))
    top_freq = 100
    # ax.hist(A, bins=range(l, h+10, 10), histtype="stepfilled") # 10 km bins
    for i in range(len(bins)-1):
        alpha = freq[i]/top_freq
        ax.axvline(bins[i], 0, 1, color='blue', alpha=alpha)
    ax.set_xlim(l, h)
    ax.tick_params(
    axis='y',          
    which='both',      
    right=False,     
    left=False,       
    labelleft=False) 
    plt.savefig("./8dyn3/a_dist_"+str(k)+".png", dpi=300)
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
for i in range(200):
    sim.integrate(sim.t + mimas_orbit/100)
    plotParticles(sim, i+1)
    plotHistA(sim, i+1)

get_time()

sim.save("8dyn3.bin")
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