from random import randint

números = list()
def sorteia(lista):
    for n in range(5):
        lista.append(randint(1,50))
    print('Sorteando 5 valores da lista: ', end='')
    for i in lista:
        print(f'{i} ', end='')
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            soma += lista[i]
    print(f'Soamndo os valores PARES de {lista}, temos {soma}')

sorteia(números)
somaPar(números)
