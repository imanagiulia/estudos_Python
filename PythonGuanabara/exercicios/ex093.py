jogador = {}
totGols = 0
gols = []

jogador['nome'] = input('Nome do jogador: ').capitalize()
qtdJogos = int(input(f'Quantos partidas {jogador['nome']} jogou? '))
for g in range(qtdJogos):
    gol = int(input(f'Quantos gols na partida {g+1}? '))
    gols.append(gol)
    jogador['gols'] = gols[:]
    totGols += gol
jogador['total'] = totGols
print('=*' *20)
print(jogador)
print('=*' *20)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=*' *20)
print(f'O jogador {jogador['nome']} jogou {qtdJogos} partidas.')
for i in range(qtdJogos):
    print(f' => Na partida {i+1}, fez {jogador['gols'][i]} gols.')
print(f'Foi um total de {jogador['total']} gols.')