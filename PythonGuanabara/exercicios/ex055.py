# maior e menor peso

maior = 0
menor = None

for c in range(5):
    peso = float(input('Digite o peso da pessoa {}: '.format(c+1)))
    if peso > maior:
        maior = peso
    if menor == None or peso < menor:
        menor = peso
print('''O maior peso foi: {}
O menor peso foi: {}'''.format(maior, menor))