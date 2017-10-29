import math


class ModularArithmetics(object):

    @staticmethod
    def add(x, y, p):
        """
        This method adds two numbers using modular arithmetics

        :param x: first number
        :param y: second number
        :param p: modulus
        :return: Sum of two modular numbers
        """
        return (x + y) % p

    @staticmethod
    def multiply(x, y, p):
        """
        This method multiplies two numbers using modular arithmetics

        :param x: first number
        :param y: second number
        :param p: modulus
        :return: Product of two modular numbers
        """
        return (x * y) % p

    @staticmethod
    def gcd(x, y):
        """
        This method calculates the greatest common divisor of two numbers
        Euclidean Algorythm

        :param x: first number
        :param y: second number
        :return: Greatest common divisor
        """
        while y != 0:
            (x, y) = (y, x % y)
        return x

    @staticmethod
    def extended_gcd(x, y):
        """
        This method calculates the greatest common divisor of two numbers
        Extended Euclidean Algorythm

        The result is following: ax + by = 1

        :param x: first number
        :param y: second number
        :return x: Greatest common divisor
        :return x0: Coefficient of x (a)
        :return y0: Coefficient of y (b)
        """
        x0, x1, y0, y1 = 1, 0, 0, 1
        while y != 0:
            (q, x, y) = (x // y, y, x % y)  # // is integer division
            (x0, x1) = (x1, x0 - q * x1)
            (y0, y1) = (y1, y0 - q * y1)
        return x, x0, y0

    @staticmethod
    def modular_inverse(x, p):
        """
        This method calculates the greatest common divisor of two numbers

        :param x: first number
        :param p: modular base
        :return: Modular Inverse
        """
        g, a, _ = ModularArithmetics.extended_gcd(x, p)
        if g == 1:
            return a % p
        else:
            print("Modular inverse does not exist for {0} mod {1}".format(x, p))
            return None

    @staticmethod
    def primitives(p):
        """
        This method gets the primitives for a certain modulus

        :param p: modular base
        :return: primitives
        """
        primitives = []
        for i in range(1, p):
            for j in range(1, p):
                val = pow(i, j) % p
                if val == 1:
                    if j != p - 1:
                        break
                    else:
                        primitives.append(i)
        return primitives







