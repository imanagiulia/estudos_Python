
lista = []

for c in range(5):
    num = int(input('Digite um valor: '))

    if not lista or num > lista[-1]:
        lista.append(num)
        print(f'Adicionado na posição {len(lista)}...')
    elif num < lista[0]:
        lista.insert(0, num)
        print('Adicionado na posição 0...')
    else:
        for i in range(len(lista)):
            if lista[i] > num:
                lista.insert(i, num)
                print(f'Adicionado na posição {i}...')
                break
print(f'Os valores digitados, em ordem, foram: {lista}')
