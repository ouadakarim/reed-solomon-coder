import unittest
from RS.RSSimplifiedCoder import RSSimplifiedCoder
# For console to work
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class ReedSolomonCoder(unittest.TestCase):
    def setUp(self):
        pass

    def test_1_error_corrupted_message(self):
        prim = 0x11d
        n = 255
        k = 243
        input_msg = "helloworldhelloworldhelloworldhelloworldhelloworldhellowor" \
                    "ldhelloworldhelloworldhelloworldhelloworldhelloworldhellow" \
                    "orldhelloworldhelloworldhelloworldhelloworldhelloworldhell" \
                    "oworldhelloworldhelloworldhelloworldhelloworldhelloworldhe" \
                    "lloworld123"

        rs = RSSimplifiedCoder(prim)

        input_num = [ord(x) for x in input_msg]
        mesecc = rs.encode(input_num, n - k)
        mesecc[2] = 155

        corrected_message, corrected_ecc = rs.decode(mesecc, n - k)
        output_msg = ''.join([chr(x) for x in corrected_message])
        self.assertEqual(input_msg, output_msg)

    def test_5_error_corrupted_message(self):
        prim = 0x11d
        n = 255
        k = 243
        input_msg = "helloworldhelloworldhelloworldhelloworldhelloworldhellowor" \
                    "ldhelloworldhelloworldhelloworldhelloworldhelloworldhellow" \
                    "orldhelloworldhelloworldhelloworldhelloworldhelloworldhell" \
                    "oworldhelloworldhelloworldhelloworldhelloworldhelloworldhe" \
                    "lloworld123"

        rs = RSSimplifiedCoder(prim)

        input_num = [ord(x) for x in input_msg]
        mesecc = rs.encode(input_num, n - k)
        mesecc[2] = 155
        mesecc[3] = 155
        mesecc[4] = 155
        mesecc[5] = 155
        mesecc[6] = 155

        corrected_message, corrected_ecc = rs.decode(mesecc, n - k)
        output_msg = ''.join([chr(x) for x in corrected_message])
        self.assertEqual(input_msg, output_msg)

    def test_2_errors_with_big_distance_message(self):
        prim = 0x11d
        n = 255
        k = 243
        input_msg = "helloworldhelloworldhelloworldhelloworldhelloworldhellowor" \
                    "ldhelloworldhelloworldhelloworldhelloworldhelloworldhellow" \
                    "orldhelloworldhelloworldhelloworldhelloworldhelloworldhell" \
                    "oworldhelloworldhelloworldhelloworldhelloworldhelloworldhe" \
                    "lloworld123"

        rs = RSSimplifiedCoder(prim)

        input_num = [ord(x) for x in input_msg]
        mesecc = rs.encode(input_num, n - k)
        mesecc[2] = 155
        mesecc[15] = 155

        corrected_message, corrected_ecc = rs.decode(mesecc, n - k)
        output_msg = ''.join([chr(x) for x in corrected_message])
        self.assertNotEqual(input_msg, output_msg)


if __name__ == '__main__':
    unittest.main()
