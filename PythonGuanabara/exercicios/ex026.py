# programa que mostra o primeiro e o último nome de uma pessoa

nome = input('Digite o seu nome completo: ')

n = nome.split()
ultimo = len(n)

print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu último nome é: {}'.format(n[ultimo - 1]))