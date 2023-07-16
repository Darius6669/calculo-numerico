from math import *

def f(x):
    F = sin(x) - e**-x
    return F

def df(x):
    return cos(x) + e**-x


def Newtonraphson(x0,Er,n):
    ea = 0
    for i in range(n):
        x1 = x0-f(x0)/df(x0)
        if(abs(x1-x0)  < Er):
            ea = ((x1 - x0)/x1)
            print('x',i+1,'=',x1,'es la raiz',' error relativo',ea)
            return ea
        x0 = x1
        print('x',i+1,'=',x1)

solucion = Newtonraphson(0.5,0.02,10)
print(solucion);
