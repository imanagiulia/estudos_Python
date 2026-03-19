import re

def validar_nome():
    padrao_nome = r'^[A-Z][a-z]+$'
    nome = input('Digite um nome: ')

    resultado = re.search(padrao_nome, nome)

    if resultado:
        return 'Nome válido!'
    else:
        return 'Nome inválido'
    
print(validar_nome())