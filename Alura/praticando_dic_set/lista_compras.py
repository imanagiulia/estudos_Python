lista_1 = input('Lista 1 (separe por vírgula): ').strip().split(',')
lista_1 = set(lista_1)

lista_2 = input('Lista 2 (separe por vírgula): ').strip().split(',')
lista_2 = set(lista_2)

intersecao_listas = lista_1.intersection(lista_2)
diferenca_lista_1 = lista_1.difference(lista_2)
diferenca_lista_2 = lista_2.difference(lista_1)

print(f'Itens em comum: {intersecao_listas}')
print(f'Itens apenas da lista 1: {diferenca_lista_1}')
print(f'Itens apenas da lista 2: {diferenca_lista_2}')
