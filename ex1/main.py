import random
import pandas as pd # type: ignore
from haversine import Unit, haversine # type: ignore
import json


# Lê e pré-processa o arquivo worldcities.csv, criando uma estrutura com apenas cidades do Paraná
df = pd.read_csv("./worldcities.csv")
pr_cities = df[df.admin_name == 'Paraná'].reset_index(drop=True)

# Prepara o dicionário de conexões
conexoes = {}

# Itera por todas as cidades do DataFrame filtrado
for i, cidade in pr_cities.iterrows():    
    nome_cidade = cidade['city']
    coord_cidade = (cidade['lat'], cidade['lng'])

    # Determina aleatoriamente o número de cidades vizinhas (entre 2 e 6)
    n_vizinhas = random.randint(2, 6)
    
    # Calcula a distância para todas as outras cidades
    distancias = []
    for j, outra_cidade in pr_cities.iterrows():
        if cidade['city'] == outra_cidade['city']:
            continue  # Pular a mesma cidade

        coord_outra_cidade = (outra_cidade['lat'], outra_cidade['lng'])
        # Realiza o cálculo de Haversine para determinar as cidades mais próximas
        distancia = haversine(coord_cidade, coord_outra_cidade, unit=Unit.KILOMETERS)
        distancias.append((outra_cidade['city'], distancia))
    
    # Ordena as cidades pela distância e seleciona as n mais próximas
    distancias.sort(key=lambda x: x[1])
    vizinhas = distancias[:n_vizinhas]
    
    # Adiciona as conexões ao dicionário
    conexoes[nome_cidade] = vizinhas

# Cria arquivo conexoes.json a partir do dicionário de conexões
with open('conexoes.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(conexoes, arquivo_json, indent=4)    