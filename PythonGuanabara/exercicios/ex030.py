distancia = int(input('Digite a distância da sua viagem, em km: '))

if distancia <= 200:
    preço = 0.5 * distancia
    print('O preço da sua pasagem será de R${:.2f}'.format(preço))
else:
    preço = 0.45 * distancia
    print('O preço da sua viagem será de R${:.2f}'.format(preço))
