import unittest
from utils.ModularArithmetics import ModularArithmetics
# For console to work
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class ChineseRemainderTheorem(unittest.TestCase):
    def setUp(self):
        pass

    def test1_chinese_remainder_theorem(self):
        self.assertEqual(ModularArithmetics.chinese_remainder_theorem([3, 4, 1], [4, 5, 7]), 99)

    def test2_chinese_remainder_theorem(self):
        self.assertEqual(ModularArithmetics.chinese_remainder_theorem([2, 3, 2], [3, 5, 7]), 23)

    def test3_chinese_remainder_theorem(self):
        self.assertEqual(ModularArithmetics.chinese_remainder_theorem([2, 3], [3, 5, 7]), None)


if __name__ == '__main__':
    unittest.main()
