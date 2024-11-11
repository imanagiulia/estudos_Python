palavras = 'ana', 'giulia', 'alexa', 'musica', 'celular'

for c in range(5):
    print(f' \nNa palavra {palavras[c]} temos as vogais: ', end='')
    if 'a' in palavras[c]:
        print('a', end=' ')
    if 'e' in palavras[c]:
        print('e', end=' ')
    if 'i' in palavras[c]:
        print('i', end=' ')
    if 'o' in palavras[c]:
        print('o', end=' ')
    if 'u' in palavras[c]:
        print('u', end=' ')