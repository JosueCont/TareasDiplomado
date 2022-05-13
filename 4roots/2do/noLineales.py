#MEtodo de falsa posicion

from math import exp

def f(x):
    return exp(2-x)-7*x

#primer intervalo
intervalo = (1,2)

#valores de f con el intervalo
x0 = f(intervalo[0])
x1 = f(intervalo[1])
c1 = (((x1*intervalo[0])-(x0*intervalo[1]))  / (x1-x0))

#print(c1)

#valores en f(c1)
x2 = f(c1)

#nuevo intervalo
int2 = (c1,2)

c2 = (((x1*int2[0])-(x2*int2[1]))  / (x1-x2))

#f(c2)
x3 = f(c2)


#nuevo intervalo 3
int3 = (c2,2)
c3 = (((x1*int3[0])-(x3*int3[1]))  / (x1-x3))
#f(c3)
x4 = f(c3)


#nuevo intervalo 4
int4 = (c3,2)
c4 = (((x1*int4[0])-(x4*int3[1]))  / (x1-x4))
#f(c4)
x5 = f(c4)

#nintervalo 5
int5 =(c4,2)
c5 = (((x1*int5[0])-(x5*int5[1]))  / (x1-x5))

print('la raiz es',c5)


