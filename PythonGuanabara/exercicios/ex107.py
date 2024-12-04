from utilidadesCeV.modulos import moedas

num = int(input('Digite um número: '))
print(f'O dobro de R${num} é R${moedas.dobro(num)}')
print(f'A metade de R${num} é R${moedas.metade(num)}')
print(f'Aumentando 10%, temos R${moedas.aumentar(num, 10)}')
print(f'Diminuindo 10%, temos R${moedas.diminuir(num, 10)}')

