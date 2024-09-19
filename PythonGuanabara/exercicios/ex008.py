# programa que recebe um número e mostra a sua tabuada

n = int(input('Digite um número para saber a sua tabuada: '))

for i in range(11):
    print('{} x {} = {}'.format(n, i, n*i))