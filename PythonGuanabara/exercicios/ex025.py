frase = input('Digite uma frase: ')

print('Quantidade de "A": {} '.format(frase.upper().count('A')))
print('Posição do primeiro "A": {}'.format(frase.upper().find('A')))
print('Posição do último "A": {}'.format(frase.upper().rfind('A')))
