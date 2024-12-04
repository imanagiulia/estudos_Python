from utilidadesCeV.modulos import moedas

num = float(input('Digite um número: '))
print(f'O dobro de {moedas.formataMoeda(num)} é {moedas.dobro(num, True)}')
print(f'A metade de {moedas.formataMoeda(num)} é {moedas.metade(num, True)}')
print(f'Aumentando 10%, temos {moedas.aumentar(num, 10, True)}')
print(f'Diminuindo 10%, temos {moedas.diminuir(num, 10, True)}')