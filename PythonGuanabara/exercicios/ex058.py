from random import randrange

tentativas = 0
chute = ''

print('Vamos jogar um jogo de adivinhação!!')
print('Você deverá adivinhar um número entre 0 e 10')

num = randrange(0, 10)

while chute != num:
    chute = int(input('Digite o seu palpite: '))
    tentativas += 1
    if chute != num:
        print('Errou!')
print('Acertou. Você acertou com {} tentativas '.format(tentativas))