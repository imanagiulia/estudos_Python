velocidade = int(input('Digite a velocidade que o carro está se locomovendo: km/h'))

if velocidade > 80:
    print('Você foi multado!')
    multa = 7 * (velocidade - 80)
    print('O valor da multa é de R${:.2f}'.format(multa))
else:
    print('Você está andando na velocidade permitida! Sem multas.')
