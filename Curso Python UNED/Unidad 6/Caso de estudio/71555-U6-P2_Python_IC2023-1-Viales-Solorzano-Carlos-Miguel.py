import openpyxl

from Vuelos import Vuelos

vuelos = []


def lista_vuelos():
    for vuelo in vuelos:
        costo_combustible = vuelo.calcular_costo_combustible()
        print(f"Vuelo {vuelo.num_vuelo}: {costo_combustible} colones")


def generarExcel():
    # Crear un nuevo libro de Excel
    workbook = openpyxl.Workbook()

    # Seleccionar la hoja de trabajo activa
    worksheet = workbook.active

    # Escribir los encabezados de las columnas en la fila 1
    worksheet['A1'] = 'Número de vuelo'
    worksheet['B1'] = 'Ciudad Origen'
    worksheet['C1'] = 'Ciudad Destino'
    worksheet['D1'] = 'Compañía aérea'
    worksheet['E1'] = 'Tipo de aeronave'
    worksheet['F1'] = 'Kilometraje'
    worksheet['G1'] = 'Costo de combustible'

    # Obtener los objetos de la lista de vuelos
    lista_vuelos = vuelos ##[...]  # Aquí se debe poner la lista de objetos de la clase Vuelo

    # Escribir los datos de cada vuelo en una fila nueva
    for i, vuelo in enumerate(lista_vuelos):
        row = i + 2
        worksheet[f'A{row}'] = vuelo.num_vuelo
        worksheet[f'B{row}'] = vuelo.ciudad_origen
        worksheet[f'C{row}'] = vuelo.ciudad_destino
        worksheet[f'D{row}'] = vuelo.compannia
        worksheet[f'E{row}'] = vuelo.tipo_aeronave
        worksheet[f'F{row}'] = vuelo.kilometraje
        worksheet[f'G{row}'] = vuelo.calcular_costo_combustible()

    # Guardar el archivo de Excel
    workbook.save('reporte_vuelos.xlsx')


while True:
    print("----- Menú -----")
    print("1. Registrar vuelo")
    print("2. Lista Vuelos")
    print("3. Generar Excel")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        num_vuelo = input("Número de vuelo: ")
        ciudad_origen = input("Ciudad origen: ")
        ciudad_destino = input("Ciudad destino: ")
        compania = input("Compañía aérea: ")
        tipo_aeronave = input("Tipo de aeronave: ")
        km = float(input("Kilometraje entre punto de inicio y de fin: "))

        vuelo = Vuelos(num_vuelo, ciudad_origen, ciudad_destino, compania, tipo_aeronave, km)
        vuelos.append(vuelo)
        print("Vuelo registrado exitosamente.")
    elif opcion == "2":
        lista_vuelos()
    elif opcion == "3":
        generarExcel()
    elif opcion == "9":
        break
    else:
        print("Opción inválida.")

print("Gracias por usar el sistema.")