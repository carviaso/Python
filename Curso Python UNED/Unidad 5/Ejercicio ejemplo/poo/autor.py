class Autor:
    nombre = ''
    nacionalidad = ''

    def __init__(self, paramNombre, paramNacionalidad):
        self.nombre = paramNombre
        self.nacionalidad = paramNacionalidad

    def descripcion(self):
        return (self.nombre, " ",self.nacionalidad)


