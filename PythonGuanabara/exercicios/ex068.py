from random import randint

print('*=' *12)
print('Vamos jogar Par ou Ímpar')
print('*=' *12)

soma = 0
vitorias = 0
while True:
    comp = randint (0, 100)
    usua = int(input('Digite um número: '))
    opUsua = input('Par ou Ímpar? [P/I]: ').strip().upper()[0]

    soma = comp + usua
    result = soma % 2

    print(f'Você jogou {usua} e o computador jogou {comp}. A soma é {soma}, que é ', end='')
    if result == 0:
        print('PAR')
    else:
        print('ÍMPAR')

    if (result == 0 and opUsua == 'P') or (result != 0 and opUsua == 'I'):
        print('Você ganhou, vamos jogar novamente!')
        vitorias += 1
    else:
        print('Você perdeu!')
        break
print(f'Você venceu {vitorias} partida(s)!')
