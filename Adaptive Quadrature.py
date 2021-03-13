import numpy as np

Tol = 1.0e-6 #誤差從這裡改，e表示科學記號10
x_intervals = np.array([])

def my_func(x):
    return np.log(x) #函數從這裡改

def adaptive_Gauss(f,a,b,n):
    c = (a+b)/2
    n_gauss_pt = 2

    f1 = my_Gauss_quad(f,a,b,n_gauss_pt)
    f2 = my_Gauss_quad(f,a,c,n_gauss_pt) + my_Gauss_quad(f,c,b,n_gauss_pt)

    if np.abs(f2-f1) > 15*Tol:
        if n == 0:
            return f2
        return adaptive_Gauss(f,a,c,n-1)+adaptive_Gauss(f,c,b,n-1)
    else:
        return f2
    
def my_Gauss_quad(func,a, b, n):

    global x_intervals
    x_intervals = np.append(np.array([a,b]),x_intervals)
    
    c = np.array([2, 1, 1, 5/9, 8/9, 5/9])
    x = np.array([0,np.sqrt(1/3),-np.sqrt(1/3),np.sqrt(3/5),0,-np.sqrt(3/5)])
    start = np.array([0, 1, 3])   # n*(n-1)/2
    
    my_integral = 0
    for i in range(start[n-1],start[n-1]+n):   # loop for nth-order Gaussian quadrature
        my_integral = my_integral + c[i]*func((b-a)/2*x[i]+(a+b)/2)
    return my_integral*(b-a)/2    

a = 0
b = 2
#積分上下界

print('integral = ', adaptive_Gauss(my_func,a,b,100))