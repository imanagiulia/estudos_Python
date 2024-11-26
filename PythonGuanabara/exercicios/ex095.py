jogador = {}
totGols = 0
gols = []
time = []

while True:
    jogador['nome'] = input('Nome do jogador: ').capitalize()
    qtdJogos = int(input(f'Quantos partidas {jogador['nome']} jogou? '))
    for g in range(qtdJogos):
        gol = int(input(f'Quantos gols na partida {g+1}? '))
        gols.append(gol)
        jogador['gols'] = gols[:]
        totGols += gol
    jogador['total'] = totGols
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    totGols = 0
    resp = input('Deseja continuar? [S/N] ').lower()
    if resp == 'n':
        break
print('No.    NOME     GOLS      TOTAL')
print('=*' *20)
for i in range(len(time)):
    print(i, end='')
    print(f'    {time[i]['nome']:<5}', end='')
    print(f'    {time[i]['gols']}', end='')
    print(f'    {time[i]['total']:<5}', end='')
    print()

while True:
    mostrar = int(input('Mostrar dados de qual jogador (999 para parar): '))

    if mostrar == 999:
        break
    else:
        print(f'  ---- LEVANTAMENTO DO JOGADOR {time[mostrar]['nome']}: ')
        for q in range(len(time[mostrar]['gols'])):
            print(f'No jogo {q+1}, fez {time[mostrar]['gols'][q]} gols')

