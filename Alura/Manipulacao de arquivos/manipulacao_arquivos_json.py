import json
dados = {
    'nome':'Ana',
    'idade': 19,
    'endereços': ['a','b']
}


# escrevendo em um arquivo .json com a função open
with open('dados.json', 'w') as f:
    json.dump(dados, f)

# leitura
with open('dados.json', 'r') as f:
    dados_lidos = json.load(f)
    print(dados_lidos)