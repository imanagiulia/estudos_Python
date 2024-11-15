lista = []
while(True):
    num = int(input('Digite um valor: '))
    lista.append(num)
    resp = input('Deseja continuar? [s/n] ').lower()
    if resp == 'n':
        break
lista.sort()
print(f'''Foram digitados {len(lista)} números
A lista ordenada fica assim: {lista}''')
if 5 in lista:
    print('O número 5 aparece na lista!')
else:
    print('O número 5 não está na lista!')