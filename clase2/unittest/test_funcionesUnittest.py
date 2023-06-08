#Christian Briceno Weiss
import unittest
import funciones

class TestFunciones(unittest.TestCase):
    
    def setUp(self):
        print('setUp')
        
    def tearDown(self):
        print('tearDown\n')
    
    def test_add(self):
        print("Comenzando suma")
        self.assertEqual(funciones.add(10,20),30)
        self.assertEqual(funciones.add(10,10),20)        
        self.assertEqual(funciones.add(10,2),12)
        self.assertEqual(funciones.add(10,22),32)
    
    def test_substract(self):
        print("Comenzando resta")
        self.assertEqual(funciones.substract(10,20),-10)
        self.assertEqual(funciones.substract(10,10),0)        
        self.assertEqual(funciones.substract(10,2),8)
        self.assertEqual(funciones.substract(10,-22),32)
    
    def test_multiply(self):
        print("Comenzando multiplicacion")
        self.assertEqual(funciones.multiply(10,2),20)
        self.assertEqual(funciones.multiply(10,10),100)        
        self.assertEqual(funciones.multiply(10,8),80)
        self.assertEqual(funciones.multiply(-10,-22),220)
    
    def test_divide(self):
        print("Comenzando division")
        self.assertEqual(funciones.divide(10,2),5)
        self.assertEqual(funciones.divide(10,10),1)        
        self.assertEqual(funciones.divide(10,8),1.25)
        self.assertEqual(funciones.divide(5,2),2.5)
        
        with self.assertRaises(ValueError):
            funciones.divide(10,0)

    def test_raised(self):
        print("Comenzando potencia")
        self.assertEqual(funciones.raised(5,2),25)
        self.assertEqual(funciones.raised(6,4),1296)        
        self.assertEqual(funciones.raised(0,0),1)
        self.assertEqual(funciones.raised(10,2),100)

#Correr la prueba en la carpeta correspondiente donde esten ambos archivos
#en Terminal usar> python -m unittest -v