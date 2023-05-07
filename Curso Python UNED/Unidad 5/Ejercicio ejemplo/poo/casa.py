from edificio import Edificio

class casa(Edificio):
    Edificio._pisos = 2

    def calcularImpuestos(self, areaPiso):
        Edificio.areaDePiso = areaPiso
        areaTotal = Edificio._calcularAreaTotal()

        if (areaTotal < 200):
            return 0
        else:
            return 0.0012 * areaTotal

