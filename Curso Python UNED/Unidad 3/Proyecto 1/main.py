# Caso de estudio 1_Python_IC2023
"""
Universidad Estatal a Distancia (UNED)
Código 71555 - PROGRAMACIÓN BÁSICA CON PYTHON - IC2023
Unidad 2 - Caso de Estudio 1
Estudiante: Carlos Miguel Viales Solórzano
Cédula: 205100311

Trabajo Unidad 3: Caso de estudio 1 _Python_IC2023
"""

# importing os module
import math
import os
from datetime import date
import locale

locale.setlocale(locale.LC_ALL, 'es_CR.UTF-8')


def calcular_velocidad_angular(f):
    """Función para resolver fórmula de la velocidad angular (w)
    la formula es:
    W = (2 * 3.14) * f

    F = frecuencia (Hertz)
    """
    # Calcular W usando la fórmula
    w = 2 * math.pi * f
    return w


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
    return (0.5 * m) * (v ** 2)


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
    return m * g * h


def imprimir_centro(cadena):
    # Obtener la longitud de la cadena y de la consola
    longitud_cadena = len(cadena)
    longitud_consola = len(str(os.get_terminal_size().columns))

    # Calcular el espacio en blanco necesario antes y después de la cadena
    espacio_en_blanco = (longitud_consola - longitud_cadena) // 2
    espacio_antes = ' ' * espacio_en_blanco
    espacio_despues = ' ' * (longitud_consola - espacio_en_blanco - longitud_cadena)

    print(len(espacio_antes + cadena + espacio_despues))
    print(len(cadena.center(longitud_consola)))
    # Imprimir la cadena centrada
    # print(espacio_antes, cadena, espacio_despues)
    print(cadena.center(longitud_consola, "."))


# print(os.get_terminal_size().columns)

""" Manejo de archivo """
if not os.path.isfile(nombre_archivo):
    archivo = open(nombre_archivo, 'w')
else:
    archivo = open(nombre_archivo, 'a')
    archivo.writelines("\n")

# Obtiene el mes en texto
mes_texto = date.today().strftime('%B')

# Escribir la cadena en el archivo
archivo.writelines("-------------------------------------------------------------\n")
archivo.writelines(date.today().strftime(f'%d de {mes_texto} del %Y'))
archivo.writelines("-------------------------------------------------------------\n")
archivo.writelines("Universidad Estatal a Distancia (UNED)\n")
archivo.writelines("Código 71555 - PROGRAMACIÓN BÁSICA CON PYTHON - IC2023\n")
archivo.writelines("Unidad 3 - Caso de Estudio 1\n")
archivo.writelines("Estudiante: Carlos Miguel Viales Solórzano\n")
archivo.writelines("Cédula: 205100311\n")
archivo.writelines("-------------------------------------------------------------\n")
archivo.writelines("\n")

""" MENU """
while True:
    """ Introdución """
    # Imprimir la fecha de hoy en texto en la consola
    print(date.today().strftime(f'%d de {mes_texto} del %Y'))

    print("-------------------------------------------------------------")
    print("Universidad Estatal a Distancia (UNED)")
    print("Código 71555 - PROGRAMACIÓN BÁSICA CON PYTHON - IC2023")
    print("Unidad 3 - Caso de Estudio 1")
    print("Estudiante: Carlos Miguel Viales Solórzano")
    print("Cédula: 205100311")
    print("-------------------------------------------------------------")
    print("\n")

    print("Menú:")
    print("1. Periodo (T)")
    print("2. Velocidad angular (w)")
    print("3. Fuerza resultante (FR)")
    print("4. Energía cinética (EC)")
    print("5. Energía potencial (EP)")
    print("X. Salir")

    opcion: str = input("Elija una opción: ").upper()

    if opcion == "1":
        # Periodo (T)
        print("\nBienvenido")
        print("Función para resolver fórmula del Periodo (T)")
        print("    La formula es:")
        print("        T = 1 / f")
        print("    Donde:")
        print("        F = frecuencia (Hertz)")
        print("\n")

        # Solicitando datos para el calculo
        f: float = float(input("Digite la Frecuencia: "))

        # Calculando
        result: float = calcular_Periodo(f)

        # Mostrando resultado del calculo
        print("Periodo (T) es", result, "\n\n")

        archivo.writelines("Resolviendo Periodo (T), con la formula T = 1 / f, donde f es " + str(f) + " y el resultado es " + str(result) + "\n")

    elif opcion == "2":
        # Velocidad angular (w)
        print("\n")
        print("Bienvenido")
        print("Función para resolver fórmula de la velocidad angular (w)")
        print("     La formula es:")
        print("         W = (2 * 3.14) * f")
        print("    Donde:")
        print("        F = frecuencia (Hertz)")
        print("\n")

        # Solicitando datos para el calculo
        f: float = float(input("Digite la Frecuencia: "))

        # Calculando
        result: float = calcular_velocidad_angular(f)

        # Mostrando resultado del calculo
        print("El resultado de la Velocidad angular es:", result, "\n\n")

        archivo.writelines(
            "Resolviendo Velocidad angular, con la formula W = (2 * 3.14) * f, donde f es " + str(f) + " y el resultado es " + str(
                result) + "\n")

    elif opcion == "3":
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
        print("\n")

        # Solicitando datos para el calculo
        m: float = float(input("Digite la Masa: "))
        a: float = float(input("Digite la Aceleración: "))

        # Calculando
        result = Calcular_Fuerza_resultante(masa=m, aceleracion=a)

        # Mostrando resultado del calculo
        print("El resultado de la Fuerza resultante(FR) es", result, "\n\n")

        archivo.writelines(
            "Resolviendo Fuerza resultante(FR), con la formula FR = m * a. Donde M es {0} y donde A es {1} y el resultado es {2}\n".format(
                str(m), str(a), str(result)))

    elif opcion == "4":
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
        print("\n")

        # Solicitando datos para el calculo
        m: float = float(input("Digite la Masa: "))
        v: float = float(input("Digite la Velocidad: "))

        # Calculando
        result = Calcular_Energía_cinetica(masa=m, velocidad=v)

        # Mostrando resultado del calculo
        print("El resultado de la Energía cinética (EC) es", result, "\n\n")

        archivo.writelines(
            "Resolviendo Energía cinética (EC), con la formula EC = (0.5 * m) * v^2. Donde M es {0} y donde V es {1} y el resultado es {2}\n".format(
                str(m), str(v), str(result)))

    elif opcion == "5":
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
        print("\n--")

        # Solicitando datos para el calculo
        m: float = float(input("Digite la Masa: "))
        h: float = float(input("Digite la Altura: "))
        g: float = float(input("Digite la Gravedad: "))

        # Calculando
        result = Calcular_Energía_Potencial(masa=m, altura=h, gravedad=g)

        # Mostrando resultado del calculo
        print("El resultado de la Energía potencial (EP) es", result, "\n\n")

        archivo.writelines(
            "Resolviendo Energía potencial (EP), con la formula 'EP = m * g * h'. Donde M es {0}, donde H es {1} y donde G es {2} y el resultado es {3}\n".format(
                str(m), str(h), str(g), str(result)))

    elif opcion == "X":
        archivo.close()
        break
    else:
        print("Opción inválida. Por favor, elija una opción del menú.")
