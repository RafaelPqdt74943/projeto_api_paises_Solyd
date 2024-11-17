import json
import requests

URL_ALL = "https://restcountries.com/v3.1/all"
URL_NAME = "https://restcountries.com/v3.1/name/{name}"

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print(f"Erro na requisição! Código: {resposta.status_code}")
    except requests.RequestException as e:
        print(f"Erro ao fazer requisição em: {url}\nDetalhes: {e}")
    return None

def parsing_json(texto_da_resposta): 
    try:
        return json.loads(texto_da_resposta)
    except json.JSONDecodeError as e:
        print(f"Erro ao fazer parsing do JSON!\nDetalhes: {e}")
    return None

def contagem_de_paises(lista_de_paises):
    return len(lista_de_paises)

def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais["name"]["common"])

def mostrar_populacao(nome_do_pais):
    url = URL_NAME.format(name=nome_do_pais)
    resposta = requisicao(url)
    if resposta:
        lista_de_paises = parsing_json(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print(f"{pais['name']['common']}: {pais['population']}")
        else:
            print("Erro ao processar os dados do país.")
    else:
        print("País não encontrado ou erro na requisição.")
        
def mostrar_moedas(nome_do_pais):
    url = URL_NAME.format(name=nome_do_pais)
    resposta = requisicao(url)
    if resposta:
        lista_de_paises = parsing_json(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print(f"Moedas do país: {pais['name']['common']}")
                moedas = pais.get('currencies', {})
                for codigo, detalhes in moedas.items():
                    print(f"Moeda: {detalhes['name']} (Código: {codigo})")
        else:
            print("Erro ao processar os dados do país.")
    else:
        print("País não encontrado ou erro na requisição.")

if __name__ == "__main__":
    mostrar_populacao('brazil')
    mostrar_moedas('brazil')
