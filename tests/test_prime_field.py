import unittest
from galois_field import PrimeFieldElement, PrimeField


class TestPrimeFieldElement(unittest.TestCase):
    
    def test_initialization(self):
        a = PrimeFieldElement(3, 5)
        self.assertEqual(a.value, 3)
        self.assertEqual(a.p, 5)
        
        b = PrimeFieldElement(8, 5)
        self.assertEqual(b.value, 3)
        
    def test_addition(self):
        a = PrimeFieldElement(3, 5)
        b = PrimeFieldElement(2, 5)
        c = a + b
        self.assertEqual(c.value, 0)
        
    def test_subtraction(self):
        a = PrimeFieldElement(3, 5)
        b = PrimeFieldElement(2, 5)
        c = a - b
        self.assertEqual(c.value, 1)
        
    def test_multiplication(self):
        a = PrimeFieldElement(3, 5)
        b = PrimeFieldElement(2, 5)
        c = a * b
        self.assertEqual(c.value, 1)
        
    def test_reciprocal(self):
        a = PrimeFieldElement(3, 5)
        b = a.reciprocal()
        self.assertEqual(b.value, 2)
        
    def test_power(self):
        a = PrimeFieldElement(3, 5)
        b = a ** 2
        self.assertEqual(b.value, 4)
        
        c = a ** -1
        self.assertEqual(c.value, 2)
        
    def test_equality(self):
        a = PrimeFieldElement(3, 5)
        b = PrimeFieldElement(3, 5)
        c = PrimeFieldElement(2, 5)
        
        self.assertTrue(a == b)
        self.assertFalse(a == c)

class TestPrimeField(unittest.TestCase):
    
    def test_initialization(self):
        F = PrimeField(5)
        self.assertEqual(F.p, 5)
        self.assertEqual(len(F.elements), 5)
        
    def test_apply_function(self):
        F = PrimeField(5)
        square = lambda x: x ** 2
        squares = F.apply(square, unique=True)
        squares_values = [x.value for x in squares]
        
        manual_squares = list(set([x.value ** 2 % F.p for x in F.elements]))
        self.assertEqual(sorted(squares_values), sorted(manual_squares))
        
    def test_multiplicative_elements(self):
        F = PrimeField(5)
        mult_elements = F.multiplicative()
        mult_values = [x.value for x in mult_elements]
        self.assertEqual(mult_values, [1, 2, 3, 4])
        
    def test_squares(self):
        F = PrimeField(5)
        squares = F.squares()
        squares_values = [x.value for x in squares]
        self.assertEqual(squares_values, [1, 4])