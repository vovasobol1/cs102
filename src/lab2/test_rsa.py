import unittest
from rsa import is_prime, gcd , multiplicative_inverse
class TestFunctions(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(8))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(10))

    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(6, 3), 3)
        self.assertEqual(gcd(40, 80), 40)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)



if __name__ == '__main__':
    unittest.main()