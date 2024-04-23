#Aclaro que me quede todo el recreo pensando como hacerlo
#aca no se copia paaaaaaa 👌 
import unittest
def fibonacci(valor):

    resultado = 0
    resultado_pasado = 0
    resultado_mas_pasado = 0

    for i in range(valor + 1):

        resultado_pasado = resultado
        resultado = resultado_pasado + resultado_mas_pasado
        resultado_mas_pasado = resultado_pasado

        if i==1:
            resultado = 1

    return resultado

# -----poner un valor para probar-----
# resultado = fibonacci(*valor*)
# print(resultado)

class Testfibonacci(unittest.TestCase):

    def test_0(self):
        resultado = fibonacci(0)
        self.assertEqual(resultado, 0)

    def test_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado, 1)

    def test_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado, 1)

    def test_5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado, 5)

    def test_10(self):
        resultado = fibonacci(10)
        self.assertEqual(resultado, 55)

    def test_13(self):
        resultado = fibonacci(13)
        self.assertEqual(resultado, 233)

unittest.main()