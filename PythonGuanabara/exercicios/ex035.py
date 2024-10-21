# aprovador de emprestimo

valorCasa = float(input('Qual o valor da casa que você deseja comprar: R$'))
sal = float(input('Qual o seu salário atual: R$'))
anos = int(input('Em quantos anos você vai pagar: '))

prestacaoMensal = valorCasa / (anos * 12)

if prestacaoMensal > (sal * (30/100)):
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')