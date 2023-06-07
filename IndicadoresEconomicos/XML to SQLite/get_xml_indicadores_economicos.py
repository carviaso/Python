import pandas as pd
import requests
import json


# Load web / WebAPI
web = f'https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx?WSDL'
web = f'https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx'

# Constantes de tipo de cambio
compra = 317
venta = 318
FechaInicio = '1/11/2021'
FechaFinal = '6/6/2023'
token = '4MIISICGIA'
correo = 'carviaso@gmail.com'

# parametros
ind_econom_func = f'/ObtenerIndicadoresEconomicos?Indicador={compra}&FechaInicio={FechaInicio}&FechaFinal={FechaFinal}&Nombre={compra}&SubNiveles=S&CorreoElectronico={correo}&Token={token}'
url = web+ind_econom_func

print(f'URL: {url}')
# print(web+ind_econom_func)

response = requests.get(url)

if response.status_code == 200:
    # Guarda la respuesta en un archivo XML
    with open('dataset.xml', 'w') as xml_file:
        xml_file.write(response.text)
else:
    print('La solicitud no fue exitosa. Código de estado:', response.status_code)

"""
if response.status_code == 200:
    # Extrae el contenido de la respuesta
    #content = response.json()
    content = response.text

    # Guarda el contenido en un archivo JSON
    with open('data.json', 'w') as json_file:
        json.dump(content, json_file)
else:
    print('La solicitud no fue exitosa. Código de estado:', response.status_code)
"""