aluno = {'nome': 0, 'media':0, 'situação':0 }
aluno['nome'] = input('Nome: ').capitalize()
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
elif aluno['media'] >= 5 and aluno['media'] <=6:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print(f'''Nome é igual a {aluno['nome']}
Média é igual a {aluno['media']}
Situação é igual a {aluno['situação']}''')

