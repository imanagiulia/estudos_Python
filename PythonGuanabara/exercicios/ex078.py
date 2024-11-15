valor = []
maior = menor = 0
for c in range(5):
    valor.append(int(input(f'Digite o {c+1}° número: ')))
    if c == 0:
        menor = maior = valor[0]
    else:
        if valor[c] > maior:
            maior = valor[c]
        elif valor[c] < menor:
            menor = valor[c]
if maior == menor:
    print(f'O maior e o menor valor digitados são iguais e foi o valor {maior}. Ele se encontra em todas as posições da lista')
else:
    print(f'''O maior valor digitado foi {maior}, na posição {valor.index(maior)} da lista
O menor valor digitado foi {menor}, na posição {valor.index(menor)} da lista''')