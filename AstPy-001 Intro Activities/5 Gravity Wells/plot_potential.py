import numpy as np
import matplotlib.pyplot as plt

from matplotlib.colors import SymLogNorm
from matplotlib import ticker
from potential import Body, single_potential, potential

AU = 1.495978707*10**11    # m

# Set up SEM system in a line
Earth = Body.Earth(1, 0)
Sun = Body.Sun(-0.5, 0)
Sun2 = Body('Sun2', 0.5, 0, 695700/5, 1988500*10**24/3)
Jupiter = Body('Jupiter', 5.2, 0, 69911, 1.89813*10**27)
Moon = Body('Moon', 1+0.00256955529, 0, 384400000, 7.34767309*10**22)

x_min, x_max = (-2, 2)                   # min and max x values 
y_min, y_max = (-2, 2)                   # min and max y values
# x_min, x_max = (0.99, 1.01)                   # min and max x values 
# y_min, y_max = (-0.01, 0.01)                   # min and max y values
# increase values for finer resolution
x_res, y_res = (1000, 1000)                  # x, y shape of grid
x = np.linspace(x_min, x_max, x_res)
y = np.linspace(y_min, y_max, y_res)
# Create a 2D grid
X, Y = np.meshgrid(x, y, indexing='ij')

# calculate combined potential
# U_Comb = potential(X, Y, [Earth, Sun, Moon])
# U_Comb = potential(X, Y, [Earth])
# U_Comb = potential(X, Y, [Sun, Jupiter]) # Interesting
U_Comb = potential(X, Y, [Sun, Sun2])
U_Comb = U_Comb.astype('float64') 

fig = plt.figure(num=1, figsize=(10, 10))
ax = fig.add_subplot(111, label="ax")
# data = ax.pcolormesh(X, Y, U_Comb, cmap='viridis', vmin=np.min(U_Comb), vmax=np.max(U_Comb), shading='auto')
# cbar = plt.colorbar(data, ax=ax, fraction=0.05, pad=0.04)
# cbar.outline.set_visible(False)

levels = np.linspace(0.1, 1, 40)
levels = abs(np.log10(levels))
levels = levels**2
levels = (levels-np.amin(levels))/(np.amax(levels)-np.amin(levels))
levels = levels*np.amin(U_Comb)
print(levels)
levels = [-2333457275,-2233457275,-2133457275,-2033457275,-1900000000, -1800000000, -1700000000,
          -1600000000, -1500000000, -1400000000]
# plt.clim(-62560988.47904567,0)
# data = ax.contour(X, Y, U_Comb, cmap='viridis',
#                   locator=ticker.SymmetricalLogLocator(base=1.2,linthresh=.01),
#                   norm=SymLogNorm(linthresh=0.03, linscale=0.03,
#                                   vmin=np.amin(U_Comb), vmax=np.amax(U_Comb), base=2),
#                   zorder=-1)
data = ax.contour(X, Y, U_Comb, cmap='viridis',
                  levels=levels,
                  norm=SymLogNorm(linthresh=0.03, linscale=0.03,
                                  vmin=np.amin(U_Comb), vmax=np.amax(U_Comb), base=2),
                  zorder=-1)
# ax.clabel(data, inline=True, fontsize=10, fmt='%.0f', zorder=0)

print(np.amin(U_Comb))
print(np.amax(U_Comb))

plt.show()
# plt.savefig('test.png', dpi=300)