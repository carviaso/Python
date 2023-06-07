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
        
        # Realizar acciones con el archivo XML
        # Por ejemplo, imprimir los elementos encontrados
        for elemento in root.iter():
            print(elemento.tag, elemento.text)

# Crear la ventana principal
ventana = tk.Tk()

# Botón para seleccionar el archivo XML
boton_seleccionar = tk.Button(ventana, text="Seleccionar archivo XML", command=leer_xml)
boton_seleccionar.pack()

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()