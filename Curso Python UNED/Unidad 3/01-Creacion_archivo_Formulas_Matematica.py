# Caso de estudio 1_Python_IC2023
"""
Universidad Estatal a Distancia (UNED)
Código 71555 - PROGRAMACIÓN BÁSICA CON PYTHON - IC2023
Unidad 2 - Caso de Estudio 1
Estudiante: Carlos Miguel Viales Solórzano
Cédula: 205100311

Trabajo Unidad 3: Proyecto 1 _Python_IC2023
Creacion de archivo con las formulas matematica solicitadas por el usuario.
"""

# importing os module
import math
import os
from datetime import date
import locale

locale.setlocale(locale.LC_ALL, 'es_CR.UTF-8')


# Funciones para el calculo de la Velocidad Angular
def calcular_velocidad_angular(f):
    """Función para resolver fórmula de la velocidad angular (w)
    la formula es:
    W = (2 * 3.14) * f

    F = frecuencia (Hertz)
    """
    # Calcular W usando la fórmula
    w = 2 * math.pi * f

    return w


# Funciones para el calculo de la Periodo(F)
def calcular_Periodo(f):
    """Funcion para calcular Periodo (T)
    La formula es:
        T = 1 / f
    Donde:
        F = frecuencia (Hertz)

    :param f: frecuencia (Hertz)
    :return: T
    """
    # Calcular T usando la fórmula
    periodo = 1 / f

    return periodo


# Funciones para el calculo de la Fuerza Resultante
def Calcular_Fuerza_resultante(masa, aceleracion):
    """Funcion para calcular Frecuencia Resultante
    La formula es:
        FR = m * a
    Donde:
        FR = frecuencia resultante (Hertz)
        M = Masa
        A = Aceleracion

    :param masa: Masa
    :param aceleracion: aceleracion
    :return:
    """
    fr = masa * aceleracion
    return fr


# Funciones para el calculo de la Energia Cinetica
def Calcular_Energía_cinetica(masa, velocidad):
    """
    Funcion para calcular Energía cinética (EC)
    La formula es:
        EC = (0.5 * m) * v^2
    Donde:
        EC = Energía cinética
        M  = Masa
        V  = Velocidad

    :param masa: masa en kg
    :param velocidad: Velocidad en m/s
    :return:
    """
    return (0.5 * masa) * (velocidad ** 2)


# Funciones para el calculo de la Energia Potencial
def Calcular_Energía_Potencial(masa, altura, gravedad):
    """
    Funcion para calcular Energía potencial (EP)
    La formula es:
        EP = m * g * h
    Donde:
        EP = Energía potencial (EP)
        M  = Masa
        G  = Gravedad (9.8)
        H  = Altura

    :param masa: masa en kg
    :param altura: altura
    :param gravedad: gravedad
    :return:
    """
    return masa * gravedad * altura


# Opcion 1
def opcion1():
    # Periodo (T)
    print("\nBienvenido")
    print("Función para resolver fórmula del Periodo (T)")
    print("    La formula es:")
    print("        T = 1 / f")
    print("    Donde:")
    print("        F = frecuencia (Hertz)")

    # Solicitando datos para el calculo
    f: float = float(input("Digite la Frecuencia: "))

    # Calculando
    result: float = calcular_Periodo(f)

    # Mostrando resultado del calculo
    print("Periodo (T) es", result, "\n\n")

    archivo.writelines(
        "tipo: Periodo (T), formula: T = 1 / f, parametros: f es {0}, resultado: {1}\n".format(str(f), str(result)))


# opcion 2
def opcion2():
    # Velocidad angular (w)
    print("\n")
    print("Bienvenido")
    print("Función para resolver fórmula de la velocidad angular (w)")
    print("     La formula es:")
    print("         W = (2 * 3.14) * f")
    print("    Donde:")
    print("        F = frecuencia (Hertz)")

    # Solicitando datos para el calculo
    f: float = float(input("Digite la Frecuencia: "))

    # Calculando
    result: float = calcular_velocidad_angular(f)

    # Mostrando resultado del calculo
    print("El resultado de la Velocidad angular es:", result, "\n\n")

    archivo.writelines("tipo: {0}, formula: {1}, parametros: f es {2}, y resultado: {3}\n".format("Velocidad angular(w)", "W = (2 * 3.14) * f", str(f), str(result)) )


