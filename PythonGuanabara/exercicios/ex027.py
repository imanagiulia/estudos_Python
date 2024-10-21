from random import randrange

print('Vamos jogar um jogo de adivinhação!!')
print('Você deverá adivinhar um número entre 0 e 5')

num = randrange(0, 5)

chute = int(input('Digite o seu palpite: '))
print('Acertou!' if chute == num else 'Errou!')
