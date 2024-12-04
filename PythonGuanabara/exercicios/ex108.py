from utilidadesCeV.modulos import moedas

num = float(input('Digite um número: '))
print(f'O dobro de {moedas.formataMoeda(num)} é {moedas.formataMoeda(moedas.dobro(num))}')
print(f'A metade de {moedas.formataMoeda(num)} é {moedas.formataMoeda(moedas.metade(num))}')
print(f'Aumentando 10%, temos {moedas.formataMoeda(moedas.aumentar(num, 10))}')
print(f'Diminuindo 10%, temos {moedas.formataMoeda(moedas.diminuir(num, 10))}')