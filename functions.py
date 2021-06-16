import math
class RealNumber:
    __slots__ = ['x','y','op']
    def __init__(self,x,op: str,y ):

        self.x=x
        self.y=y
        self.op=op
    def __repr__(self): #metoda ktora wypisuje klase
        return f"{self.x} {self.op} {self.y}"

    def __add__(self): #metoda dodawania
        return self.x + self.y

    def __mul__(self): #metoda mnożenia
        return self.x*self.y

    def __sub__(self): #metoda odejmowania
        return self.x-self.y

    def __truediv__(self): #metoda dzielenia
        return self.x / self.y

    def __pow__(self): #metoda potęgowania
        return math.pow(self.x ,self.y)
        # power = 1
        # for x in range(self.y):
        #     power = power * self.x
        # return power

def root(x , y):
    return math.pow(x,1/y)