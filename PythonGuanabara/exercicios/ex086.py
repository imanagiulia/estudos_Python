matriz = list()
linha = []
coluna = []
for l in range(3):
    for c in range(3):
        coluna.append(int(input(f'Digite o valor {[l]} {[c]} da matriz: ')))
    matriz.append(coluna[:])
    coluna.clear()


for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print('')