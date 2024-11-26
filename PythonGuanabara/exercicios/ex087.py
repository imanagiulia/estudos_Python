matriz = list()
coluna = []
somaPar = somaColuna3 = maiorLinha2 = 0
for l in range(3):
    for c in range(3):
        coluna.append(int(input(f'Digite o valor {[l]} {[c]} da matriz: ')))
    matriz.append(coluna[:])
    coluna.clear()


for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        if c + 1 == 3:
            somaColuna3 += matriz[l][c]
        if l + 1 == 2:
            if matriz[l][c] > maiorLinha2:
                maiorLinha2 = matriz[l][c]

    print('')

print('=*' *30)
print(f'A soma dos números PAR digitados é {somaPar};')
print(f'A soma dos números digitados na COLUNA TRÊS é {somaColuna3};')
print(f'O maior valor digitado na LINHA DOIS foi {maiorLinha2}.')
