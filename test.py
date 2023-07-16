import unittest 
import bisecciones
import binomio_raphason
import ejercicio_riemman
import euler
from math import *
class test_biseccion(unittest.TestCase):# esta es la que se encarga del test de bisecciones

    def test_Biseccion(self):
        print("---------------------------TEST 1 aprobado--------------------------------------")
        self.assertEqual(bisecciones.bisecciones(0,1,0.02),0.02631578947368421)


class test_raphason(unittest.TestCase):# esta es la que se encarga del test de newthon raphson
    
    def test_raphason(self):
        print("---------------------------TEST 2 aprobado--------------------------------------")
        self.assertEqual(binomio_raphason.Newtonraphson(0.5,0.02,10),0.004903061084143822)


class test_riemann(unittest.TestCase):# esta es la que se encarga del test de la suma de riemman
    
    def test_riemann(self):
        print("---------------------------TEST 3 aprobado--------------------------------------")
        self.assertEqual(ejercicio_riemman.suma_riemman(0,1,5),0.43146135109221634)
        

class test_euler(unittest.TestCase):# esta es la que se encarga del test de la suma de riemman
    
    def test_euler(self):
        print("---------------------------TEST 4 aprobado--------------------------------------")
        self.assertEqual(euler.euler(2,1,4),2.55016300175339)
        
if(__name__=='__main__'):
    unittest.main()
