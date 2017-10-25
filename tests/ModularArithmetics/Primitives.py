import unittest
from utils.ModularArithmetics import ModularArithmetics
# For console to work
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class Primitives(unittest.TestCase):
    def setUp(self):
        pass

    def test1_primitives_of_11(self):
        self.assertEqual(ModularArithmetics.find_primitives(11), [2, 6, 7, 8])

    def test2_primitives_of_17(self):
        self.assertEqual(ModularArithmetics.find_primitives(17), [
            3, 5, 6, 7, 10, 11, 12, 14])

    def test3_primitives_of_71(self):
        self.assertEqual(ModularArithmetics.find_primitives(71), [
            7, 11, 13, 21, 22, 28, 31, 33, 35, 42, 44, 47, 52, 53, 55, 56, 59,
            61, 62, 63, 65, 67, 68, 69])

    def test4_primitives_of_1021(self):
        self.assertEqual(ModularArithmetics.find_primitives(1021), [
            10, 22, 30, 31, 34, 35, 37, 40, 43, 46, 50, 53, 59, 65, 66, 76, 77,
            82, 90, 93, 94, 95, 102, 103, 105, 109, 111, 119, 120, 122, 124,
            127, 129, 134, 137, 138, 140, 143, 150, 159, 160, 161, 166, 172,
            175, 177, 178, 184, 185, 195, 198, 209, 211, 212, 221, 228, 231,
            232, 236, 239, 241, 246, 260, 263, 266, 270, 279, 281, 282, 283,
            285, 287, 298, 299, 304, 306, 309, 313, 315, 325, 326, 327, 329,
            330, 333, 337, 352, 357, 358, 366, 372, 377, 380, 381, 385, 386,
            387, 388, 394, 398, 402, 410, 411, 419, 420, 427, 428, 429, 434,
            436, 440, 449, 450, 461, 466, 469, 473, 477, 480, 483, 485, 487,
            490, 494, 496, 498, 502, 505, 516, 519, 523, 525, 527, 531, 534,
            536, 538, 541, 544, 548, 552, 555, 560, 571, 572, 581, 585, 587,
            592, 593, 594, 601, 602, 610, 611, 619, 623, 627, 633, 634, 635,
            636, 640, 641, 644, 649, 655, 663, 664, 669, 684, 688, 691, 692,
            694, 695, 696, 706, 708, 712, 715, 717, 722, 723, 734, 736, 738,
            739, 740, 742, 751, 755, 758, 761, 775, 780, 782, 785, 789, 790,
            793, 800, 809, 810, 812, 823, 826, 836, 837, 843, 844, 846, 849,
            855, 860, 861, 862, 871, 878, 881, 883, 884, 887, 892, 894, 897,
            899, 901, 902, 910, 912, 916, 918, 919, 926, 927, 928, 931, 939,
            944, 945, 955, 956, 962, 968, 971, 975, 978, 981, 984, 986, 987,
            990, 991, 999, 1011])


if __name__ == '__main__':
    unittest.main()
