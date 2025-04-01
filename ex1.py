import math

class Circle:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio

    def area(self):

        return math.pi * self.raio ** 2
    def perimetro(self):
        
        return 2 * math.pi * self.raio
     
    def test_pertencente(self, ponto):
        
        x_ponto, y_ponto = ponto
        x_centro, y_centro = self.centro

        distancia = math.sqrt((x_ponto - x_centro) ** 2 + (y_ponto - y_centro) ** 2)
        return distancia <= self.raio