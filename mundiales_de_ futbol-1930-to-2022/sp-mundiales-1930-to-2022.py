# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 01:49:45 2022

@author: Carlos Viales

https://es.wikipedia.org/wiki/2022_FIFA_World_Cup
https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol_de_2014
https://en.wikipedia.org/wiki/2014_FIFA_World_Cup

BEGIN sp_mundiales_1930_to_2022
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
       1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014,
       2018, 2022]

def get_matches(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    response = requests.get(web)
    content = response.text
    #lxml o html
    soup = BeautifulSoup(content, 'html.parser') 
    
    matches = soup.find_all('div', class_='footballbox')

    home = []
    score = []
    away = []

    print(web)
    for match in matches:
        home.append(match.find('th', class_='fhome').get_text().strip())
        score.append(match.find('th', class_='fscore').get_text().strip())
        away.append(match.find('th', class_='faway').get_text().strip())

    dict_football = {'home': home, 'score': score, 'away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    return df_football

# fifa worldcup histical data
# -- lista de comprension --
fifa = [get_matches(year) for year in years]

df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv('fifa_worldcup_histical_data.csv',index=False)

# fixture data
df_fixture = get_matches(2022)
df_fixture.to_csv('fifa_worldcup_fixture_data.csv', index=False)

df_fifa.to_excel('fifa_worldcup_histical_data.xlsx',header=True)
df_fixture.to_excel('fifa_worldcup_fixture_data.xlsx', header=True)

#end sp_mundiales_1930_to_2022