from datetime import datetime

# Inicio - Funciones lambda para validar cada campo
# ====================================================
# Función para validar el nombre completo
validate_name = lambda name: len(name) > 9

# Función para validar el correo electrónico
validate_email = lambda email: '@' in email and '.' in email.split('@')[1]

# Función para validar la edad
validate_birthyear = lambda year: datetime.now().year - year >= 18


# Función para validar la provincia
#validate_province = lambda province: province in ["San Jose", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limon"]
def validar_provincia(provincia):
    provincias_validas = ["San Jose", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limon"]
    filtro = filter(lambda x: x.lower() == provincia.lower(), provincias_validas)
    if len(list(filtro)) > 0:
        return True
    else:
        return False



# Función para validar el número de teléfono
validate_phone = lambda phone: str(phone).isdigit() and str(phone).startswith(('2', '4', '6', '7', '8')) and len(
    str(phone)) == 8


# ====================================================
# Fin - Funciones lambda para validar cada campo
# ====================================================


# Función para pedir un campo y validar su valor
# ====================================================
def get_valid_input(prompt, validator):
    while True:
        value = input(prompt)
        if validator(value):
            return value
        else:
            print("Error: Valor inválido. Inténtelo de nuevo.")


# ====================================================

print(" ====================================================")
print("71555 - Programación Básica con Python")
print("I Cuatrimestre 2023")
print("Ruta de aprendizaje - Unidad 4")
print(" ---- ")
print("Cedula: 205100311")
print("Carlos Miguel Viales Solorzano")
print(" ====================================================")

# Pedir los datos de contacto y validarlos
# ====================================================
name = get_valid_input("Nombre completo: ", validate_name)
email = get_valid_input("Correo electrónico: ", validate_email)
birthyear = int(get_valid_input("Año de nacimiento: ", lambda year: year.isdigit() and validate_birthyear(int(year))))
#province = get_valid_input("Provincia (San Jose, Alajuela, Cartago, Heredia, Guanacaste, Puntarenas, Limon): ", validate_province)
province = get_valid_input("Provincia (San Jose, Alajuela, Cartago, Heredia, Guanacaste, Puntarenas, Limon): ", validar_provincia)
phone = int(get_valid_input("Teléfono: ", validate_phone))

# Imprimir los datos de contacto
# ====================================================
print("\nLos datos de contacto son:")
print(f"Nombre completo:{name}")
print(f"Correo electrónico:{email}")
print(f"Año de nacimiento: {birthyear}")
print(f"Provincia: {province}")
print(f"Teléfono: {phone}")
