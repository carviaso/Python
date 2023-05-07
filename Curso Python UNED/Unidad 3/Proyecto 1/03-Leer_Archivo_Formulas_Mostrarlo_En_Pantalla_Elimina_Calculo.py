# Caso de estudio 1_Python_IC2023
"""
Universidad Estatal a Distancia (UNED)
Código 71555 - PROGRAMACIÓN BÁSICA CON PYTHON - IC2023
Unidad 3 - Proyecto 1
Estudiante: Carlos Miguel Viales Solórzano
Cédula: 205100311
Trabajo Unidad 3: Proyecto 1 - IC2023

Lectura de un archivo
Despligue de las líneas de este y la numeración de cada linea
Elimina linea seleccionada
"""
archivo = "archivo.txt"

import os


# Funcion de la lectura del archivo
def procesar_archivo(nombre_archivo, separador, caracter_a_reemplazar, caracter_nuevo):
    with open(nombre_archivo, 'r') as archivo:
        line_num = 0
        lineas_procesadas = []
        for line_num, linea in enumerate(archivo, 1):
            # Separación de la línea y reemplazo del caracter
            elementos = linea.strip('\n').split(separador)
            elementos = [elem.replace(caracter_a_reemplazar, caracter_nuevo) for elem in elementos]

            # Formateo de la línea procesada con el número de línea
            linea_procesada = f"{line_num}: {separador.join(elementos)}"
            lineas_procesadas.append(linea_procesada)
    return lineas_procesadas


def delete_line(nombre_archivo, numero_linea):
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        with open(nombre_archivo, 'w') as archivo:
            for indice, linea in enumerate(lineas):
                if indice != numero_linea - 1:
                    archivo.write(linea)
    except FileNotFoundError:
        print("El archivo no existe.")
    except IndexError:
        print("El número de línea no es válido.")


while True:
    """ Manejo de archivo """
    # Solicita el nombre del archivo a crear
    archivo = input("Ingrese el nombre del archivo a abrir: ")

    # Validar la extensión del archivo
    if not archivo.endswith(".txt"):
        archivo += ".txt"

    # Verificar si el archivo existe
    if os.path.exists(archivo):
        # Leer el contenido del archivo
        lineas = procesar_archivo(archivo, ':', ',', ';')
        print("El contenido del archivo es:")
        for linea in lineas:
            print(linea)

        # Numero de Linea a eliminar
        respuesta = input("¿Digite El número de línea?: ")
        if respuesta.lower() != "":
            delete_line(archivo, int(respuesta))

        respuesta = input("¿Desea Salir? (S/N): ")
        if respuesta.lower() != "s":
            break
    else:
        print("El archivo no existe. Intente nuevamente.")

# EOF
