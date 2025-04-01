import math

class Circle:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio

    def area(self):
        """
        Calcula a área do círculo.
        """
        return math.pi * self.raio ** 2
