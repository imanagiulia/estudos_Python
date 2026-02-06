texto_1 = set(input("Texto 1: ").lower().strip().split(" "))
texto_2 = set(input("Texto 2: ").lower().strip().split(" "))

intersecao_textos = texto_1.intersection(texto_2)

print(f'Palavras em comum: {intersecao_textos}')