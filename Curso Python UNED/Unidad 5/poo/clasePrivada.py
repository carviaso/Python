class ClasePrivada :
    __nombre = ""

    def __mostrar(self):
        print('Metodo privado, el valor de nombre es ',self.__nombre)

    #Permite desde el exterior, poner un valor a un atributo privado
    def setNombre (self, valorNombre):
        self.__nombre = valorNombre

    # Permite desde el exterior, obtener el valor de un atributo privado
    def getNombre(self):
        return self.__nombre

