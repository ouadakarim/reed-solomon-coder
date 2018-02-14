import unittest

from Modular.Modular import Modular
# For console to work
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class ModularInverse(unittest.TestCase):
    def setUp(self):
        pass

    def test_mod_inv_in_class_of_3_mod_7(self):
        a = Modular(3, 7)
        self.assertEqual(a.modular_inverse().value, 5)


if __name__ == '__main__':
    unittest.main()
