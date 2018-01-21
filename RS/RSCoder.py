from GF.GaloisFieldArithmetics import GaloisFieldArithmetics


class RSCoder(object):
    """
    Reed-Solomon Encoder/Decoder class
    """
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

    def encode(self, msg_in, nsym):
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
        it's essentially equivalent to a Fourier Transform
        (Chien search being the inverse).
        """
        synd = [0] * nsym
        for i in range(0, nsym):
            synd[i] = self.GF.polynomial_evaluate(msg, self.GF.power(2, i))
        return [0] + synd

    def check_message(self, msg, nsym):
        """
        Returns true if the message + ecc has no error of false otherwise
        (may not always catch a wrong decoding or a wrong message, particularly
        if there are too many errors -- above the Singleton bound --, but it usually does)
        """
        return max(self.calculate_syndromes(msg, nsym)) == 0

    def find_errata_locator(self, e_pos):
        """
        Compute the erasures/errors/errata locator polynomial from the
        erasures/errors/errata positions (the positions must be relative to
        the x coefficient, eg: "hello worldxxxxxxxxx" is tampered to
        "h_ll_ worldxxxxxxxxx" with xxxxxxxxx being the ecc of length n-k=9,
        here the string positions are [1, 4], but the coefficients are reversed
        since the ecc characters are placed as the first coefficients of the
        polynomial, thus the coefficients of the erased characters are
        n-1 - [1, 4] = [18, 15] = erasures_loc to be specified as an argument.
        """

        e_loc = [1]
        for i in e_pos:
            e_loc = self.GF.polynomial_multiply(e_loc, self.GF.polynomial_add([1], [
                self.GF.power(2, i), 0]))
        return e_loc

    def find_error_evaluator(self, synd, err_loc, nsym):
        """
        Compute the error (or erasures if you supply sigma=erasures locator
        polynomial, or errata) evaluator polynomial Omega from the syndrome
        and the error/erasures/errata locator Sigma.
        """
        _, remainder = self.GF.polynomial_divide(self.GF.polynomial_multiply(synd, err_loc),
                                                 ([1] + [0] * (nsym + 1)))
        return remainder

    def correct_errata(self, msg_in, synd, err_pos):
        """
        Forney algorithm, computes the values (error magnitude) to correct the
        input message.
        """
        coef_pos = [len(msg_in) - 1 - p for p in err_pos]
        err_loc = self.find_errata_locator(coef_pos)
        err_eval = self.find_error_evaluator(synd[::-1], err_loc,
                                             len(err_loc) - 1)[::-1]

        X = []  # will store the position of the errors
        for i in range(0, len(coef_pos)):
            l = 255 - coef_pos[i]
            X.append(self.GF.power(2, -l))

        # Forney algorithm: compute the magnitudes
        E = [0] * (
            len(msg_in))  # will store the values that need to be corrected
        Xlength = len(X)
        for i, Xi in enumerate(X):
            Xi_inv = self.GF.inverse(Xi)
            err_loc_prime_tmp = []
            for j in range(0, Xlength):
                if j != i:
                    err_loc_prime_tmp.append(
                        self.GF.subtract(1, self.GF.multiply(Xi_inv, X[j])))
            err_loc_prime = 1
            for coef in err_loc_prime_tmp:
                err_loc_prime = self.GF.multiply(err_loc_prime, coef)

            y = self.GF.polynomial_evaluate(err_eval[::-1], Xi_inv)
            y = self.GF.multiply(self.GF.power(Xi, 1), y)

            # Compute the magnitude
            magnitude = self.GF.divide(y, err_loc_prime)
            E[err_pos[i]] = magnitude
        msg_in = self.GF.polynomial_add(msg_in, E)
        return msg_in

    def find_error_locator(self, synd, nsym, erase_loc=None, erase_count=0):
        """
        Find error/errata locator and evaluator polynomials with Berlekamp-Massey algorithm
        """
        if erase_loc:
            err_loc = list(erase_loc)
            old_loc = list(erase_loc)
        else:
            err_loc = [1]
            old_loc = [1]

        synd_shift = 0
        if len(synd) > nsym: synd_shift = len(synd) - nsym

        for i in range(0, nsym - erase_count):
            if erase_loc:
                K = erase_count + i + synd_shift
            else:
                K = i + synd_shift

            delta = synd[K]
            for j in range(1, len(err_loc)):
                delta ^= self.GF.multiply(err_loc[-(j + 1)], synd[K - j])

            old_loc = old_loc + [0]

            if delta != 0:
                if len(old_loc) > len(err_loc):
                    new_loc = self.GF.polynomial_scale(old_loc, delta)
                    old_loc = self.GF.polynomial_scale(err_loc,
                                                       self.GF.inverse(delta))
                    err_loc = new_loc

                err_loc = self.GF.polynomial_add(err_loc,
                                                 self.GF.polynomial_scale(old_loc,
                                                                       delta))

        # Check if the result is correct, that there's not too many errors to correct
        while len(err_loc) and err_loc[0] == 0:
            del err_loc[0]
        errs = len(err_loc) - 1
        # if (errs - erase_count) * 2 + erase_count > nsym:
        #     raise ReedSolomonError("Too many errors to correct")

        return err_loc

    def find_errors(self, err_loc, nmess):  # nmess is len(msg_in)
        """
        Find the roots (ie, where evaluation = zero) of error polynomial
        by brute-force trial, this is a sort of Chien's search (but less
        efficient, Chien's search is a way to evaluate the polynomial such
        that each evaluation only takes constant time).
        """
        errs = len(err_loc) - 1
        err_pos = []
        for i in range(nmess):
            if self.GF.polynomial_evaluate(err_loc, self.GF.power(2, i)) == 0:
                err_pos.append(nmess - 1 - i)
        # if len(err_pos) != errs:
            # couldn't find error locations
            # raise ReedSolomonError("Too many (or few) errors found by Chien \
            #                         Search for the errata locator polynomial!")
        return err_pos

    def forney_syndromes(self, synd, pos, nmess):
        erase_pos_reversed = [nmess - 1 - p for p in pos]
        fsynd = list(synd[1:])
        for i in range(0, len(pos)):
            x = self.GF.power(2, erase_pos_reversed[i])
            for j in range(0, len(fsynd) - 1):
                fsynd[j] = self.GF.multiply(fsynd[j], x) ^ fsynd[j + 1]
        return fsynd

    def decode(self, msg_in, nsym, erase_pos=None):
        """
        Reed-Solomon main decoding function
        """
        if len(msg_in) > 255:  # can't decode, message is too big
            raise ValueError(
                "Message is too long (%i when max is 255)" % len(msg_in))

        msg_out = list(msg_in)
        if erase_pos is None:
            erase_pos = []
        else:
            for e_pos in erase_pos:
                msg_out[e_pos] = 0
        # if len(erase_pos) > nsym: raise ReedSolomonError(
        #     "Too many erasures to correct")
        synd = self.calculate_syndromes(msg_out, nsym)
        if max(synd) == 0:
            return msg_out[:-nsym], msg_out[-nsym:]  # no errors

        fsynd = self.forney_syndromes(synd, erase_pos, len(msg_out))
        err_loc = self.find_error_locator(fsynd, nsym,
                                          erase_count=len(erase_pos))
        err_pos = self.find_errors(err_loc[::-1], len(msg_out))
        # if err_pos is None:
        #     raise ReedSolomonError("Could not locate error")

        msg_out = self.correct_errata(msg_out, synd, (
            erase_pos + err_pos))
        synd = self.calculate_syndromes(msg_out, nsym)
        # if max(synd) > 0:
        #     raise ReedSolomonError("Could not correct message")
        # return the successfully decoded message
        # also return the corrected ecc block so that the user can check()
        return msg_out[:-nsym], msg_out[-nsym:]


class ReedSolomonError(Exception):
    pass
