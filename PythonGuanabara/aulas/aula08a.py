#importação de bibliotecas

import math#importa todas as funcionalidades da biblioteca
# from math import sqrt // importa uma funcionalidade em específico
num = int(input('Digiete um número: '))

raiz = math.sqrt(num) #versão import math
#raiz = math = sqrt(num) // versão from import

print('A raiz quadrada de {} é {}'.format(num, raiz))
