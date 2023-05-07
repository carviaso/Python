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
validate_province = lambda province: province in ["San Jose", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limon"]

# Función para validar el número de teléfono
validate_phone = lambda phone: str(phone).isdigit() and str(phone).startswith(('2', '4', '6', '7', '8')) and len(str(phone)) == 8
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

# Pedir los datos de contacto y validarlos
# ====================================================
name = get_valid_input("Nombre completo: ", validate_name)
email = get_valid_input("Correo electrónico: ", validate_email)
birthyear = int(get_valid_input("Año de nacimiento: ", lambda year: year.isdigit() and validate_birthyear(int(year))))
province = get_valid_input("Provincia: ", validate_province)
phone = int(get_valid_input("Teléfono: ", validate_phone))

# Imprimir los datos de contacto
# ====================================================
print("Nombre completo:{1}".format(name))
print("Correo electrónico:{1}".format(email))
print("Año de nacimiento: {1}".format(birthyear))
print("Provincia: {1}".format(province))
print("Teléfono: {1}".format(phone))
