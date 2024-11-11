from random import randint
numeros = ['','','','','']
for c in range(5):
    numeros[c] = randint(1, 10)
print(f'Os valores sorteados foram {numeros}')

maior = menor = numeros[0]

for c in range(5):
    if numeros[c] < menor:
        menor = numeros[c]
    elif numeros[c] > maior:
        maior = numeros[c]
print(f'O menor valor sorteado foi {menor}')
print(f'O maior valor sorteado foi {maior}')