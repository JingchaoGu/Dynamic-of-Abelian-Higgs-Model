import numpy as np
import matplotlib.pyplot as plt
import random


def runge_kutta_system(f, states0, t):
    h = 0.01 #time stpe
    num_equations = len(states0)
    results = np.zeros((len(t), num_equations))
    results[0] = states0
    for i in range(1, len(t)):
        k1 = h * f(t[i - 1], results[i - 1])
        k2 = h * f(t[i - 1] + h / 2, results[i - 1] + k1 / 2)
        k3 = h * f(t[i - 1] + h / 2, results[i - 1] + k2 / 2)
        k4 = h * f(t[i - 1] + h, results[i - 1] + k3)
        results[i] = results[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return results


def system_of_odes(t, states):
    k = 5.0
    x, px, y, py = states
    dx_dt = px
    dpx_dt = -x * y**2
    dy_dt = py
    dpy_dt = -y * x**2 - k * (-1 + y**2) * y
    return np.array([dx_dt, dpx_dt, dy_dt, dpy_dt])
