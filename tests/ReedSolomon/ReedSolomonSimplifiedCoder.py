import unittest
from RS.RSSimplifiedCoder import RSSimplifiedCoder
# For console to work
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class ReedSolomonCoder(unittest.TestCase):
    def setUp(self):
        pass

    def test_not_corrupted_message(self):
        prim = 0x11d
        n = 20
        k = 11
        input_msg = "hello world"

        rs = RSSimplifiedCoder(prim)

        mesecc = rs.encode_message([ord(x) for x in input_msg], n - k)
        mesecc[2] = 155

        corrected_message, corrected_ecc = rs.simple_decode(mesecc, n - k)
        output_msg = ''.join([chr(x) for x in corrected_message])
        self.assertEqual(input_msg, output_msg[:-n+k])


if __name__ == '__main__':
    unittest.main()
