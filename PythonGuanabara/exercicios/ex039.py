# alistamento
from datetime import date
anoNasc = int(input('Digite o ano de seu nascimento: '))

anoAtual = date.today().year
idade = anoAtual - anoNasc
tempoRestante = 18 - idade
atraso = idade - 18


if idade < 18:
    print('Você ainda deve se alistar, porém só daqui {} anos!'.format(tempoRestante))
elif idade > 18:
    print('Você já passou do seu tempo de alistamento! Deveria ter se alistado {} anos atrás.'.format(atraso))
else:
    print('Está na hora de você se alitar!')