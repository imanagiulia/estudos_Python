# jokenpô

from random import  randint

# 1 = pedra
# 2 = papel
# 3 = tesoura
print('Vamos jogar Jokenpô!!')

computador = randint(1,3)
usuario = input('Qual sua jogada: ').lower()

if (computador == 1 and usuario == 'pedra') or (computador == 2 and usuario == 'papel') or (computador == 3 and usuario == 'tesoura'):
    if computador == 1:
        print('Minha jogada: PEDRA')
        print('Sua jogada: PEDRA')
    elif computador == 2:
        print('Minha jogada: PAPEL')
        print('Sua jogada: PAPEL')
    else:
        print('Minha jogada: TESOURA')
        print('Minha jogada: TESOURA')
    print('Resultado: EMPATE')
elif computador == 1 and usuario == 'papel':
    print('Minha jogada: PEDRA')
    print('Sua jogada: PAPEL')
    print('Resultado: VOCÊ GANHOU!')
elif computador == 1 and usuario == 'tesoura':
    print('Minha jogada: PEDRA')
    print('Sua jogada: TESOURA')
    print('Resultado: COMPUTADOR GANHOU!')
elif computador == 2 and usuario == 'pedra':
    print('Minha jogada: PAPEL')
    print('Sua jogada: PEDRA')
    print('Resultado: COMPUTADOR GANHOU!')
elif computador == 2 and usuario == 'tesoura':
    print('Minha jogada: PAPEL')
    print('Sua jogada: TESOURA')
    print('Resultado: VOCÊ GANHOU!')
elif computador == 3 and usuario == 'pedra':
    print('Minha jogada: TESOURA')
    print('Sua jogada: PEDRA')
    print('Resultado: COMPUTADOR GANHOU!')
elif computador == 3 and usuario == 'papel':
    print('Minha jogada: TESOURA')
    print('Sua jogada: PAPEL ')
    print('Resultado: VOCÊ GANHOU!')
else:
    print('[ERRO] jogada inválida!')
