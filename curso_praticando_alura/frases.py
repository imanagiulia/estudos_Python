def contar_vogais(frase):
    total_vogal = 0
    frase = frase.lower()

    vogais = ['a', 'e', 'i', 'o', 'u']

    for letra in frase:
        if letra not in vogais:
            continue
        else:
            total_vogal += 1

    return total_vogal

def dectar_palavras_longas(frase):
    frase = frase.split(' ')
    palavras_longas = []

    for palavra in frase:
        if len(palavra) > 10:
            palavras_longas.append(palavra)

    if len(palavras_longas) == 0:
        return 'Nenhuma palavra longa foi encontrada no texto.'
    
    return f'Palavra longas encontradas: {palavras_longas}'


