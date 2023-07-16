from math import *

def f(x):#esta funcion es solo para retornar y evaluar los datos
    return x * cos(x)

def suma_riemman(a,b,n):# funcion donde hago los calculos 
    h = (b-a)/n
    suma = 0#acumulador
    aux = a
    for i in range(n):
        aux += h
        print("A",i,": ",(h * f(aux)))# esto es para mostrar las iteraciones
        suma = suma + (h * f(aux))
    return suma;

a = 0
b = 1
n = 5

solucion = suma_riemman(a,b,n)

def return_solucion():
    global solucion;
    return solucion


