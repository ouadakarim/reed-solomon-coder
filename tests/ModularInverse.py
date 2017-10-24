import unittest
from utils.ModularArithmetics import ModularArithmetics
# For console to work
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class ModularInverse(unittest.TestCase):
    def setUp(self):
        pass

    def test_mod_inv_of_13_mod_17(self):
        self.assertEqual(ModularArithmetics.modular_inverse(13, 17), 4)

    def test_mod_inv_of_3_mod_7(self):
        self.assertEqual(ModularArithmetics.modular_inverse(3, 7), 5)

    def test_mod_inv_of_2_mod_8(self):
        # Modular inverse should not exist
        self.assertEqual(ModularArithmetics.modular_inverse(2, 8), None)


if __name__ == '__main__':
    unittest.main()
