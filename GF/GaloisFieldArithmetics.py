from GF.GaloisFieldBasicArithmetics import GaloisFieldBasicArithmetics


class GaloisFieldArithmetics(object):
    gf_exp = [0] * 512
    gf_log = [0] * 256

    def __init__(self, prim=0x11d):
        self.init_tables(prim)

    def init_tables(self, prim=0x11d):
        """
        Precompute the logarithm and anti-log tables for faster computation
        later, using the provided primitive polynomial.
        """
        self.gf_exp = [0] * 512  # anti-log (exponential) table
        self.gf_log = [0] * 256  # log table
        x = 1
        for i in range(0, 255):
            self.gf_exp[i] = x
            self.gf_log[x] = i
            x = GaloisFieldBasicArithmetics.multiply_noLUT(x, 2, prim)
        for i in range(255, 512):
            self.gf_exp[i] = self.gf_exp[i - 255]
        return [self.gf_log, self.gf_exp]

    @staticmethod
    def add(x, y):
        return GaloisFieldBasicArithmetics.add(x, y)

    @staticmethod
    def subtract(x, y):
        return GaloisFieldBasicArithmetics.subtract(x, y)

    @staticmethod
    def multiply_noLUT(x, y, prim=0):
        return GaloisFieldBasicArithmetics.multiply_noLUT(x, y, prim)

    def multiply(self, x, y):
        if x == 0 or y == 0:
            return 0
        return self.gf_exp[self.gf_log[x] + self.gf_log[y]]

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError()
        if x == 0:
            return 0
        return self.gf_exp[(self.gf_log[x] + 255 - self.gf_log[y]) % 255]

    def power(self, x, power):
        return self.gf_exp[(self.gf_log[x] * power) % 255]

    def inverse(self, x):
        return self.gf_exp[
            255 - self.gf_log[x]]  # gf_inverse(x) == gf_div(1, x)

    def polynomial_scale(self, p, x):
        r = [0] * len(p)
        for i in range(0, len(p)):
            r[i] = self.multiply(p[i], x)
        return r

    def polynomial_add(self, p, q):
        r = [0] * max(len(p), len(q))
        for i in range(0, len(p)):
            r[i + len(r) - len(p)] = p[i]
        for i in range(0, len(q)):
            r[i + len(r) - len(q)] ^= q[i]
        return r

    def polynomial_multiply(self, p, q):
        """
        Multiply two polynomials, inside Galois Field
        """
        r = [0] * (len(p) + len(q) - 1)
        for j in range(0, len(q)):
            for i in range(0, len(p)):
                r[i + j] ^= self.multiply(p[i], q[j])
        return r

    def polynomial_evaluate(self, poly, x):
        """
        Evaluates a polynomial in GF(2^p) given the value for x. This is based
        on Horner's scheme for maximum efficiency.
        """
        y = poly[0]
        for i in range(1, len(poly)):
            y = self.multiply(y, x) ^ poly[i]
        return y

    def polynomial_divide(self, dividend, divisor):
        """
        Fast polynomial division by using Extended Synthetic Division and
        optimized for GF(2^p) computations (doesn't work with standard
        polynomials outside of this galois field, see the Wikipedia
        article for generic algorithm).
        """
        msg_out = list(dividend)
        for i in range(0, len(dividend) - (len(divisor) - 1)):
            coef = msg_out[i]
            if coef != 0:
                for j in range(1, len(divisor)):
                    if divisor[j] != 0:  # log(0) is undefined
                        msg_out[i + j] ^= self.multiply(divisor[j], coef)
        separator = -(len(divisor) - 1)
        return msg_out[:separator], msg_out[separator:]
