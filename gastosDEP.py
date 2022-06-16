import requests




url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome'
resp = requests.get(url).json()

for d in resp ['dados']:    
    print (d['nome'], d  ['id'], d['siglaUf'], d['urlFoto'])
