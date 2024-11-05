# interrompendo estrutura de repetição WHILE

soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
#print('A soma dos números digitados é {}'.format(soma))
print(f'A soma dos números digitados é {soma}')