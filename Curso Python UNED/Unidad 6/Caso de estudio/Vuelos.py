class Vuelos:
    num_vuelo = ''
    ciudad_origen = ''
    ciudad_destino = ''
    compannia = ''
    tipo_aeronave = ''
    kilometraje = 0

    def __init__(self, paramNumVuelo, paramCiudadOrigen, paramCiudadDestino, paramCompannia, paramTipoAeronave,
                 paramKilometraje):
        self.num_vuelo = paramNumVuelo
        self.ciudad_origen = paramCiudadOrigen
        self.ciudad_destino = paramCiudadDestino
        self.compannia = paramCompannia
        self.tipo_aeronave = paramTipoAeronave
        self.kilometraje = paramKilometraje

    def descripcion(self):
        return f"{self.num_vuelo}, de {self.ciudad_origen} a {self.ciudad_destino}, con kilometraje: {self.kilometraje} de la compañía {self.compannia}, tipo es: {self.tipo_aeronave}, Costo : {self.calcular_costo_combustible()} Colones"

    def calcular_costo_combustible(self):
        litros_combustible = (self.kilometraje / 100) * 1200
        costo_combustible = litros_combustible * 326
        return costo_combustible
