class aeropuerto:
    nombre = ''
    localidad = ''

    def __init__(self, paramNombre, paramLocalidad):
        self.nombre = paramNombre
        self.localidad = paramLocalidad

    def descripcion(self):
        return (self.nombre, " ",self.localidad)