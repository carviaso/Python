import sqlite3

# Conectarse a la base de datos (creará una nueva si no existe)
conexion = sqlite3.connect('mi_basededatos.db')

# Crear un objeto cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear una tabla en la base de datos
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nombre TEXT NOT NULL,
                  edad INTEGER NOT NULL)''')

# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()