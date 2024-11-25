num = [[], []]

for c in range(7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'números PAR digitados: {num[0]}')
print(f'números ÍMPAR digitados: {num[1]}')