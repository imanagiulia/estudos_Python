# Manipulação de strings (cadeias de caracteres)

# fatiamente

frase = 'Olá! Sou a naju e estou aprendendo Python!'
print(frase[11:15]) # primeiro parâmetro é o número que deve iniciar; segundo é um número a mais do que deve terminar

print(frase[:5]) # primeiro parâmetro sem nada significa que irá começar pelo índice 0

print(frase[5:]) # da mesma forma, segundo parâmentro sem nada significa que irá terminar no último índice

print(frase[0:42:2]) # terceiro parâmetro serve para íncidar quantos índices serão pulados a cada impressão

# análise

print(len(frase)) # conta o comprimento da string

print(frase.count('a')) # conta quantos 'a's tem na string, tem limitação pois, nesse caso, irá contar apenas as mínusculas

print(frase.upper().count('O')) # dessa forma contará todos os caracteres 'o', pois a frase foi passada inteiramente para maiusculas. O oposto também serve
print(frase.lower().count('o'))

frase2 = '   naju está aprendendo muito!    '
print(frase2.strip()) # tira os espaços 'inuteis' da esquerda e direita
print(frase2.rstrip()) # tira apenas os espaços da direita
print(frase2.lstrip()) # tira apenas os espaços da esquerda

print(frase.replace('naju', 'Ana Giulia')) # substitui uma palavra por outra, porém não definitivamente
print(frase) # aqui pode-se ver que a string original não foi afetada

print('naju' in frase) # mostra de a palavra 'naju' está na string // retorno booleano
print('Java' in frase)

print(frase.find('naju')) # me mostra a posição que a palavra 'naju' começa

print(frase.split()) # fatia a frase

print(frase.find('a')) # mostra a posição da primeira vez que uma letra foi encontrada
print(frase.rfind('a')) # mostra a posição da última vez que uma letra foi encontrada