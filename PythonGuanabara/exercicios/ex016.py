# programa para calcular a hipotenusa de um triângulo

from math import pow, sqrt

COpo = int(input('Digite o valor do cateto oposto: '))
CAdj= int(input('Digite o valor do cateto adjacente: '))

hipoQua = pow(COpo,2) + pow(CAdj,2)

hipo = sqrt(hipoQua)

print('A hipotenusa é igual a {}'.format(hipo))
