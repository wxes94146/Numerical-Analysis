import numpy

#辛普森法
def f(x):
  return numpy.sin(x)
n = 10
a = 0
b = numpy.pi
h = (b-a)/n
s = 0
for i in range(0,n,2):
  s = s+f(a+i*h)+4*f(a+(i+1)*h)+f(a+(i+2)*h)
print(s*h/3)

#梯形法
def f(x):
  return x**10
def trapz(f,a,b,N):
    """
    Approximate the definite integral of f(x) from a to b by the 
    composite trapezoidal rule, using N subintervals
 
    For example:
    trapz(lambda x: x**2+2*x+1,0.0,3.0,100)
    """
    return (b-a)*(float(f(a)+f(b))/2+sum([float(f(a+(b-a)*k/N)) for k in range(1,N)]))/N
print(trapz(f,0,1,5))

#牛頓法
def f(x):
  return x**2-2
def df(x):
  return 2*x
x_old = 1
for i in range(0,5):
  x_new = x_old - f(x_old)/df(x_old)
  x_old = x_new
print(x_old)