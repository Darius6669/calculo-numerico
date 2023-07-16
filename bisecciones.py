from math import *

def f(x):
    return sin(x) - e**-x
    
def bisecciones(a,b,er):#funcion donde realizo  los calculos
    m1 = a
    m = b
    k = 0
    indice = 0
    ea = 0# esta es la que uso para sacar el error
    if(f(a) * f(b) >0):#evaluo si la funcion cambia de signo
        print("La funcion no cambia de signo")
        
    aux = a
    while(abs(m1-m)> er):#ciclo donde itero
        m1 = m
        m = (a+b)/2
        if(f(a)*f(m) < 0):
            b = m
            
        if(f(b)*f(m) < 0):
            a = m
            
        if(indice > 1):#condion para calcular el error
            ea = ((b-a)/b)
        indice = indice +1
    print("El error relativo calculado :",ea)    
    print("El resultado aproximado:",m)
    return ea


solucion = bisecciones(0,1,0.02)


