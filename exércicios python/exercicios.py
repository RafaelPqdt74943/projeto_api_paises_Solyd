pokemon = {
    "nome": "Pikachu",
    "tipo": "Elétrico",
    "ataques": {
        "ataque_1": "Choque do Trovão",
        "ataque_2": "Cauda de Ferro",
        "ataque_3": "Investida"
    },
    "status": {
        "hp": 35,
        "ataque": 55,
        "defesa": 40
    },
    "evoluções": ["Pichu", "Raichu"]
}

#print(pokemon["ataques"]["ataque_3"]," e " ,pokemon["ataques"]["ataque_1"])

""" for chaves in pokemon.keys():
   print(chaves) """

""" for chave, item in pokemon.items():
    print(f"{chave} : {item} ") """
    
print(pokemon["evoluções"][0])  # Saída: Pichu
print(pokemon["evoluções"][1])  # Saída: Raichu
