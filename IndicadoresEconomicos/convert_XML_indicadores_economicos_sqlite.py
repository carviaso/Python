import xml.etree.ElementTree as ET
import sqlite3

from decimal import Decimal
from datetime import datetime

import time

# Ruta del archivo XML
ruta_archivo = 'dataset.xml'

# Parsear el archivo XML y obtener los datos
tree = ET.parse(ruta_archivo)

# Obtener el elemento raíz del árbol XML
root = tree.getroot()

# Imprimir la etiqueta de la raíz
print(f'root.tag: {root.tag}')

# Buscar elementos por su etiqueta //Datos_de_INGC011_CAT_INDICADORECONOMIC/
elementos = root.findall('.//INGC011_CAT_INDICADORECONOMIC')

"""
# Recorrer los elementos encontrados
for elemento in elementos:
    if elemento.text:
        # Realizar alguna operación con cada elemento
        print(f'elemento.tag: {elemento.tag}')
        cod = elemento.find('COD_INDICADORINTERNO').text
        fecha = elemento.find('DES_FECHA').text
        valor = elemento.find('NUM_VALOR').text
        # ... obtener los demás datos que necesites

        resultado = 'venta' if cod == '317' else 'compra'

        # Imprimir los datos
        print(f'Nombre: {resultado} \t\t Edad:   {fecha} \t\t Valor:  {valor}')
"""

# Conectar a la base de datos SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

print(f'conn status:{conn}')

# Crear la tabla en la base de datos
cursor.execute('CREATE TABLE IF NOT EXISTS CAT_INDICADORECONOMIC (id INTEGER PRIMARY KEY AUTOINCREMENT, COD_INDICADORINTERNO STRING, DES_FECHA DATETIME UNIQUE, NUM_VALOR DECIMAL(10, 2))')


print(f'Cantidad: {len(elementos)}')

# Obtener la cantidad total de elementos
total_elementos = len(elementos) # root.iter()

# Inicializar un contador
contador = 0

print(total_elementos)
# Recorrer los elementos del XML y realizar las inserciones
for elemento in elementos:
    # Incrementar el contador
    contador += 1

    # Realizar las acciones deseadas para cada elemento
    if elemento.text:
        columna1 = elemento.find('COD_INDICADORINTERNO').text

        columna2 = datetime.fromisoformat(elemento.find('DES_FECHA').text)
        columna2b = datetime.strptime( elemento.find('DES_FECHA').text, '%Y-%m-%dT%H:%M:%S%z')

        columna3 = Decimal(elemento.find('NUM_VALOR').text)
        # Formatear el valor decimal como texto
        texto_decimal = "{:.2f}".format(columna3)
        
        # Sentencia SQL de inserción
        sentencia_sql = 'INSERT OR IGNORE INTO CAT_INDICADORECONOMIC (COD_INDICADORINTERNO, DES_FECHA, NUM_VALOR) VALUES (?, ?, ?)'
        try:
            # print(f'columna2 = {columna2} \t columna2b = { columna2 } \t DES_FECHA: {elemento.find("DES_FECHA").text}') 
            # Insertar los datos en la tabla
            cursor.execute(sentencia_sql, (columna1, columna2, texto_decimal))
            
             # Guardar los cambios
            conn.commit()
            
            # print("Inserción exitosa")

        except sqlite3.Error as error:
            print("Error al insertar datos:", error)

        # Calcular el porcentaje de recorrido
        porcentaje_recorrido = (contador / total_elementos) * 100

        # Imprimir el porcentaje de recorrido
        print(f"Porcentaje de recorrido: {porcentaje_recorrido:.2f}%")

# Cerrar la conexión
conn.close()

"""
#############################################
# Recorrer el árbol de elementos
def recorrer_arbol(elemento):
    # Procesar el elemento actual
    print('Elemento:', elemento.tag)
    if elemento.text:
        print('Contenido:', elemento.text)

    # Recorrer los elementos hijos
    for child in elemento:
        recorrer_arbol(child)
        # Hacer una pausa de 3 segundos
        time.sleep(2)
"""

# Llamar a la función de recorrido con el elemento raíz
# recorrer_arbol(root)
#############################################
"""
print(root.text)
print(tree.getroot().text)

print('dataset:')


# Iterar sobre los elementos del DataSet
for dataset in root.findall('.//DataSet'):
    print(f'dataset: {dataset.__len__}')
    # Obtener los datos del DataSet
    for data in dataset.findall('.//INGC011_CAT_INDICADORECONOMIC'):
        cod = data.find('COD_INDICADORINTERNO').text
        fecha = data.find('DES_FECHA').text
        valor = data.find('NUM_VALOR').text
        # ... obtener los demás datos que necesites

        # Imprimir los datos
        print(f'Nombre:{cod}')
        print(f'Edad:  {fecha}')
        print(f'Valor: {valor}')
"""


"""
# Conectar a la base de datos SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Crear la tabla en la base de datos
cursor.execute('CREATE TABLE IF NOT EXISTS CAT_INDICADORECONOMIC (COD_INDICADORINTERNO STRING, DES_FECHA DATETIME, NUM_VALOR DECIMAL(10, 2))')

# Recorrer los elementos del XML y realizar las inserciones
for elemento in root:
    columna1 = elemento.find('COD_INDICADORINTERNO').text
    columna2 = datetime.fromisoformat(elemento.find('DES_FECHA').text)
    columna3 = Decimal(elemento.find('NUM_VALOR').text)
    
    # Insertar los datos en la tabla
    cursor.execute('INSERT INTO CAT_INDICADORECONOMIC VALUES (?, ?, ?)', (columna1, columna2, columna3))

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
"""