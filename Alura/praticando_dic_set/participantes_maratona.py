participantes = {
    "Mariana": 25, 

    "Carlos": 32, 

    "Beatriz": 28, 

    "Rafael": 35
}

nome_participantes = []
idade_participantes = []

for nome, idade in participantes.items():
    nome_participantes.append(nome)
    idade_participantes.append(idade)

print('Nome dos participantes:  ')
for nome in nome_participantes:
    print(f'{nome}  ', end='')

print('\n Idade dos participantes')
for idade in idade_participantes:
    print(f'{idade} ', end='')

print('\n Participantes e suas idades: ')
for nome, idade in participantes.items():
    print(f'- {nome}: {idade}')