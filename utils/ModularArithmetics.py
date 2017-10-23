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

        :param x: first number
        :param y: second number
        :return: Greatest common divisor
        """
        while y != 0:
            (x, y) = (y, x % y)
        return x

    @staticmethod
    def modular_inverse(x, y, p):
        """
        This method calculates the greatest common divisor of two numbers

        :param x: first number
        :param y: second number
        :return: Modular Inverse
        """


