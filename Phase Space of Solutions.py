import numpy as np
import matplotlib.pyplot as plt

# Specify the time points where Runge Kutta Method is Performed
t_start = 0
t_end = 100
num_steps = 10000
time_points = np.linspace(t_start, t_end, num_steps)


# Calculate Initial Value for p_y
def py_inti(x0,y0,px0,k):
    return (0.25-k/2*(-1+y0**2)**2-x0**2*y0**2-px0**2)**(1/2)


# Specify Coupling Constant
k= 5.0 
# Generate Initial Condition
px0 = np.random.uniform(0, 0.1)
y0 = np.random.uniform((-(0.5/k)**1/2 + 1)**(1/2), ((0.5/k)**1/2 + 1)**(1/2))
x0 = np.random.uniform(-((0.25-k/2*(-1+y0**2)**2-px0**2)/y0**2)**(1/2), ((0.25-k/2*(-1+y0**2)**2-px0**2)/y0**2)**(1/2))
py0 = py_inti(x0,y0,px0,k)
state0 = x0,px0,y0,py0
solution = runge_kutta_system(system_of_odes, state0, time_points)
x = solution[:,0]
px = solution[:,1]
y = solution[:,2]
py = solution[:,3]
# Plot Phase Portrait
plt.figure(1)
plt.plot(x, y,marker=',', linestyle='', markersize=0.5, color = 'black') 
plt.xlabel('x')
plt.ylabel('y')
plt.title('Phase Space of Solution xy with kap=...')   
plt.show()

plt.figure(2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(x, y, px,c=py, cmap='plasma',marker=',',s=0.1)
cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('py')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('px')
plt.title('Phase Space of Solution with kap=...')      
ax.view_init(elev=0, azim=90)  