# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fpdf import FPDF

from Vuelos import Vuelos

vuelos = []
pdf = FPDF()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def agregarVuelo():
    num_vuelo = input("Número de vuelo: ")
    ciudad_origen = input("Ciudad origen: ")
    ciudad_destino = input("Ciudad destino: ")
    compania = input("Compañía aérea: ")
    tipo_aeronave = input("Tipo de aeronave: ")
    km = float(input("Kilometraje entre punto de inicio y de fin: "))

    vuelo = Vuelos(num_vuelo, ciudad_origen, ciudad_destino, compania, tipo_aeronave, km)
    vuelos.append(vuelo)
    print("Vuelo registrado exitosamente.")


def exportarPDF():
    # Agragando Pagina
    pdf.add_page()
    # Establece fuentes negrita
    pdf.set_font("Helvetica", 'B', size=15)
    # Texto Centrado
    pdf.cell(200, 10, txt="Lista de Vuelos", ln=1, align='C')
    # Establece fuentes italica
    pdf.set_font("Helvetica", 'I', size=8)
    # Texto
    line = 3
    for vuelo in vuelos:
        costo_combustible = vuelo.calcular_costo_combustible()
        texto = f"Vuelo {vuelo.num_vuelo}: {costo_combustible} colones"
        pdf.cell(200, 10, txt=texto, ln=line, align='L')
        line = line + 1
        texto = vuelo.descripcion()
        pdf.cell(200, 10, txt=texto, ln=line, align='L')
        line = line + 1

    # Guardando el PDF
    pdf.output("Lista_De_Vuelos.pdf")


def listaVuelos():
    # Texto
    line = 3
    for vuelo in vuelos:
        costo_combustible = vuelo.calcular_costo_combustible()
        texto = f"\nVuelo {vuelo.num_vuelo}: {costo_combustible} colones"
        print(texto)
        print(vuelo.descripcion())


if __name__ == '__main__':
    #print_hi('PyCharm')
    opcionSeleccionada = 0

    while (opcionSeleccionada != 4):
        print("----- Menú -----")
        print("1. Registrar vuelos")
        print("2. Exportar a PDF")
        print("3. Lista Vuelos")
        print("4. Salir")

        print("\n Indique su opción: ")
        try:
            opcionSeleccionada = int(input())
        except ValueError:
            print("Valor no valido")
        else:
            if (opcionSeleccionada == 1):
                agregarVuelo()
            if (opcionSeleccionada == 2):
                exportarPDF()
            if (opcionSeleccionada == 3):
                listaVuelos()

    print("Gracias por usar el sistema.")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
