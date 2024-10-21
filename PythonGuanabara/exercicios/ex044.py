# gerenciador de pagamentos

precoNormal = float(input('Digite o preço normal do produto: '))
formaPaga = input('Digite a forma de pagamento: ').lower()

if formaPaga in 'dinheiro cheque ':
    precoFinal = precoNormal - (precoNormal * 10/100)
    print('Você recebeu um desconto de 10%, o produto que custava R${:.2f} sairá por R${:.2f}'.format(precoNormal, precoFinal))
elif formaPaga == 'cartao' or 'cartão':
    precoFinal = precoNormal - (precoNormal * 5/100)
    print('Você recebeu um desconto de 5%, o produto que custava R${:.2f} sairá por R${:.2f}'.format(precoNormal, precoFinal))
elif formaPaga == '2x cartao' or '2x cartão':
    print('O produto sairá por R${:.2f}'.format(precoNormal,))
else:
    precoFinal = precoNormal + (precoNormal * 20/100)
    print('Você recebeu um juros de 20%, o produto que custava R${:.2f} sairá por R${:.2f}'.format(precoNormal, precoFinal))