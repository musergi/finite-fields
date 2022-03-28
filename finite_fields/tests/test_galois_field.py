import unittest
from finite_fields.galois_field import RootGaloisField

class TestRootGaloisField(unittest.TestCase):
    def test_cardinality(self):
        gf1 = RootGaloisField(5)
        gf2 = RootGaloisField(17)
        self.assertEqual(gf1.cardinality, 5)
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
