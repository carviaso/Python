import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET

def leer_xml():
    # Abrir el diálogo de selección de archivo
    filename = filedialog.askopenfilename(filetypes=[("Archivos XML", "*.xml")])
    
    if filename:
        # Cargar el archivo XML
        tree = ET.parse(filename)
        root = tree.getroot()
        
        elementos = root.findall('.//INGC011_CAT_INDICADORECONOMIC')

        # Crear una ventana secundaria
        ventana_resultado = tk.Toplevel(ventana)
        
        # Crear una cuadrícula para mostrar los elementos del XML
        for i, elemento in enumerate(elementos):
            etiqueta = tk.Label(ventana_resultado, text=elemento.tag)
            etiqueta.grid(row=i, column=0)
            
            valor = tk.Label(ventana_resultado, text=elemento.text)
            valor.grid(row=i, column=1)

# Crear la ventana principal
ventana = tk.Tk()

# Botón para seleccionar el archivo XML
boton_seleccionar = tk.Button(ventana, text="Seleccionar archivo XML", command=leer_xml)
boton_seleccionar.grid(row=0, column=0)

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
