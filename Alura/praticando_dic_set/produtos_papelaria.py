produtos = {}

while True:
    produto = input('Digite o nome do produto [sair para sair]: ')

    if produto.lower() == 'sair':
        print('Saindo...')
        break

    quantidade = (int(input('Digite a quantidade: '))) 
    produtos[produto] = quantidade

print('Produtos cadastrados: ')
for nome, quantidade in produtos.items():
    print(f'- Nome: {nome} | Quantidade: {quantidade}')

op = input('Deseja alterar a quantidade de algum item? [s/n]').lower().strip()

if op[0] == 's':
    produto_a_atualizar = input('Nome do produto a ser atualizado: ')
    nova_quantidade = int(input('Nova quantidade do produto: '))

    produtos[produto_a_atualizar] = nova_quantidade

    print('Lista atualizada: ')
    for nome, quantidade in produtos.items():
        print(f'- Nome: {nome} | Quantidade: {quantidade}')