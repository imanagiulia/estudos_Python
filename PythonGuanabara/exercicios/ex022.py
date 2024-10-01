# programa para ler um número e mostrar cada uma das suas posições separadamente

num = input('Digite um número entre 0 e 9999: ')

print('unidade: {}'.format(num[3]))
print('dezena: {}'.format(num[2]))
print('centena: {}'.format(num[1]))
print('milhar: {}'.format(num[0]))