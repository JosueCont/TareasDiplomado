from math import sin, sqrt

def f(x):
    return 2*(sin(sqrt(x))-x)

a = 0
b = 1.9724
m = (a+b)/2

r1 = f(m)*(b-a)
print("Regla del punto medio: ",r1)

r2 = ((b-a)/6)*(f(a)+4*f(m)+f(b))
print("con regla de simpson: ",r2)

