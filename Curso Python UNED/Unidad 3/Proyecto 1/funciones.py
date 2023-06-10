"""
Conjunto de funciones
"""
import math
import os


# ---------------------------------------------------------------------------------------------
def calcular_velocidad_angular(f):
    """Función para resolver fórmula de la velocidad angular (w)
    la formula es:
    W = (2 * 3.14) * f

    F = frecuencia (Hertz)
    """
    # Calcular W usando la fórmula
    w = 2 * math.pi * f
    return w


# ---------------------------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------------------------
def imprimir_centro(cadena):
    # Obtener la longitud de la cadena y de la consola
    longitud_cadena = len(cadena)
    longitud_consola = len(str(os.get_terminal_size().columns))

    # Calcular el espacio en blanco necesario antes y después de la cadena
    espacio_en_blanco = (longitud_consola - longitud_cadena) // 2
    espacio_antes = ' ' * espacio_en_blanco
    espacio_despues = ' ' * (longitud_consola - espacio_en_blanco - longitud_cadena)

    # Imprimir la cadena centrada
    print(espacio_antes + cadena + espacio_despues)
