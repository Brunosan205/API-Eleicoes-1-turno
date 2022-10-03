import requests
import json
import pandas as pd


data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')

data.json()

json_data = json.loads(data.content)

candidato = []
partido = []
votos = []
porcentagem = []

for info in json_data['cand']:
    if info['seq'] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        candidato.append(info['nm'])
        votos.append(info['vap'])
        porcentagem.append(info['pvap'])


df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=[
                                'Candidato', 'Nº Votos', 'Porcentagem'])
print(df_eleicao)