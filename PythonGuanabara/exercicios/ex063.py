n = int(input('Digite um número: ')) - 2
antecessor = 1
ultimo = 1

print('{} - {} - '.format(antecessor, ultimo), end='')
while n != 0:
    aux = ultimo
    proximo = ultimo + antecessor
    ultimo = proximo
    antecessor = aux
    print('{} - '.format(proximo), end='')
    n -= 1