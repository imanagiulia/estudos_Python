numeros = ['', '', '', '']

for c in range(4):
    numeros[c] = int(input(f'Digite o {c+1}° número: '))


print(f'O número 9 apareceu {numeros.count(9)} vez(es)')

if 3 not in numeros:
    print('O valor 3 não aparece em nenhuma posição')
else:
    print(f'O primeiro número 3 apareceu na {numeros.index(3) + 1}° posição')

pares = []

for c in range(4):
    if numeros[c] % 2 == 0:
        pares.append(numeros[c])
print(f'Os valores pares foram {pares}')