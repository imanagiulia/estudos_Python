# sorteia um nome entre 4 alunos
from random import randrange

aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')

sorteado = randrange(1, 4)



if sorteado == 1:
    print('O aluno sorteado foi o {}, {}'.format(sorteado, aluno1))
elif sorteado == 2:
    print('O aluno sorteado foi o {}, {}'.format(sorteado, aluno2))
elif sorteado == 3:
    print('O aluno sorteado foi o {}, {}'.format(sorteado, aluno3))
elif sorteado == 4:
    print('O aluno sorteado foi o {}, {}'.format(sorteado, aluno4))
