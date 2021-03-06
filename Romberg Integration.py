import numpy as np
import matplotlib.pyplot as plt

def my_func(x):
    return np.sin(x)   #np.log(np.sin(x))-np.log(x) 

def composite_trapezoid(y,h):
    return (np.sum(y)+np.sum(y[1:-1]))*h/2

m = 5
n = 2**m
a = 0
b = np.pi
x = np.linspace(a,b,2**m+1)
yy = my_func(x)
A = np.zeros((m+1,m+1))

for i in range(m+1):
    y = yy[::2**(m-i)]
    h = (b-a)/2**i
    A[i,0]=composite_trapezoid(y,h)
    
    for j in range(1,i+1):
        A[i,j]=A[i,j-1]+(A[i,j-1]-A[i-1,j-1])/(4**j-1)
    
    print('\n %.2d ' % 2**i, end='')
    for j in range(0,i+1):
        print(' %.12e' % A[i,j], end='')

for i in range(m+1):    
    h = np.pi/(2**(np.arange(i,m+1)))
    integral_err = np.abs(2 - A[i:,i])
    
    plt.plot(h, integral_err,'o-',label=str(i+1))
    plt.yscale('log')
    plt.xscale('log')
    plt.legend(loc='upper right', shadow=True)
    
plt.title('Romberg Integration with Trapezoidal Rule\n\n Error v.s. h')
plt.xlabel(' h (log scale) ')
plt.ylabel(' Error (log scale)')
plt.xticks([0.1, 1, 10])
plt.show