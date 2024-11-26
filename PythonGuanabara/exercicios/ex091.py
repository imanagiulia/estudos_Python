from random import randint
from time import sleep
from operator import itemgetter

sorteio = {}

sorteio['jogador1'] = randint(1,6)
sorteio['jogador2'] = randint(1,6)
sorteio['jogador3'] = randint(1,6)
sorteio['jogador4'] = randint(1,6)
print('VALORES SORTEADOS:')
ranking = dict()
for j, n in sorteio.items():
    print(f'O {j} tirou {n} no dado.')
    sleep(0.5)
ranking = (sorted(sorteio.items(), key=itemgetter(1), reverse=True))
print('=*' *15)
print('RANKING DOS JOGADORES')
for  p,(j, n) in enumerate(ranking):
    print(f'{p+1}° lugar: {j} com {n} pontos')
