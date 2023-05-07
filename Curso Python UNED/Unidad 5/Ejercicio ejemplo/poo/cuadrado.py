from figuraAbstracta import FiguraAbstracta

class Cuadrado(FiguraAbstracta):
    lado = 0

    def calcularArea(self):
        return self.lado * self.lado

    def calcularPerimetro(self):
        return 4 * self.lado

