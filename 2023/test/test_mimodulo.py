import sys
import os

# Añadir el directorio padre al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from reto21_numeros_primos_gemelos import is_primo, primos

import unittest

class TestFuncionesPrimo(unittest.TestCase):

    def test_is_primo(self):
        # Pruebas para números primos
        self.assertTrue(is_primo(2))
        self.assertTrue(is_primo(3))
        self.assertTrue(is_primo(5))
        self.assertTrue(is_primo(7))
        self.assertTrue(is_primo(11))
        
        # Pruebas para números no primos
        self.assertFalse(is_primo(4))
        self.assertFalse(is_primo(6))
        self.assertFalse(is_primo(8))
        self.assertFalse(is_primo(9))
        self.assertFalse(is_primo(10))
    
    def test_primos(self):
        # Pruebas para la función primos
        self.assertEqual(primos(14), [(3, 5), (5, 7), (11, 13), (17, 19)])
        self.assertEqual(primos(20), [(3, 5), (5, 7), (11, 13), (17, 19)])
        
        # Prueba para el rango menor a 5
        with self.assertRaises(ValueError):
            primos(4)

if __name__ == "__main__":
    unittest.main()