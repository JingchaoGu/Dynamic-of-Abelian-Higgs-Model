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
# Change x and p_x to Get Phase Portrait for y-p_y
plt.plot(x, px,marker=',', linestyle='', markersize=0.5, color = 'black') 
plt.xlabel('x')
plt.ylabel('y')
plt.title('Phase Portrait with kap=...')   
plt.show()