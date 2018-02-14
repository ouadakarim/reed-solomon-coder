import unittest
from Modular.ModularArithmetics import ModularArithmetics
# For console to work
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class GreatestCommonDivisor(unittest.TestCase):
    def setUp(self):
        pass

    def test_gcd_of_3_12(self):
        self.assertEqual(ModularArithmetics.gcd(3, 12), 3)

    def test_gcd_of_16_20(self):
        self.assertEqual(ModularArithmetics.gcd(16, 20), 4)


if __name__ == '__main__':
    unittest.main()

