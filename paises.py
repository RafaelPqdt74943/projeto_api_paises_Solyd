import json

import requests


URL_ALL = "https://restcountries.com/v3.1/all"
#URL_NAME= "https://restcountries.com/v3.1/name/brasil"

resposta = requests.get(URL_ALL)

paises = json.loads(resposta.text) #parsing de json para python

print(len(paises))

for pais in paises :
    print(pais['name']['common'], pais['currencies'])

