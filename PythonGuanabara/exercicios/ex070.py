
print('=' *20)
print('  MERCADO DA NAJU')
print('=' *20)

maisBarato = totalCompra = proMais1000 = 0
nomeProdutoBarato = continuar = ''

while True:
    produto = input('Digite o nome do produto: ')
    preço = float(input('Digite o preço do produto: R$'))
    totalCompra += preço

    if maisBarato == 0 or preço < maisBarato:
        maisBarato = preço
        nomeProdutoBarato = produto

    if preço > 1000:
        proMais1000 += 1

    while continuar != 'S' and continuar != 'N':
        continuar = input('Deseja adicionar outro produto [S/N]: ').upper().strip()[0]
    if continuar == 'N':
        print('----------Programa encerrado----------')
        break
    continuar = ''

print(f'''Seu carrinho possui:
Uma compra no total de R${totalCompra};
{proMais1000} produto(s) acima de R$1000;
O produto mais barato foi {nomeProdutoBarato}''')