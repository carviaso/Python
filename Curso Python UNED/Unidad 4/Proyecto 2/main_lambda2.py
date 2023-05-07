import re
from datetime import date

# Función para validar el nombre completo
validate_name = lambda name: len(name) > 9

# Función para validar el correo electrónico
validate_email = lambda email: bool(re.match(r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$', email))

# Función para validar la edad
validate_age = lambda year: date.today().year - year >= 18

# Función para validar la provincia
provincias = ["San Jose", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limon"]
validate_province = lambda province: province in provincias

# Función para validar el número de teléfono
validate_phone = lambda phone: bool(re.match(r'^[2|4|6|7|8]\d{7}$', phone))

# Función para pedir y validar los datos de contacto de una persona
def get_contact_info():
    while True:
        name = input("Ingrese su nombre completo: ")
        if not validate_name(name):
            print("El nombre debe tener al menos 10 caracteres.")
            continue

        email = input("Ingrese su correo electrónico: ")
        if not validate_email(email):
            print("El correo electrónico no es válido.")
            continue

        year = int(input("Ingrese su año de nacimiento: "))
        if not validate_age(year):
            print("Debe ser mayor de edad para registrarse.")
            continue

        province = input("Ingrese la provincia en que vive: ")
        if not validate_province(province):
            print("Debe ingresar una provincia válida de Costa Rica.")
            continue

        phone = input("Ingrese su número de teléfono: ")
        if not validate_phone(phone):
            print("El número de teléfono no es válido.")
            continue

        # Si todos los datos son válidos, retornamos un diccionario con ellos
        return {
            "nombre": name,
            "correo": email,
            "año de nacimiento": year,
            "provincia": province,
            "teléfono": phone
        }

# Ejemplo de uso
contact_info = get_contact_info()
print("Los datos de contacto ingresados son:", contact_info)
