# programa que recebe o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('Digite o preço do produto: '))

novoPreco = preco - (preco * 5/100)

print('O preço do produto com 5% de desconto fica R${:.2f}'.format(novoPreco))