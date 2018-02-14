import unittest
from Modular.Modular import Modular
# For console to work
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class ModularClass(unittest.TestCase):
    def setUp(self):
        pass

    # Adding
    def test_adding_modulars(self):
        a = Modular(4, 5)
        b = Modular(7, 5)
        self.assertEqual((a + b).value, 1)

    def test_adding_modulars_with_different_modulus(self):
        a = Modular(4, 5)
        b = Modular(7, 3)
        with self.assertRaises(Exception) as context:
            a + b
        self.assertTrue('Numbers with different modules cannot be added' in str(context.exception))

    def test_adding_modular_and_number(self):
        a = Modular(5, 4)
        b = 6
        self.assertEqual((a + b).value, 3)

    # Multiplying
    def test_multiplying_modulars(self):
        a = Modular(4, 5)
        b = Modular(7, 5)
        self.assertEqual((a * b).value, 3)

    def test_multiplying_modulars_with_different_modulus(self):
        a = Modular(4, 5)
        b = Modular(7, 3)
        with self.assertRaises(Exception) as context:
            a * b
        self.assertTrue('Numbers with different modules cannot be added' in str(context.exception))

    def test_multiplying_modular_and_number(self):
        a = Modular(10, 13)
        b = 3
        self.assertEqual((a * b).value, 4)


if __name__ == '__main__':
    unittest.main()

