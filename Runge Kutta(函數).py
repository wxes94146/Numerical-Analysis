import numpy as np

def dy(t, y):
    return y*(2-y)

def F(dy, t0, y0, h, n):
  t = np.linspace(0, 2, n+1)
  w = np.zeros((n+1, 1))
  w[0] = y0
  for i in range(n):
    k1 = h * dy(t[i], w[i])
    k2 = h * dy(t[i] + 1/2 * h, w[i] + k1 * 1/2)
    k3 = h * dy(t[i] + 1/2 * h, w[i] + k2 * 1/2)
    k4 = h * dy(t[i] + h, w[i] + k3)
    w[i+1] = w[i] + (k1+2*k2+2*k3+k4)/6
  return (t, w)

a = F(dy, 0, 0.1, 0.2, 5)
for i in range(6):
  print('%.1f'%a[0][i], a[1][i])