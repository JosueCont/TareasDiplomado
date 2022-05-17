def f(x):
    return (7**-x)+3

a = -1
b = 2

r1 = f(a)*(b-a)
print("con regla del rectangulo: ",r1)

r1 = ((b-a)/2)*(f(a) + f(b))
print("Regla de trapecio: ",r1)