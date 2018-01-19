
class GaloisFieldBasicArithmetics(object):
    @staticmethod
    def add(x, y):
        return x ^ y

    @staticmethod
    def subtract(x, y):
        return x ^ y

    @staticmethod
    def multiply_carry_less(x, y):
        """
        Bitwise carry-less multiplication on integers
        """
        z = 0
        i = 0
        while (y >> i) > 0:
            if y & (1 << i):
                z ^= x << i
            i += 1
        return z

    @staticmethod
    def bit_length(n):
        """
        Compute the position of the most significant bit (1) of an integer. Equivalent to int.bit_length()
        """
        bits = 0
        while n >> bits: bits += 1
        return bits

    @staticmethod
    def divide_carry_less(dividend, divisor=None):
        """
        Bitwise carry-less long division on integers and returns the remainder
        """
        # Compute the position of the most significant bit for each integers
        dl1 = GaloisFieldBasicArithmetics.bit_length(dividend)
        dl2 = GaloisFieldBasicArithmetics.bit_length(divisor)
        # If the dividend is smaller than the divisor, just exit
        if dl1 < dl2:
            return dividend
        for i in range(dl1 - dl2, -1, -1):
            if dividend & (1 << i + dl2 - 1):
                dividend ^= divisor << i
        return dividend

    @staticmethod
    def multiply_noLUT(x, y, prim=0):
        """
        Multiplication in Galois Fields without using a precomputed look-up table (and thus it's slower)
        by using the standard carry-less multiplication + modular reduction using an irreducible prime polynomial
        """
        result = GaloisFieldBasicArithmetics.multiply_carry_less(x, y)
        if prim > 0:
            result = GaloisFieldBasicArithmetics.divide_carry_less(result, prim)

        return result

