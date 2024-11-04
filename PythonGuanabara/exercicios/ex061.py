termo1 = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))

termo10 = termo1 + razao * 10
n = termo1
while n != termo10:
    print('{} - > '.format(n), end='')
    n += razao
