# é primo?
from math import sqrt
n = int(input('Digite um número para saber se ele é primo: '))
if n <= 1:
    print('Não é primo!')
elif n == 2:
        print('É primo!')
elif n > 2 and n % 2 == 0:
    print('Não é primo!')
else:
    primo = True
    for c in range(2, int(sqrt(n)), 2):
        if n % c == 0:
            primo = False
            break

    if primo:
        print('É primo')
    else: 
        print('Não é primo  ')
