# tabuada

n = int(input('De qual número você deseja saber a tabuada: '))

for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, n*c))