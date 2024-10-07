n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))
n3 = int(input('Digite um outro número: '))
menor = n1
maior = n1

if n2 > n3 and n2 > n1:
    maior = n2
elif n3 > n2 and n3 > n1:
    maior = n3
if n2 < n3 and n2 < n1:
    menor = n2
elif n3 < n2 and n3 < n1:
    menor = n3

print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado foi {}'.format(menor))
