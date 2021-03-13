import numpy as np
import matplotlib.pyplot as plt

def dy(t, y):
    return y - t**2 + 1
def y_true(t):
    return (t + 1)**2 - 0.5 * np.exp(t)
n = 10
a = 0
b = 2
h = 0.2
t = np.linspace(a, b, n+1)
w = np.zeros((n+1, 1))
w[0] = 0.5

# Rung Kutta
print('%.2f'%t[0], '%.6e'%w[0], y_true(t[0]))
for i in range(4):
    k1 = h * dy(t[i], w[i])
    k2 = h * dy(t[i] + 1/2 * h, w[i] + k1 * 1/2)
    k3 = h * dy(t[i] + 1/2 * h, w[i] + k2 * 1/2)
    k4 = h * dy(t[i] + h, w[i] + k3)
    w[i+1] = w[i] + (k1+2*k2+2*k3+k4)/6
    print('%.2f'%t[i+1], '%.6e'%w[i+1], y_true(t[i+1]))

for i in range(4, n):
    w[i+1] = w[i] + (h/24)*(55*dy(t[i], w[i]) - 59*dy(t[i-1], w[i-1]) + 37*dy(t[i-2], w[i-2]) - 9*dy(t[i-3], w[i-3]))
    print('%.2f'%t[i+1], '%.6e'%w[i+1], y_true(t[i+1]))
plt.plot(t, w)