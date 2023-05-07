# Importar librería para validar correo electrónico
import re

# Definir función de validación de nombre
'''
def validar_nombre(nombre):
    if len(nombre) < 9:
        print("El nombre debe tener al menos 9 letras.")
        return False
    return True
'''
validar_nombre = lambda nombre: True if len(nombre) > 9 else False

# Definir función de validación de correo electrónico
'''
def validar_correo(correo):
    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(patron_correo, correo):
        print("El correo electrónico no tiene el formato correcto.")
        return False
    return True
'''
validar_correo = lambda correo: True if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo) else False


# Definir función de validación de año de nacimiento
def validar_anio_nacimiento(anio):
    edad = 2023 - int(anio)
    if edad < 18:
        print("La persona debe ser mayor de edad.")
        return False
    return True


# Definir función de validación de provincia
def validar_provincia(provincia):
    provincias = ["San Jose", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limon"]
    if provincia not in provincias:
        print("Debe ingresar una provincia válida de Costa Rica.")
        print(provincias)
        return False
    return True


# Definir función de validación de número de teléfono
def validar_telefono(telefono):
    if len(telefono) != 8 or telefono[0] not in ["2", "4", "6", "7", "8"]:
        print("El número de teléfono debe tener 8 dígitos y comenzar con 2, 4, 6, 7 u 8.")
        return False
    return True


# Definir función principal para solicitar datos y validarlos
def ingresar_datos():
    nombre = input("Ingrese su nombre completo: ")
    while not validar_nombre(nombre):
        nombre = input("Ingrese su nombre completo: ")

    correo = input("Ingrese su correo electrónico: ")
    while not validar_correo(correo):
        correo = input("Ingrese su correo electrónico: ")

    anio = input("Ingrese su año de nacimiento: ")
    while not validar_anio_nacimiento(anio):
        anio = input("Ingrese su año de nacimiento: ")

    provincia = input("Ingrese la provincia en que vive: ")
    while not validar_provincia(provincia):
        provincia = input("Ingrese la provincia en que vive: ")

    telefono = input("Ingrese su número de teléfono: ")
    while not validar_telefono(telefono):
        telefono = input("Ingrese su número de teléfono: ")

    datos = [nombre, correo, anio, provincia, telefono]
    return datos


# Ejemplo de uso
empleado = ingresar_datos()
print(empleado)
# print(f"Nombre: {nombre}")
