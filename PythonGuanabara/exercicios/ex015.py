# programa que lê um número real e mostra apenas sua parte inteira

import math

num = float(input('Digite um número real (ex: 5.523): '))
print('A parte inteira do número digitado é {:.0f}'.format(math.floor(num)))