
pessoa = []
grupo = []
maior = menor = 0
while True:
    pessoa.append(input('nome: '))
    pessoa.append(int(input('peso: ')))

    if len(grupo) == 0:
       menor = maior = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    resp = input('Deseja continuar? [S/N] ').lower()
    if resp[0] == 'n':
        break
print(f'Foram cadastradas {len(grupo)} pessoas')
print(f'O maior peso cadastrado foi {maior}kg', end='; Pessoas com esse peso: ')
for p in grupo:
    if p[1] == maior:
        print(f', {p[0]}', end=' ')
print(f'\n O menor peso cadastrado foi {menor}kg', end='; Pessoas com esse peso: ')
for p in grupo:
    if p[1] == menor:
        print(f', {p[0]}', end=' ')