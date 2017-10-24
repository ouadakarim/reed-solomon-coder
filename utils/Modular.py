from utils.ModularArithmetics import ModularArithmetics


class Modular:
    def __init__(self, value, modulus):
        self.value = value % modulus
        self.modulus = modulus

    def __add__(self, other):
        if isinstance(other, self.__class__):
            if self.modulus != other.modulus:
                raise ValueError('Numbers with different modules cannot be added')
            val = ModularArithmetics.add(self.value, other.value, self.modulus)
            return Modular(val, self.modulus)
        else:
            val = ModularArithmetics.add(self.value, other, self.modulus)
            return Modular(val, self.modulus)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            if self.modulus != other.modulus:
                raise ValueError('Numbers with different modules cannot be added')
            val = ModularArithmetics.multiply(self.value, other.value, self.modulus)
            return Modular(val, self.modulus)
        else:
            val = ModularArithmetics.multiply(self.value, other, self.modulus)
            return Modular(val, self.modulus)

    def modular_inverse(self):
        val = ModularArithmetics.modular_inverse(self.value, self.modulus)
        return Modular(val, self.modulus)
