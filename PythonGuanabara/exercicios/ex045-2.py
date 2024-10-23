from random import randint

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
print('''Qual será sua jogada:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Sua escolha: '))

if computador == jogador:
    print('Resultado: EMPATE!')
elif computador == 0 and jogador == 1:
    print('Resultado: VOCÊ GANHOU!')
elif computador == 0 and jogador == 2:
    print('Resultado: COMPUTADOR GANHOU!')
elif computador == 1 and jogador == 0:
    print('Resultado: COMPUTADOR GANHOU!')
elif computador == 1 and jogador == 2:
    print('Resultado: VOCÊ GANHOU!')
elif computador == 2 and jogador == 0:
    print('Resultado: VOCÊ GANHOU!')
elif computador == 2 and jogador == 1:
    print('Resultado: COMPUTADOR GANHOU!')
else:
    print('[ERRO] Opção inválida')

print('O computador escolheu {}'.format(opcoes[computador]))
print('Você escolheu {}'. format(opcoes[jogador]))
