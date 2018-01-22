from GF.GaloisFieldArithmetics import GaloisFieldArithmetics


class RSSimplifiedCoder(object):
    def __init__(self, nsym, prim=0x11d):
        self.GF = GaloisFieldArithmetics(prim)
        self.g = self.generate_generator_polynomial(nsym)

    def generate_generator_polynomial(self, nsym):
        """
        Generate an irreducible generator polynomial (necessary to encode a
        message into Reed-Solomon)
        """
        g = [1]
        for i in range(0, nsym):
            g = self.GF.polynomial_multiply(g, [1, self.GF.power(2, i)])
        return g

    def encode(self, msg_in, nsym):
        """
        Reed-Solomon main encoding function
        """
        gen = self.g #self.generate_generator_polynomial(nsym)
        _, remainder = self.GF.polynomial_divide(msg_in + [0] * (len(gen) - 1), gen)
        msg_out = msg_in + remainder
        return msg_out

    # TODO check if correct
    def calculate_simple(self, msg, nsym):
        """
        Simple syndrome calculation
        with dividing with generator
        for n=255 and k = 243
        x12+68x11+119x10+67x9+118x8+220x7+31x6+7x5+84x4+92x3+127x2+213x+97
        """
        g = self.g #generate_generator_polynomial(nsym)
        _, remainder = self.GF.polynomial_divide(msg, g)
        return remainder

    def cyclic_move_right(self, msg, i):
        return msg[i:] + msg[:i]

    def decode(self, msg_in, nsym):
        for i in range(0, len(msg_in)):
            synd = self.calculate_simple(msg_in, nsym)

            weight = sum([1 if s != 0 else 0 for s in synd])
            if weight <= (nsym+1)/2:
                corrected_message = self.GF.polynomial_add(msg_in, synd)
                msg_out = self.cyclic_move_right(corrected_message, -i)
                return msg_out[:-nsym], msg_out[-nsym:]
            msg_in = self.cyclic_move_right(msg_in, 1)
        return [], []


class ReedSolomonError(Exception):
    pass
