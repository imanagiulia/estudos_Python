# categoria natação
from datetime import date

anoNasc = int(input('Digite o ano de seu nascimento: '))

anoAtual = date.today().year
idade = anoAtual - anoNasc

if idade <= 9:
    print('CATEGORIA: mirim')
elif idade <= 14:
    print('CATEGORIA: infantil')
elif idade <= 19:
    print('CATEGORIA: junior')
elif idade <= 20:
    print('CATEGORIA: sênior')
else:
    print('CATEGORIA: master')