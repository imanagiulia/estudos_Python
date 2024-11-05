while True:
    n = int(input('Digite um número para saber a sua tabuada [número negativo encerra o programa]: '))
    if n < 0:
        print('Programa encerrado. Volte sempre!')
        break
    for c in range(11):
        print(f'{n} x {c} = {n*c}')
