lista = listaA = listaB = []
while(True):
    lista.append(int(input('Digite um valor: ')))
    resp = input('Deseja continuar? [s/n] ').lower()
    if resp == 'n':
        break

for cont in range(len(lista)):
    if lista[cont] % 2 == 0:
        listaA.append(lista[cont])
    else:
        listaB.append(lista[cont])
print(f'''Lista original: {lista}
Lista de número PAR: {listaA}
Lista de números ÌMPAR {listaB}''')
