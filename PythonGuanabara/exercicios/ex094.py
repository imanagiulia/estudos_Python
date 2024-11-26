
pessoa = dict()
grupo = list()
totPessoas = soma = media = 0
while True:
    pessoa['nome'] = input('Nome: ').capitalize()
    pessoa['sexo'] = input('Sexo [F/M]: ').lower()
    while pessoa['sexo'] != 'm' and pessoa['sexo'] != 'f':
        print('[ERRO] Por favor, digite apenas F ou M')
        pessoa['sexo'] = input('Sexo [F/M]: ').lower()
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    resp = input('Quer continuar? [S/N] ').lower()
    grupo.append(pessoa.copy())
    pessoa.clear()
    totPessoas += 1
    while resp != 's' and resp != 'n':
        print('[ERRO] Por favor, digite apenas S ou N')
        resp = input('Quer continuar? [S/N] ').lower()
    if resp == 'n':
        break
media = soma/totPessoas
print(f'Foram cadastradas {totPessoas} pessoas')
print('As mulheres cadastradas foram ', end='')
for m in range(len(grupo)):
    if grupo[m]['sexo'] == 'f':
        print(grupo[m]['nome'], end=', ')
print(f'\nA média de idades cadastradas é {media} anos')
print('Lista das pessoas cuja idade está acima da média: ')
for p in range(len(grupo)):
    if grupo[p]['idade'] > media:
        for k,v in grupo[p].items():
            print(f'  {k} = {v}; ', end='')
        print()