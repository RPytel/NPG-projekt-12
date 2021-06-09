import cmath
from functions import real_number
# napisana klasa real_numbers i kuba wzorujac sie na niej napisz complex_numbers


class ComplexNumber(real_number):

    def __init__(self, x, op: str = None, y = 0):

        super().__init__(complex(x), op, complex(y))

    def __abs__(self):
        return abs(self.x)

