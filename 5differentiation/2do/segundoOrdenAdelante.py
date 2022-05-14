#Derivada de segundo orden hacia adelante

from math import sin

def f(x):
    return (((sin(2*x))**(3)) / (x**4 +1))

x0 = 2.45
h1 = 0.000001

r1 = ((f(x0+(2*h1))-(2*f(x0+h1))+f(x0))/(h1**2))
print("r1 =",r1)