import numpy as np

c = np.array([1, 1, 0.5555555556, 0.8888888889, 0.5555555556,
              0.3478548451, 0.6521451549, 0.6521451549, 0.3478545451,
              0.2369268850561890, 0.4786286704993660, 0.5688888888888880, 0.4786286704993660, 0.2369268850561890])

xi = np.array([np.sqrt(1/3), -np.sqrt(1/3), np.sqrt(3/5), 0, -np.sqrt(3/5),
               -0.8611363116, -0.3399810436, 0.3399810436, 0.8611363116,
               -0.9061798459386640, -0.5384693101056830, 0, 0.5384693101056830, 0.9061798459386640])

start = np.array([0, 2, 5, 9])

def my_fun(x):
    return x**6

n = 5
my_integral = 0
for i in range(start[n-2],start[n-2]+n): # loop for nth-order Gaussian quadrature
    my_integral = my_integral + c[i]*my_fun(xi[i])
    
print('\n appr. value = ',my_integral, '\n exact value = ', 2/7)




c = np.array([1, 1, 0.5555555556, 0.8888888889, 0.5555555556,
              0.3478548451, 0.6521451549, 0.6521451549, 0.3478545451,
              0.2369268850561890, 0.4786286704993660, 0.5688888888888880, 0.4786286704993660, 0.2369268850561890])

xi = np.array([np.sqrt(1/3), -np.sqrt(1/3), np.sqrt(3/5), 0, -np.sqrt(3/5),
               -0.8611363116, -0.3399810436, 0.3399810436, 0.8611363116,
               -0.9061798459386640, -0.5384693101056830, 0, 0.5384693101056830, 0.9061798459386640])

start = np.array([0, 2, 5, 9])

def my_fun(x):
    return np.sin(x)

n = 5
a = 0
b = np.pi
my_integral = 0
for i in range(start[n-2],start[n-2]+n): #loop for nth-order Gaussian quadrature
    my_integral = my_integral + c[i]*my_fun(((b-a)/2)*xi[i]+(b+a)/2)
    
print('\n appr. value = ',((b-a)/2)*my_integral, '\n exact value = ', 2)