op = 0
maior = 0
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

while op != 5:
    print('''Opcções:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    op = int(input('Sua opção: '))
    if op == 1:
        soma = n1 + n2
        print('A soma entre os números {} e {} é {}'.format(n1, n2, soma))
    if op == 2:
        mult = n1 * n2
        print('A multiplicação entre os números {} e {} é {}'.format(n1, n2, mult))
    if op == 3:
        if n1 > n2:
            maior = n1
            print('Entre os números {} e {}, o maior é {}'.format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print('Entre os números {} e {}, o maior é {}'.format(n1, n2, maior))
        if n1 == n2:
            print('Os números são iguais, portanto nenhum é maior!')
    if op == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    if op == 5:
        print('Fim da execução do programa!')