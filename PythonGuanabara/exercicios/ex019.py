# sortear ordem de apresentação entre 4 alunos

import random

aluno1 = input('Digite o nome do aluno 1')
aluno2 = input('Digite o nome do aluno 2')
aluno3 = input('Digite o nome do aluno 3')
aluno4 = input('Digite o nome do aluno 4')

alunos = [aluno1, aluno2, aluno3, aluno4]

ordemApre = random.shuffle(alunos)

print('A ordem de apresentação será: {}'.format(ordemApre))
