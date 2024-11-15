import requests


URL = "https://restcountries.com/v3.1/all"
URL_NAME= "https://restcountries.com/v3.1/name/brasil"

resposta = requests.get(URL)
resposta2=requests.get(URL_NAME)

print(resposta.status_code)
print(resposta.text)

print(resposta2.text)

