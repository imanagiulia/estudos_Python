# comparador de dois números

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

if n1 > n2:
    print('O maior número é {:.1f}'.format(n1))
    print('O menor número é {:.1f}'.format(n2))
elif n2 > n1:
    print('O maior número é {:.1f}'.format(n2))
    print('O menor número é {:.1f}'.format(n1))
else:
    print('Os dois números são iguais')
