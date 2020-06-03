import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Lithosphere geothermal gradient

Ts = 15 # surface temp (deg C)
Q = 30 # mantle heat flow (mW/m^2)
K = 2.5 # thermal conductivity (W/m/deg)
Ao = 2.0 # heat production (microW/m^3)
b = 10 # characteristic depth of Ao (km)

z = np.arange(0,100,.1)
T = []

for i in z:
    if i < b:
        T.append(Q*i/K + Ao*i*(b-i/2)/K + Ts)
    else:
        T.append(Q*i/K + Ao*b**2/(2*K) + Ts)

fig = plt.figure(num=1, figsize=(6, 10))
plt.plot(T, -z)

# plt.show()

axins = inset_axes(plt.gca(), width="40%", height="40%")
axins.plot(T, -z)
axins.set_ylim(-35, 0)
axins.set_xlim(0, 500)

plt.show()

# file = 'geotherm.csv'

# df = pd.read_csv(file)

# print(df.head())
