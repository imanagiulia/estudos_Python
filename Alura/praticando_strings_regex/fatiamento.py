def fatiar_palavra(palavra: str):
    palavra.lower().split()
    primeira_parte = palavra[:3]
    ultima_parte = palavra[-3:]
    partes_palavra = [primeira_parte, ultima_parte]

    return partes_palavra

palavra_chave = input('Digite uma palavra chave: ')

partes = fatiar_palavra(palavra_chave)

print(f"Primeira parte: {partes[0]}")
print(f"Última parte: {partes[1]}")
