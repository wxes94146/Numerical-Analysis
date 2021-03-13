import numpy as np
import matplotlib.pyplot as plt

def dy(t, y):
    return y - t**2 + 1
def y_true(t):
    return (t + 1)**2 - 0.5 * np.exp(t)
n = 10
a = 0
b = 2
h = (b-a)/n
t = np.linspace(a, b, n+1)

# Euler's Method
w = np.zeros((n+1, 1))
w[0] = 0.5
print('%.2f'%t[0], '%.6e'%w[0],y_true(t[0]))
for i in range(n):
    w[i+1] = w[i] + h * dy(t[i], w[i])
    print('%.2f'%t[i+1], 'w = %.6e'%w[i+1], y_true(t[i+1]))
plt.plot(t, w)

# Midpoint Method
print('%.2f'%t[0], '%.6e'%w[0],y_true(t[0]))
for  i in range(n):
    w[i+1] = w[i] + h * dy(t[i] + h/2, w[i] + h/2 * dy(t[i], w[i]))
    print('%.2f'%t[i+1], '%.6e'%w[i+1], y_true(t[i+1]))
plt.plot(t, w)

# Rung Kutta
print('%.2f'%t[0], '%.6e'%w[0], y_true(t[0]))
for i in range(n):
    k1 = h * dy(t[i], w[i])
    k2 = h * dy(t[i] + 1/2 * h, w[i] + k1 * 1/2)
    k3 = h * dy(t[i] + 1/2 * h, w[i] + k2 * 1/2)
    k4 = h * dy(t[i] + h, w[i] + k3)
    w[i+1] = w[i] + (k1+2*k2+2*k3+k4)/6
    print('%.2f'%t[i+1], '%.6e'%w[i+1], y_true(t[i+1]))
plt.plot(t, w)

# Modified Euler's Method
print('%.2f'%t[0], '%.6e'%w[0], y_true(t[0]))
for i in range(n):
    w[i+1] = w[i] + (1/2)*h*(dy(t[i], w[i]) + dy(t[i+1], w[i] + h*dy(t[i], w[i])))
    print('%.2f'%t[i+1], '%.6e'%w[i+1], y_true(t[i+1]))
plt.plot(t, w)