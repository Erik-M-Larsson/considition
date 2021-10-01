
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

[vehicle_length, vehicle_width, vehicle_height] = [70, 50, 50]

paket = [{
    "id": 56, 
    "x1": 0,
    "x2": 0,
    "x3": 0,
    "x4": 0,
    "x5": 23,
    "x6": 23,
    "x7": 23,
    "x8": 23,
    "y1": 0,
    "y2": 0,
    "y3": 0,
    "y4": 0,
    "y5": 25,
    "y6": 25,
    "y7": 25,
    "y8": 25,
    "z1": 0,
    "z2": 0,
    "z3": 0,
    "z4": 0,
    "z5": 9,
    "z6": 9,
    "z7": 9,
    "z8": 9,
    "weightClass": 2,
    "orderClass": 3
},
{
   "id": 5, 
    "x1": 25,
    "x2": 25,
    "x3": 25,
    "x4": 25,
    "x5": 35,
    "x6": 35,
    "x7": 35,
    "x8": 35,
    "y1": 0,
    "y2": 0,
    "y3": 0,
    "y4": 0,
    "y5": 10,
    "y6": 10,
    "y7": 10,
    "y8": 10,
    "z1": 0,
    "z2": 0,
    "z3": 0,
    "z4": 0,
    "z5": 5,
    "z6": 5,
    "z7": 5,
    "z8": 5,
    "weightClass": 2,
    "orderClass": 3
  }]
  
  
  

x, y, z = np.indices((vehicle_length, vehicle_width, vehicle_height))

paket_rep = (paket[0]["x1"] <= x) & (x <= paket[0]["x5"]) & (paket[0]["y1"] <= y) & (y <= paket[0]["y5"]) & (paket[0]["z1"] <= z) & (z <= paket[0]["z5"])

voxels = paket_rep

# Controll Tranperency
alpha = 0.1

# set the colors of each object
colors = np.empty(voxels.shape, dtype=object)
colors[:] = 'green'



# Create axis
#axes = [vehicle_length, vehicle_width, vehicle_height]



# Control colour
#colors = np.empty(axes + [4], dtype=np.float32)
#colors[:] = [0, 1, 0, alpha]  # green

'''for pak in paket:
    l, b, h = pak["x5"] - pak["x1"], pak["y5"] - pak["y1"], pak["z5"] - pak["z1"]
    

    
    # Create Data
    data =  #np.ones(axes, dtype=bool)

    ax = fig.add_subplot(111, projection='3d')
    # Voxels is used to customizations of the
    # sizes, positions and colors.
    ax.voxels(data, facecolors=colors) #, edgecolors='grey')
'''
# set the colors of each object
colors = np.empty(voxels.shape, dtype=object)
colors[:] = 'green'

# Plot figure
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
ax.voxels(voxels, facecolors=colors)
plt.show()
