import unittest
from RS.RSCoder import RSCoder
# For console to work
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class ReedSolomonCoder(unittest.TestCase):
    def setUp(self):
        pass

    def test1_corrupted_message_with_6_errors_and_3_known_locations(self):
        prim = 0x11d
        n = 20  # set the size you want, it must be > k, the remaining n-k symbols will be the ECC code (more is better)
        k = 11  # k = len(message)
        input_msg = "hello world"

        rs = RSCoder(prim)

        mesecc = rs.encode_message([ord(x) for x in input_msg], n - k)

        # Tampering 6 characters of the message (over 9 ecc symbols, so we are above the Singleton Bound)
        mesecc[0] = 0
        mesecc[1] = 2
        mesecc[2] = 2
        mesecc[3] = 2
        mesecc[4] = 2
        mesecc[5] = 2
        print("Corrupted: %s" % mesecc)

        corrected_message, corrected_ecc = rs.correct_msg(mesecc, n - k,
                                                          erase_pos=[0, 1, 2])
        print("Repaired: %s" % (corrected_message + corrected_ecc))
        output_msg = ''.join([chr(x) for x in corrected_message])
        self.assertEqual(input_msg, output_msg)

    def test2_corrupted_message_with_4_errors_and_0_known_locations(self):
        prim = 0x11d
        n = 20
        k = 11
        input_msg = "hello world"

        rs = RSCoder(prim)

        mesecc = rs.encode_message([ord(x) for x in input_msg], n - k)
        # Tampering 6 characters of the message
        mesecc[0] = 0
        mesecc[1] = 2
        mesecc[2] = 2
        mesecc[3] = 2
        # Decoding/repairing the corrupted message, by providing the locations
        # of a few erasures, we get below the Singleton Bound
        # Remember that the Singleton Bound is: 2*e+v <= (n-k)
        corrected_message, corrected_ecc = rs.correct_msg(mesecc, n - k)
        output_msg = ''.join([chr(x) for x in corrected_message])
        self.assertEqual(input_msg, output_msg)

    def test3_corrupted_message_with_3_errors_and_0_known_locations(self):
        prim = 0x11d
        n = 20
        k = 11
        input_msg = "hello world"

        rs = RSCoder(prim)

        mesecc = rs.encode_message([ord(x) for x in input_msg], n - k)
        # Tampering 6 characters of the message
        mesecc[0] = 0
        mesecc[1] = 2
        mesecc[2] = 2

        # Decoding/repairing the corrupted message, by providing the locations
        # of a few erasures, we get below the Singleton Bound
        # Remember that the Singleton Bound is: 2*e+v <= (n-k)
        corrected_message, corrected_ecc = rs.correct_msg(mesecc, n - k)
        output_msg = ''.join([chr(x) for x in corrected_message])
        self.assertEqual(input_msg, output_msg)

    def test4_not_corrupted_message(self):
        prim = 0x11d
        n = 20
        k = 11
        input_msg = "hello world"

        rs = RSCoder(prim)

        mesecc = rs.encode_message([ord(x) for x in input_msg], n - k)

        corrected_message, corrected_ecc = rs.correct_msg(mesecc, n - k)
        output_msg = ''.join([chr(x) for x in corrected_message])
        self.assertEqual(input_msg, output_msg)


if __name__ == '__main__':
    unittest.main()
