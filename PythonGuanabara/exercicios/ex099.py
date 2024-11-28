def maior(*num):
    tam = len(num)
    mai = 0
    print('Analisando os valores passados...')
    for valor in num:
        if valor == num[0]:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        print(f'{valor} ', end='')
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')
    print('-=' *15)

maior(1, 3, 4)
maior(1, 3, 5, 4)
maior(2, 9, 4, 5, 7, 1)
maior(2, 7, 0)
maior(1, 2)
maior(5)
maior()