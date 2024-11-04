resp = ''
media = 0
c = 0
soma = 0
maior = ''
menor = ''

while resp != 'N':
    n = int(input('Digite um número: '))
    c += 1
    soma += n
    if c == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    media = soma / c
    resp = input('Deseja digitar mais um número: [S/N]').upper()

print('''A média dos núemros digitados é {}
O maior número digitado foi {}
O menor número digitado foi {}'''.format(media, maior, menor))
