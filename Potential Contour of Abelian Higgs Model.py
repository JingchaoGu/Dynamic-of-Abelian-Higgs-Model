import numpy as np
import matplotlib.pyplot as plt

# Set range of x and y axis
X = np.linspace(-1.5, 1.5, 1000)
Y = np.linspace(-1.5, 1.5, 1000)

# Potential of Abelian Higgs Model
def potential(x,y, kap):
    return 1/2*x**2*y**2 + kap/4*(-1+y**2)**2

xx,yy = np.meshgrid(X,Y)

# Calculate Energy Levels
Z = potential(xx, yy, kap) # kap is coupling constant
levels = np.linspace(0, 0.5,17)

# Plot Potential Contours
fig, ax = plt.subplots() 
contours = ax.contour(X, Y, Z, levels) 
ax.clabel(contours,levels=levels[0:6], inline=1, fontsize=10)
plt.title('Potential Contours') 

