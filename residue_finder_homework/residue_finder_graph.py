# This script creates a 3D plot for the associated residues calculated in the residue_finder.py script.
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

filepath = 'C:\\Users\\HP\\PycharmProjects\\Hw7\\1ubq.pdb'

coordinates_x = []
coordinates_y = []
coordinates_z = []

with open(filepath) as pdbfile:
    for line in pdbfile:
        if line.startswith('ATOM'):
            boluk = line.split()
            atomName = boluk[2]
            atomNumber = boluk[1]
            atomList = boluk
            residueName = boluk[3]
            if atomName == 'CA':
                coordinates_x.append(float(boluk[6]))
                coordinates_y.append(float(boluk[7]))
                coordinates_z.append(float(boluk[8]))

ax = plt.gca(projection="3d")
x, y, z = coordinates_x, coordinates_y, coordinates_z
ax.scatter(x, y, z, c='blue', s=30)
ax.plot(x, y, z, color='red')
plt.show()
plt.savefig("Enter directory name", dpi=72)
