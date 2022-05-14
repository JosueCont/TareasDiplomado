#metodo diferencias finitas progersivas

from math import sin

def f(x):
    return (((sin(2*x))**(3)) / (x**4 +1))

x0 = 2.45
h1 = 0.000001

r1 = ((f(x0+h1)-f(x0))/h1)
print("r1 =",r1)