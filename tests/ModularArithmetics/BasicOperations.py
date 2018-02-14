import unittest
from Modular.ModularArithmetics import ModularArithmetics
# For console to work
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class BasicOperations(unittest.TestCase):
    def setUp(self):
        pass

    def test_adding_numbers_3_4_mod11(self):
        self.assertEqual(ModularArithmetics.add(3, 4, 11), 7)

    def test_adding_numbers_5_4_mod7(self):
        self.assertEqual(ModularArithmetics.add(5, 4, 7), 2)

    def test_multiplying_numbers_6_5_mod8(self):
        self.assertEqual(ModularArithmetics.multiply(6, 5, 8), 6)

    def test_multiplying_numbers_8_3_mod3(self):
        self.assertEqual(ModularArithmetics.multiply(8, 3, 3), 0)


if __name__ == '__main__':
    unittest.main()