# Opcion 3
def opcion3():
    # Fuerza resultante(FR)
    print("\n")
    print("Bienvenido")
    print("Función para resolver fórmula de la Fuerza resultante (FR)")
    print("     La formula es:")
    print("         FR = m * a")
    print("    Donde:")
    print("         FR = Fuerza resultante")
    print("         M  = Masa")
    print("         A  = Aceleracion")

    # Solicitando datos para el calculo
    m: float = float(input("Digite la Masa: "))
    a: float = float(input("Digite la Aceleración: "))

    # Calculando
    result = Calcular_Fuerza_resultante(masa=m, aceleracion=a)

    # Mostrando resultado del calculo
    print("El resultado de la Fuerza resultante(FR) es", result, "\n\n")

    archivo.writelines(
        "tipo: Fuerza resultante(FR), formula: FR = m * a, parametros: M es {0}; A es {1}, resultado: es {2}\n".format(
            str(m), str(a), str(result)))


# Opcion 4
def opcion4():
    # Energía cinética (EC)
    print("\n")
    print("Bienvenido")
    print("Función para resolver fórmula de la Energía cinética (EC)")
    print("     La formula es:")
    print("         EC = (0.5 * m) * v^2")
    print("    Donde:")
    print("         EC = Energía cinética")
    print("         M = Masa")
    print("         V = Velocidad")

    # Solicitando datos para el calculo
    m: float = float(input("Digite la Masa: "))
    v: float = float(input("Digite la Velocidad: "))

    # Calculando
    result = Calcular_Energía_cinetica(masa=m, velocidad=v)

    # Mostrando resultado del calculo
    print("El resultado de la Energía cinética (EC) es", result, "\n\n")

    archivo.writelines(
        "tipo: Energía cinética (EC), formula: EC = (0.5 * m) * v^2, parametros: M es {0}; V es {1}, resultado: {2}\n".format(
            str(m), str(v), str(result)))


# Opcion 5
def opcion5():
    # Fuerza resultante(FR)
    print("\n")
    print("--")
    print("Función para resolver fórmula de la Energía potencial (EP)")
    print("     La formula es:")
    print("         EP = m * g * h")
    print("    Donde:")
    print("         EP = Energía potencial (EP)")
    print("         M  = Masa en kg")
    print("         G  = Gravedad (9.8) donde gravedad en m/s^2")
    print("         H  = Altura en metros")

    # Solicitando datos para el calculo
    m: float = float(input("Digite la Masa: "))
    h: float = float(input("Digite la Altura: "))
    g: float = float(input("Digite la Gravedad: "))

    # Calculando
    result = Calcular_Energía_Potencial(masa=m, altura=h, gravedad=g)

    # Mostrando resultado del calculo
    print("El resultado de la Energía potencial (EP) es", result, "\n\n")

    archivo.writelines(
        "tipo: Energía potencial (EP), formula: 'EP = m * g * h', parametros: M es {0}; H es {1}; G es {2}, resultado: {3}\n".format(
            str(m), str(h), str(g), str(result)))


# ----------------------------------------------------------------------------------------
# Obtiene el mes en texto
mes_texto = date.today().strftime('%B')

""" Manejo de archivo """
# Solicita el nombre del archivo a crear
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Validar la extensión del archivo
if not nombre_archivo.endswith(".txt"):
    nombre_archivo += ".txt"

#Valida la existencia
if os.path.exists(nombre_archivo):
    respuesta = input("El archivo ya existe. ¿Desea reemplazarlo? (S/N): ")
    if respuesta.lower() != "s":
        print("No se creó el archivo.")
        exit()

archivo = open(nombre_archivo, "w")
print("El archivo se llamará:", nombre_archivo)

# Inicio MENU
while True:
    # Imprimir la fecha de hoy en texto en la consola
    print(date.today().strftime(f'%d de {mes_texto} del %Y'))
    # Información del proyecto
    print("-------------------------------------------------------------")
    print("Universidad Estatal a Distancia (UNED)")
    print("Código 71555 - PROGRAMACIÓN BÁSICA CON PYTHON - IC2023")
    print("Unidad 3 - Caso de Estudio 1")
    print("Estudiante: Carlos Miguel Viales Solórzano")
    print("Cédula: 205100311")
    print("Programa del calculo de operacion y generacion de archivo de texto con las formulas solicitadas.")
    print("-------------------------------------------------------------")

    # Despligue de las opciones de las operaciones
    print("Menú:")
    print("1. Periodo (T)")
    print("2. Velocidad angular (w)")
    print("3. Fuerza resultante (FR)")
    print("4. Energía cinética (EC)")
    print("5. Energía potencial (EP)")
    print("X. Salir")

    opcion: str = input("Elija una opción: ").upper()

    if opcion == "1":
        opcion1()

    elif opcion == "2":
        opcion2()

    elif opcion == "3":
        opcion3()

    elif opcion == "4":
        opcion4()

    elif opcion == "5":
        opcion5()

    elif opcion == "X":
        break
    else:
        print("Opción inválida. Por favor, elija una opción del menú.")


# Cierre del archivo
archivo.close()