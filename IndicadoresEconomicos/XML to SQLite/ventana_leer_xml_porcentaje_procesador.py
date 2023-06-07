import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
import psutil

def procesar_xml():
    # Abrir el diálogo de selección de archivo
    filename = filedialog.askopenfilename(filetypes=[("Archivos XML", "*.xml")])
    
    if filename:
        # Cargar el archivo XML
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Procesar el XML y obtener el porcentaje de procesador
        porcentaje_procesador = psutil.cpu_percent()
        
        # Crear una ventana secundaria
        ventana_resultado = tk.Toplevel(ventana)
        
        # Mostrar el porcentaje de procesador en una etiqueta
        etiqueta_porcentaje = tk.Label(ventana_resultado, text=f"Porcentaje de Procesador: {porcentaje_procesador}%")
        etiqueta_porcentaje.pack()

# Crear la ventana principal
ventana = tk.Tk()

# Botón para seleccionar el archivo XML
boton_seleccionar = tk.Button(ventana, text="Seleccionar archivo XML", command=procesar_xml)
boton_seleccionar.pack()

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
