import unittest
from finite_fields.root_galois_field import RootGaloisField


class TestRootGaloisField(unittest.TestCase):
    def test_cardinality(self):
        gf1 = RootGaloisField(5)
        self.assertEqual(gf1.cardinality, 5)
        gf2 = RootGaloisField(17)
        self.assertEqual(gf2.cardinality, 17)

    def test_random_element(self):
        gf = RootGaloisField(17)
        self.assertIn(gf.random(), gf)

    def test_equivalence_class(self):
        gf = RootGaloisField(5)
        self.assertIn(5, gf[0])
        self.assertIn(6, gf[1])
        
    def test_iterator(self):
        gf = RootGaloisField(5)
        for index, equivalence_class in enumerate(gf):
            self.assertIn(index, equivalence_class)

    def test_addition(self):
        gf = RootGaloisField(5)
        self.assertEqual(gf[3], gf.add(gf[1], gf[2]))
        self.assertEqual(gf[3], gf[1] + gf[2])

    def test_substraction(self):
        gf = RootGaloisField(5)
        self.assertEqual(gf[4], gf.substract(gf[1], gf[2]))
        self.assertEqual(gf[4], gf[1] - gf[2])

    def test_multiplication(self):
        gf = RootGaloisField(17)
        self.assertEqual(gf.multiply(gf[3], gf[2]), gf[6])
        self.assertEqual(gf.multiply(gf[10], gf[2]), gf[3])
        self.assertEqual(gf[3] * gf[2], gf[6])
        self.assertEqual(gf[10] * gf[2], gf[3])

    def test_division(self):
        gf = RootGaloisField(17)
        self.assertEqual(gf.divide(gf[6], gf[1]), gf[6])
        self.assertEqual(gf.divide(gf[10], gf[2]), gf[5])
        self.assertEqual(gf[6] / gf[1], gf[6])
        self.assertEqual(gf[10] // gf[2], gf[5])
        self.assertEqual(gf[6] // gf[1], gf[6])
        self.assertEqual(gf[10] / gf[2], gf[5])

    def test_inverse(self):
        gf = RootGaloisField(17)
        self.assertEqual(gf.inverse(gf[1]), gf[1])
        self.assertEqual(gf.inverse(gf[2]), gf[9])
        self.assertEqual(gf.inverse(gf[3]), gf[6])
        self.assertEqual(gf.inverse(gf[9]), gf[2])
        self.assertEqual(gf.inverse(gf[6]), gf[3])
        self.assertEqual(~gf[1], gf[1])
        self.assertEqual(~gf[2], gf[9])
        self.assertEqual(~gf[3], gf[6])
        self.assertEqual(~gf[9], gf[2])
        self.assertEqual(~gf[6], gf[3])

    def test_parameters(self):
        gf1 = RootGaloisField(5)
        self.assertEqual(gf1.p, 5)
        self.assertEqual(gf1.m, 1)
        gf2 = RootGaloisField(17)
        self.assertEqual(gf2.p, 17)
        self.assertEqual(gf2.m, 1)

    def test_zero(self):
        gf = RootGaloisField(13)
        self.assertIn(0, gf.zero)
        self.assertEqual(gf.zero.representative, 0)
        for element in gf:
            self.assertEqual(element + gf.zero, element)

    def test_one(self):
        gf = RootGaloisField(13)
        self.assertIn(1, gf.one)
        for element in gf:
            if element != gf.zero:
                self.assertEqual(element * gf.one, element)
            else:
                self.assertEqual(element * gf.one, gf.zero)

    def test_prime_checking(self):
        with self.assertRaises(ValueError):
            gf = RootGaloisField(6)
