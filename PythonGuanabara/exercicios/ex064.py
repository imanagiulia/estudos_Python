n = ''
soma = 0
qtd = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        soma += n
        qtd += 1

print('''Você digitou {} números.
A soma dos números digitados é {}'''.format(qtd, soma))