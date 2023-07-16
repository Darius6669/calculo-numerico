from math import *

def f(t,y):
    func = (t-y)**2 + 1
    return func


def euler(t,y,n):
    print('y(',t,')=',y)
    h = (t-y)/n
    print('valor de H:',h)
    print("i  ", "  Ti", "      Yi", "            Yi+1")
    for k in range(n):
        y = y+h*f(t,y)
        t = t+h
        print(k,')','(',t,')','(',y,')',    '   (',    y+h*f(t,y),')')
    return y


        
solucion=euler(2,1,4)
print(solucion)
