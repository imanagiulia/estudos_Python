# grupo maioridade
from datetime import date
anoAtual = date.today().year
menorIdade = 0
maiorIdade = 0

for c in range(7):
    n = int(input('Digite o ano de nascimento da pessoa {}: '.format(c+1)))
    if anoAtual - n < 18:
        menorIdade += 1
    else:
        maiorIdade += 1
print('Menores de idade: {}'.format(menorIdade))
print('Maiores de idade: {}'.format(maiorIdade))