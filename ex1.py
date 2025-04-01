import math

class Circle:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio

    def area(self):

        return math.pi * self.raio ** 2
    def perimetro(self):
        
        return 2 * math.pi * self.raio