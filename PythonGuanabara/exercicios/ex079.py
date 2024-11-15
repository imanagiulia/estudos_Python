valor = []
resp = 'q'
c = 0
while(True):
    num = int(input('Digite um valor: '))
    if num in valor:
        print('Valor duplicado! Não irei adicionar!')
    else:
        valor.append(num)
        print('Valor adicionado com sucesso...')
    while resp not in 'ns':
        resp = input('Deseja continuar [s/n]: ').lower()
    if resp == 'n':
        break
    resp = 'q'
print('=' * 25)
valor.sort()
print(f'Você digitou os valores {valor}')