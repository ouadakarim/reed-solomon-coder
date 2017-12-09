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
            x = GaloisFieldBasicArithmetics.gf_mult_noLUT(x, 2, prim)
        for i in range(255, 512):
            self.gf_exp[i] = self.gf_exp[i - 255]
        return [self.gf_log, self.gf_exp]

    @staticmethod
    def gf_add(x, y):
        return GaloisFieldBasicArithmetics.gf_add(x, y)

    @staticmethod
    def gf_sub(x, y):
        return GaloisFieldBasicArithmetics.gf_sub(x, y)

    @staticmethod
    def gf_mult_noLUT(x, y, prim=0, field_charac_full=256, carryless=True):
        return GaloisFieldBasicArithmetics.gf_mult_noLUT(x, y, prim,
                                                         field_charac_full,
                                                         carryless)

    def gf_mul(self, x, y):
        if x == 0 or y == 0:
            return 0
        return self.gf_exp[self.gf_log[x] + self.gf_log[y]]

    def gf_div(self, x, y):
        if y == 0:
            raise ZeroDivisionError()
        if x == 0:
            return 0
        return self.gf_exp[(self.gf_log[x] + 255 - self.gf_log[y]) % 255]

    def gf_pow(self, x, power):
        return self.gf_exp[(self.gf_log[x] * power) % 255]

    def gf_inverse(self, x):
        return self.gf_exp[
            255 - self.gf_log[x]]  # gf_inverse(x) == gf_div(1, x)

    def gf_poly_scale(self, p, x):
        r = [0] * len(p)
        for i in range(0, len(p)):
            r[i] = self.gf_mul(p[i], x)
        return r

    def gf_poly_add(self, p, q):
        r = [0] * max(len(p), len(q))
        for i in range(0, len(p)):
            r[i + len(r) - len(p)] = p[i]
        for i in range(0, len(q)):
            r[i + len(r) - len(q)] ^= q[i]
        return r

    def gf_poly_mul(self, p, q):
        """
        Multiply two polynomials, inside Galois Field
        """
        r = [0] * (len(p) + len(q) - 1)
        for j in range(0, len(q)):
            for i in range(0, len(p)):
                r[i + j] ^= self.gf_mul(p[i], q[j])
        return r

    def gf_poly_eval(self, poly, x):
        """
        Evaluates a polynomial in GF(2^p) given the value for x. This is based
        on Horner's scheme for maximum efficiency.
        """
        y = poly[0]
        for i in range(1, len(poly)):
            y = self.gf_mul(y, x) ^ poly[i]
        return y

    def gf_poly_div(self, dividend, divisor):
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
                        msg_out[i + j] ^= self.gf_mul(divisor[j], coef)
        separator = -(len(divisor) - 1)
        return msg_out[:separator], msg_out[separator:]
