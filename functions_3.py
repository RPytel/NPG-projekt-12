import numpy as np
from functions import RealNumber
from typing import List

class Matrix(RealNumber):

    def __init__(self, x, op: str, y):
        """konstruktor macierzy"""
        super().__init__(np.array(x), op, np.array(y))

    def __matmul__(self): #metoda mnożenia macierzowego
        return self.x @ self.y

    def input(self):
        lst: List[List[int]] = []
        n = int(input("Podaj liczbę wierszy macierzy: "))
        if n <= 0:
            raise Exception("Nieprawidłowy rozmiar macierzy")
        for i in range(n):
            lst1: List[int] = []
            for j in range(n):
                x = int(input("Podaj wartość elementu a{}{}: ".format(i+1, j+1)))
                lst1.append(x)
            lst.append(lst1)
        z = np.array(lst)
        return z
