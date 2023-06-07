# imports of Libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
# from datetime import *
from dateutil.parser import *

import plotly.express as px

# Load web / WebAPI
#web = f'https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx?WSDL'
web = f'https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx'

# Constantes de tipo de cambio
compra = 317
venta = 318
FechaInicio = '1/11/2022'
FechaFinal = '16/11/2022'
token = '4MIISICGIA'
correo = 'carviaso@gmail.com'

# parametros
ind_econom_func = f'/ObtenerIndicadoresEconomicos?Indicador={compra}&FechaInicio={FechaInicio}&FechaFinal={FechaFinal}&Nombre={compra}&SubNiveles=S&CorreoElectronico={correo}&Token={token}'

response = requests.get(web+ind_econom_func)
content = response.text

print(f'Accesando el web: {web+ind_econom_func}')
# -----------------------------------------------------------------------------------------
#lxml o html o html.parser
soup = BeautifulSoup(content, 'lxml') 

# -----------------------------------------------------------------------------------------
# filtrando los datos
indicadoreconomic = soup.find_all('ingc011_cat_indicadoreconomic')

# -----------------------------------------------------------------------------------------
# definiendo listas
fecha_indic =[]
valor = []

print(f'Cantidad: {len(indicadoreconomic)} de registros.')

for indic in indicadoreconomic:
    des_fecha = indic.find('des_fecha').get_text().strip()
    num_valor = indic.find('num_valor').get_text().strip()
    
    fecha_indic.append(des_fecha)
    valor.append(num_valor)
    
    # print(type(parse(des_fecha)))
    #now = parse(des_fecha)
    
    #print(now)
    #print(f'Fecha : {des_fecha} - num_valor : {num_valor}')    
    #print()

# Generando dicionario
dict_indicadores = {'fecha' : fecha_indic, 'valor' : valor }

# Convirtiendo a DataFrame
df_indicadores = pd.DataFrame(dict_indicadores)

# Creando los datos de indicadores Economicos en CSV
df_indicadores.to_csv('indicadores_economicos_data.csv',index=False, header=True)

print(df_indicadores)

"""
# Plot the scatterplot using Plotly. We ploy y vs x (#Confirmed vs Date)
fig = px.scatter(df_indicadores, x='fecha', y='valor', color='State/UnionTerritory')
fig.update_traces(mode='markers+lines')
fig.show()
"""