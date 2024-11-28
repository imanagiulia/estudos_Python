def area(l, c):
    a = l * c
    print(f'A área de um terreno cuja largura é {l} e o comprimento é {c} é {a}m²')

print('-' *20)
print('CONTROLE DE TERRENOS')
print('-' *20)

larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)