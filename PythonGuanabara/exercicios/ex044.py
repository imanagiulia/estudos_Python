# gerenciador de pagamentos.

precoNormal = float(input('Digite o preço normal do produto: '))
print('''Formas de pagamento:
[1] à vista dinheiro/pix
[2] à vista cartão
[3] 2x no cartão
[4] 3x ao mais no cartão''')

formaPaga = int(input('Sua opção de pagemento: ').lower())

if formaPaga == 1:
    precoFinal = precoNormal - (precoNormal * 10/100)
    print('Você recebeu um desconto de 10%, o produto que custava R${:.2f} sairá por R${:.2f}'.format(precoNormal, precoFinal))
elif formaPaga == 2:
    precoFinal = precoNormal - (precoNormal * 5/100)
    print('Você recebeu um desconto de 5%, o produto que custava R${:.2f} sairá por R${:.2f}'.format(precoNormal, precoFinal))
elif formaPaga == 3:
    print('O produto sairá por R${:.2f}'.format(precoNormal,))
elif formaPaga == 4:
    precoFinal = precoNormal + (precoNormal * 20/100)
    print('Você recebeu um juros de 20%, o produto que custava R${:.2f} sairá por R${:.2f}'.format(precoNormal, precoFinal))
else:
    print('[ERRO] Opção inválida!')
