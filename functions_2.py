import cmath
from functions import RealNumber


class ComplexNumber(RealNumber):

    def __init__(self, x, op: str = None, y = 0):
        """konstruktor liczby zespolonej"""
        super().__init__(complex(x), op, complex(y))

    def __abs__(self):
        """metoda obliczania modułu"""
        return abs(self.x)

    def atan(self):
        """metoda obliczania argumentu głownego"""
        return cmath.phase(self.x)
