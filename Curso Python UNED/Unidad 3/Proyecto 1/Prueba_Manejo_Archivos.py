import os


# ------------------------------------------------------------
def open_file_and_display(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")


# ------------------------------------------------------------
def abrir_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("El archivo no existe.")


# ------------------------------------------------------------
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


# ------------------------------------------------------------
def mostrar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")


# ------------------------------------------------------------
def guardar_archivo(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(datos)
        print("Datos guardados correctamente.")


# ------------------------------------------------------------
# Definicion de Main
# ------------------------------------------------------------
def main():
    while True:
        print("1. Abrir archivo\n2. Eliminar cálculo\n3. Mostrar archivo\n4. Guardar información en archivo\n5. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
        
            if opcion == 1:
                nombre_archivo = input("Ingrese el nombre del archivo a abrir: ")
                abrir_archivo(nombre_archivo)

            elif opcion == 2:
                nombre_archivo = input("Ingrese el nombre del archivo: ")
                numero_linea = int(input("Ingrese el número de línea a eliminar: "))
                eliminar_calculo(nombre_archivo, numero_linea)

            elif opcion == 3:
                nombre_archivo = input("Ingrese el nombre del archivo a mostrar: ")
                mostrar_archivo(nombre_archivo)

            elif opcion == 4:
                nombre_archivo = input("Ingrese el nombre del archivo a guardar: ")
                datos = input("Ingrese los datos a guardar: ")
                guardar_archivo(nombre_archivo, datos)

            elif opcion == 5:
                break

            else:
                print("Opción inválida.")
        
        except ValueError:
            print("Valor no valido")


if __name__ == '__main__':
    main()
