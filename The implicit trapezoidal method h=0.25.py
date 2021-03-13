import numpy as np

def myfun_y(t,y):
    return 5*np.exp(5*t)*(y-t)**2+1

def myfun(t):
    return t - np.exp(-5*t)
def fun(x,w,t):
    return w + h/2*myfun_y(t,w) + h/2*(5*np.exp(5*(t+h))*(x-(t+h))**2 + 1) - x 
def my_deri(x,t):
    return h/2*5*np.exp(5*(t+h))*2*(x-(t+h))-1
def my_newton(f, df, x0, t): #Newton's method to find root
    iter_max = 20
    Tol = 1.0e-6
    x_old = x0
    x_new = x_old - f(x_old, x0, t)/df(x_old, t)
    count = 0
    while abs(x_new - x_old) > Tol and count < iter_max:
        count = count +1
        x_old = x_new
        x_new = x_old - f(x_old, x0, t)/df(x_old, t)
    if count < iter_max :
        return x_new
    else:
        print('divergent')
        quit()    

a = 0
b = 1
n = 4
h = (b-a)/n
t = np.linspace(0, 1, n+1)
w = np.zeros(n+1) #Euler Method 
w[0] = -1
for i in range(n):
    w[i+1]= my_newton(fun, my_deri, w[i], t[i])
    print('%.2f   '%t[i+1],'%.7f'%w[i+1])