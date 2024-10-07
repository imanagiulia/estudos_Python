ano = int(input('Digite o ano para saber se ele é bissexto ou não: '))

final = ano // 1 % 100

if final % 4 == 0:
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))
