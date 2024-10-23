# progressão aritmética

termo1 = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
rep = razao*10
print('Os 10 primeiros termos dessa P.A são:')

for c in range(termo1, rep, razao):
    print(c)