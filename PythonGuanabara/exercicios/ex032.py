n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))
n3 = int(input('Digite um outro número: '))

if (n1 > n2 and n1 > n3) and (n2 > n3):
    print('{} foi o maior número digitado e o menor foi {}'.format(n1, n3))
elif (n1 > n2 and n1 > n3) and (n3 > n2):
    print('{} foi o maior número digitado e o menor foi {}'.format(n1, n2))
elif (n2 > n1 and n2 > n3) and (n1 > n3):
    print('{} foi o maior número digitado e o menor foi {}'.format(n2, n3))
elif (n2 > n1 and n2 > n3) and (n3 > n1):
    print('{} foi o maior número digitado e o menor foi {}'.format(n2, n1))
elif (n3 > n1 and n3 > n2) and (n1 > n2):
    print('{} foi o maior número digitado e o menor foi {}'.format(n3, n2))
else:
    print('{} foi o maior número digitado e o menor foi {}'.format(n3, n1))
