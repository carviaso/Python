#Imprime todos los ficheros existentes en tu carpeta de Descargas.
import os
ruta_descargas = os.path.join(os.path.expanduser('~'), 'Downloads')

print(ruta_descargas)

path = ruta_descargas #'/ruta/de/la/carpeta'

for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print(file)
