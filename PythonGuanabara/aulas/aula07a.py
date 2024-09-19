n = int(input('n1: '))
n2 = int(input('n2: '))
print('A soma de {} e {} é {}'.format(n,n2, n+n2, end=' ')) # o end impede que pule uma linha
print('A divisão de {} por {} é {:.2f}'.format(n, n2, n/n2))
print('A multiplicação de {} e {} é {}'.format(n, n2, n*n2))
print('A divisão inteira de {} e {} é {}'.format(n, n2, n//n2))
print('A potência de {} por {} é {}'.format(n, n2, n**n2))
print('O resto da divisão de {} por {} é {}'.format(n, n2, n%n2))
print('A subtração de {} por {} é {}'.format(n, n2, n-n2))