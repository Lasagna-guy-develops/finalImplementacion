import unittest
from MetodosMath import Rectangulo, Triangulo, Circulo, Fibonacci, Factorial

class Test(unittest.TestCase):

    def test_Rectangulo(self):
        self.assertEqual(Rectangulo.area(2, 4), 8)
        self.assertEqual(Rectangulo.perimetro(2, 4), 12)
        self.assertEqual(Rectangulo.area(0.00095, 0.03), 2.8499999999999998e-05)
        self.assertEqual(Rectangulo.perimetro(0.00095, 0.03), 0.0619)
        self.assertEqual(Rectangulo.area(90000000000, 87562111234), 7880590011060000000000)
        self.assertEqual(Rectangulo.perimetro(90000000000, 87562111234), 355124222468)

    def test_Circulo(self):
        self.assertEqual(round(Circulo.area(2), 2), 12.57)
        self.assertEqual(round(Circulo.perimetro(2), 2), 12.57)
        self.assertEqual(round(Circulo.area(0.00095), 2), 0.0)
        self.assertEqual(round(Circulo.perimetro(0.00095), 2), 0.01)
        self.assertEqual(round(Circulo.area(87562111234), 2), 2.4086978308076886e+22)
        self.assertEqual(round(Circulo.perimetro(87562111234), 2), 550168970771.09)

    def test_Triangulo(self):
        self.assertEqual(Triangulo.perimetro(2, 3, 2), 7)
        self.assertEqual(Triangulo.area(2, 3, 2), 1.984313483298443)
        self.assertEqual(Triangulo.perimetro(0.00095, 0.03, 0.00067), 0.031619999999999995)
        self.assertEqual(Triangulo.area(0.00095, 0.03, 0.00067), 1.375657534184561e-20+0.0002246619245879461j)
        self.assertEqual(Triangulo.perimetro(90000000000, 87562111234, 799999996732), 977562107966)
        self.assertEqual(Triangulo.area(90000000000, 87562111234, 799999996732), 9552763.421200978+1.5600846591608265e+23j)

    def test_Fibonacci(self):
        self.assertEqual(Fibonacci.fib(4), [1, 1, 2, 3, 5])
        self.assertEqual(Fibonacci.fib(1), [1])
        self.assertEqual(Fibonacci.fib(20), [1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946])


    def test_Factorial(self):
        self.assertEqual(Factorial.factorial(4), 24)
        self.assertEqual(Factorial.factorial(1), 1)
        self.assertEqual(Factorial.factorial(30), 265252859812191058636308480000000)

if __name__ == '__main__':
    unittest.main()