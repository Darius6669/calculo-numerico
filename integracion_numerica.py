from math import *
from sympy import *
from scipy.integrate import quad
print("-------------------iteraciones de la suma de riemann ----------------------")
from ejercicio_riemman import return_solucion
print("-----------------------------------------")
resultado_suma_riemann  = return_solucion()# esta hace lo mismo pero llamando la funcion del archivo ejercicio_riemann

def f(x):#esta funcion es solo para retornar y evaluar los datos 
    return x * cos(x)

resultado = quad(f,0,1) #esta se encarga calcular la integral

def suma_trapecio(a,b,n):#funcion donde hago los calculos 
    h = (b-a)/n 
    suma = 0 # acumulador
    aux = a # aux que toma el valor del primer intervalo
    print("-------------------iteraciones del metodo del trapecio----------------------")
    for i in range(n):
        aux1 = aux
        aux += h
        print("A",i,":",(((f(aux1)+f(aux))*h)/2))# esta es para mostrar las iteraciones
        suma = suma + (((f(aux1)+f(aux))*h)/2)#acumula los resultados de las iteraciones para el total
    return suma;

a = 0
b = 1
n = 5

solucion = suma_trapecio(a,b,n) #variable la cual toma el valor de la funcion suma_trapecio
def return_resultad():
    global solucion
    return solucion
respuesta = return_resultad()

#aqui calculo los errores de suma de riemann y metodo del trapecio
error = ((0.3817732906760362 - solucion)/0.3817732906760362)
error_riemann = ((0.3817732906760362 - resultado_suma_riemann)/0.3817732906760362)

print("---------------------errores de trapecio--------------------")
print("la suma del trapecio es :",solucion)
print("la integral es :",resultado)
print("el error es :",error)


print("---------------------errores de suma riemann--------------------")
print("la suma de riemann es :",resultado_suma_riemann)
print("la integral es :",resultado)
print("el error es :",error_riemann)

solucion = suma_trapecio(a,b,n)

