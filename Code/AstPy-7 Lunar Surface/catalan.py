import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file = './RDR_272E273E_46p130529S45SPointPerRow_csv_table/RDR_272E273E_46p130529S45STopoFull_csv_table.csv'

df = pd.read_csv(file)

fig = plt.figure(num=1)
ax = fig.gca(projection='3d')

X = df['Pt_Longitude']
Y = df['Pt_Latitude']
Z = df['topography']

surf = ax.plot_trisurf(X, Y, Z, cmap='Greys', edgecolor='none')
fig.colorbar(surf)

# for i in range(0,91,1):
#     ax.view_init(elev=0+i, azim=i)
#     plt.savefig('./catalan/catalan%d.png' % i)

plt.show()