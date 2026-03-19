import re

def encontra_palavras_letra_especifica():
    titulo = input('Digite o título do livro: ')
    palavras_titulo = titulo.split()

    letra = input('Digite a letra inicial para pesquisa: ')
    matchs = []

    for palavra in palavras_titulo:
        if re.search(fr'^[{letra}]{{1}}', palavra):
            matchs.append(palavra)

    return matchs

print(encontra_palavras_letra_especifica())