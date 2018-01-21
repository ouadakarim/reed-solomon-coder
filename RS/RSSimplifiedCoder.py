from GF.GaloisFieldArithmetics import GaloisFieldArithmetics


# TODO:
# Kilknanaście testów

class RSSimplifiedCoder(object):
    def __init__(self, prim=0x11d):
        self.GF = GaloisFieldArithmetics(prim)

    def generate_generator_polynomial(self, nsym):
        """
        Generate an irreducible generator polynomial (necessary to encode a
        message into Reed-Solomon)
        """
        g = [1]
        for i in range(0, nsym):
            g = self.GF.polynomial_multiply(g, [1, self.GF.power(2, i)])
        return g

    def encode_message(self, msg_in, nsym):
        """
        Reed-Solomon main encoding function
        """
        gen = self.generate_generator_polynomial(nsym)
        _, remainder = self.GF.polynomial_divide(msg_in + [0] * (len(gen) - 1), gen)
        msg_out = msg_in + remainder
        return msg_out

    def calculate_syndromes(self, msg, nsym):
        """
        Given the received codeword msg and the number of error correcting
        symbols (nsym), computes the syndromes polynomial. Mathematically,
        it's essentially equivalent to a Fourrier Transform
        (Chien search being the inverse).
        """
        synd = [0] * nsym
        for i in range(0, nsym):
            synd[i] = self.GF.polynomial_evaluate(msg, self.GF.power(2, i))
        return [0] + synd

    # TODO check if correct
    def calculate_simple(self, msg, nsym):
        """
        Given the received codeword msg and the number of error correcting
        symbols (nsym), computes the syndromes polynomial. Mathematically,
        it's essentially equivalent to a Fourrier Transform
        (Chien search being the inverse).
        """
        g = self.generate_generator_polynomial(nsym)
        _, remainder = self.GF.polynomial_divide(msg, g)
        return remainder

    def cyclic_move_right(self, msg, i):
        return msg[i:] + msg[:i]

    def simple_decode(self, msg_in, nsym):
        for i in range(0, len(msg_in)):
            synd1 = self.calculate_syndromes(msg_in, nsym)
            synd= self.calculate_simple(msg_in, nsym)
            weight = sum([1 if s != 0 else 0 for s in synd])
            if weight <= nsym:
                corrected_message = self.GF.polynomial_add(msg_in, synd) # + [0]*(len(msg_in) - nsym))
                msg_out = self.cyclic_move_right(corrected_message, -i)
                return msg_out, msg_out #msg_out[:-nsym], msg_out[-nsym:]
            msg_in = self.cyclic_move_right(msg_in, 1)


class ReedSolomonError(Exception):
    pass
