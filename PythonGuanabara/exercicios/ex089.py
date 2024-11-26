sala = list()
aluno = list()
media = soma = 0
while True:
    nome = input('Nome: ').capitalize()
    aluno.append(nome)
    for n in range(2):
        aluno.append(float(input(f'Nota {n+1}: ')))
        soma += aluno[n+1]
    media = soma/2
    soma = 0
    aluno.append(media)
    sala.append(aluno[:])
    aluno.clear()
    resp = input('Deseja adicionar outro aluno? [S/N]: ').lower()
    if resp == 'n':
        print('==' *15)
        break
print('No.  NOME      MÉDIA')
print('-' *30)
for a in range(len(sala)):
    print(f'{a}', end='')
    print(f'   {sala[a][0]:<10} ', end='')
    print(f'   {sala[a][3]} ', end='')
    print()
while True:
    mostrarNota = int(input('Mostrar notas de qual aluno [digite o No. correspondente ao aluno], 999 interrompe o programa: '))
    if mostrarNota == 999:
        break
    else:
        print(f'As notas de {sala[mostrarNota][0]} são [{sala[mostrarNota][1]}, {sala[mostrarNota][2]}]')