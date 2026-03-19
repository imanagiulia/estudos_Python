def padroniza_nome_produto(item: str):
    item_padrao = item.lower().strip()
    return item_padrao

novo_item = padroniza_nome_produto(input('Digite o nome do produto: '))

print(novo_item)


