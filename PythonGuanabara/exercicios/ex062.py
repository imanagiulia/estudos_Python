termo1 = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))

termo10 = termo1 + razao * 10
n = termo1
while n != termo10:
    print('{} - > '.format(n), end='')
    n += razao
op = 1
c = 0
while op != 0:
    print('''\n Deseja saber mais termos?
    se sim: digite a quantidade de termos:
    se não: digite 0''')
    op = int(input('Sua opção: '))

    while c != op:
        print('{} - > '.format(n), end='')
        n += razao
        c += 1
    c = 0

    if op == c:
        print('Programa encerrado!')