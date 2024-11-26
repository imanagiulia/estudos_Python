from random import randint
from time import sleep

print('=*' *15)
print(f'     PALPITES MEGA SENA')
print('=*' *15)

qtdJogos = int(input('Quantos jogos você deseja que eu gere? '))
print(f'-------- GERANDO {qtdJogos} JOGOS ------------')
palpites = list()
jogo = list()

for l in range(qtdJogos):
    for c in range(6):
        num = randint(1, 60)
        if len(palpites) == 0:
            jogo.append(num)
        else:
            if num not in palpites:
                jogo.append(num)
            else:
                continue
    jogo.sort()
    palpites.append(jogo[:])
    jogo.clear()
for l in range(qtdJogos):
    print(f'Jogo {l+1}: {palpites[l]}')
    sleep(0.5)
print()
print('--------- BOA SORTE! ---------')