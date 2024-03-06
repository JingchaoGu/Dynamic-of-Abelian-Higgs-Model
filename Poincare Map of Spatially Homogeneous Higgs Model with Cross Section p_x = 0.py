import numpy as np
import matplotlib.pyplot as plt
import random
t_start = 0
t_end = 100
num_steps = 10000
time_points = np.linspace(t_start, t_end, num_steps)
def py_inti(x0,y0,px0,k):
    return (0.25-k/2*(-1+y0**2)**2-x0**2*y0**2-px0**2)**(1/2)
N = 64
k= 5.0
for i in range(N):
    px0 = 0.01
    prob = random.randint(0,1)
    if prob == 0:
        y0 = np.random.uniform(-((0.5/k)**1/2 + 1)**(1/2), -(-(0.5/k)**1/2 + 1)**(1/2))
    else:
        y0 = np.random.uniform((-(0.5/k)**1/2 + 1)**(1/2), ((0.5/k)**1/2 + 1)**(1/2))
    
    x0 = np.random.uniform(-((0.25-k/2*(-1+y0**2)**2-px0**2)/y0**2)**(1/2), ((0.25-k/2*(-1+y0**2)**2-px0**2)/y0**2)**(1/2))
    py0 = py_inti(x0,y0,px0,k)
    state0 = x0,px0,y0,py0
    solution = runge_kutta_system(system_of_odes, state0, time_points)
    x = solution[:,0]
    px = solution[:,1]
    y = solution[:,2]
    py = solution[:,3]
    xx=[]
    yy=[]
    for j in range(len(px)-1):
        if (px[j] <=0 and px[j+1] >= 0) or (px[j] >=0 and px[j+1] <= 0):
            xp = -px[j]*((x[j+1] - x[j])/(px[j+1] - px[j])) + x[j]
            yp = -px[j]*((y[j+1] - y[j])/(px[j+1] - px[j])) + y[j]
            xx.append(xp)
            yy.append(yp)
        plt.plot(xx,yy,marker=',', linestyle='', markersize=0.5, color = 'black') 
plt.xlabel('x')
plt.ylabel('y')
plt.title('Poincare Map')   