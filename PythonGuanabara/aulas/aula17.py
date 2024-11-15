# LISTAS

comidas = ['hamburger', 'pão', 'picolé', 'pudim']
print(comidas)

# PARA ADICIONAR UM ITEM A ESSA LISTA, UTILIZA-SE O COMANDO APPEND

comidas.append('tomate')
print(comidas)

# PARA MODIFICAR O ITEM DE UM DOS INTEX, UTILIZA-SE O SEGUINTE COMANDO:

comidas[2] = 'pizza'
print(comidas)

# PARA ADICIONAR UM ITEM EM UMA DETERMINADA POSIÇÃO, UTILIZA-SE O COMANDO INSERT

comidas.insert(0, 'sushi') # sushi será adicionado na posição 0 e hamburguer passsará a ser na posição 1
print(comidas)

# HÁ VÁRIAS MANEIRAS DE DELETAR ITENS DE UMA LISTA
# EM TODOS OS CASOS AS POSIÇÕES DOS ITENS SERÃO REAJUSTADAS APÓS A AÇÃO DE DELETAR

del comidas[4] # deletará o item da posição 4
print(comidas)

comidas.pop(0) # geralmente deleta o ultimo item, mas pode ser manipulado, assim como foi feito, para deletar o item desejado que nesse caso é 'sushi'
print(comidas)

comidas.remove('pão') #elimina a primeira ocorrencia
print(comidas)

# CRIANDO LISTAS COM RANGE

valores = list(range(5,11)) # estrutura ordenada
print(valores)

valores = [4,3,1,7,8,2] # estrutura não ordenada
print(valores)

# PARA ORDENAR UMA LISTA NAO ORDENADA BASTA UTILIZAR O METODO SORT

valores.sort()
print(valores)

# PARA ORDENAR NA ORDEM REVERSA, UTILIZA-SE O COMANDO REVERSE

valores.sort(reverse=True)
print(valores)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')

a = [1,2,3]
b = a # é uma relação, se eu altero b, a também será alterado
b[2] = 4
print(a,b)

# PARA SE FAZER UMA CÓPIA DE A EM B:
b = a[:] # agora b é uma cópia de a
b[1] = 3
print(a,b)

