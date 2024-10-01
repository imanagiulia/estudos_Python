# programa para calcular o valor do seno, cosseno e tangente de um ângulo

from math import cos, sin, tan, radians

ang = int(input('Digite o valor do Ângulo: '))

print('O cosseno de {}graus é {:.2f}'.format(ang, cos(radians(ang))))
print('O seno de {}graus é {:.2f}'.format(ang, sin(radians(ang))))
print('A tangente de {}graus é {:.2f}'.format(ang, tan(radians(ang))))