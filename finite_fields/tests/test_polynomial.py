import unittest
from finite_fields import RootGaloisField, Polynomial


class TestPolinomial(unittest.TestCase):
    def test_degree(self):
        gf = RootGaloisField(5)
        p = Polynomial([gf.zero, gf.one, gf.one])
        self.assertEqual(p.degree, 2)
        self.assertEqual(len(p), 3)

    def test_degree_zero_max_coefficient(self):
        gf = RootGaloisField(5)
        p = Polynomial([gf.zero, gf.one, gf.zero])
        self.assertEqual(p.degree, 1)

    def test_empty_polynomial(self):
        p1 = Polynomial([])
        with self.assertRaises(TypeError):
            p2 = Polynomial()

    def test_addition(self):
        gf = RootGaloisField(5)
        p1 = Polynomial([gf[1], gf[1], gf[1]])
        p2 = Polynomial([gf[4], gf[1], gf[2]])
        expected = Polynomial([gf[0], gf[2], gf[3]])
        self.assertEqual(p1 + p2, expected)
    
    def test_different_length_addition(self):
        gf = RootGaloisField(5)
        p1 = Polynomial([gf[3], gf[2]])
        p2 = Polynomial([gf[2], gf[4], gf[1]])
        expected = Polynomial([gf[0], gf[1], gf[1]])
        self.assertEqual(p1 + p2, expected)

    def test_substraction(self):
        gf = RootGaloisField(5)
        p1 = Polynomial([gf[1], gf[1], gf[1]])
        p2 = Polynomial([gf[4], gf[1], gf[2]])
        expected = Polynomial([gf[2], gf[0], gf[4]])
        self.assertEqual(p1 - p2, expected)

    def test_substraction_null_result(self):
        gf = RootGaloisField(5)
        p1 = Polynomial([gf[1], gf[1], gf[1]])
        self.assertEqual(p1 - p1, Polynomial([]))

    def test_multiplication(self):
        gf = RootGaloisField(5)
        p1 = Polynomial([gf[2], gf[1], gf[3], gf[4]])
        p2 = Polynomial([gf[2], gf[0], gf[3]])
        expected = Polynomial([gf[4], gf[2], gf[2], gf[1], gf[4], gf[2]])
        self.assertEqual(p1 * p2, expected)

    def test_null_multiplication(self):
        gf = RootGaloisField(5)
        p1 = Polynomial([gf[2], gf[1], gf[3], gf[4]])
        p2 = Polynomial([])
        self.assertEqual(p1 * p2, p2)
    
    def test_one_multiplication(self):
        gf = RootGaloisField(5)
        p1 = Polynomial([gf[2], gf[1], gf[3], gf[4]])
        p2 = Polynomial([gf.one])
        self.assertEqual(p1 * p2, p1)
    
    def test_division(self):
        gf = RootGaloisField(5)
        p1 = Polynomial([gf[2], gf[3], gf[4], gf[0], gf[1]])
        p2 = Polynomial([gf[3], gf[1]])
        expected = Polynomial([gf[4], gf[3], gf[2], gf[1]])
        self.assertEqual(p1 / p2, expected)
    
    def test_remainder(self):
        gf = RootGaloisField(5)
        p1 = Polynomial([gf[2], gf[3], gf[4], gf[0], gf[1]])
        p2 = Polynomial([gf[3], gf[1]])
        expected = Polynomial([])
        self.assertEqual(p1 % p2, expected)
