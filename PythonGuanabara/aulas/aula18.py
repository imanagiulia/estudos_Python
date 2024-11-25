# listas compostas = listas dentro de outra lista

pessoas = [['Pedro', 12], ['Maria', 67], ['Ana', 19]]

print(pessoas[0][1])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])

teste = list()
teste.append('naju')
teste.append(19)
galera = list()
galera.append(teste[:])
teste[0] = 'Brenda'
teste[1] = 18
galera.append(teste[:])
print(galera)
dado = list()
for c in range(2):
    dado.append(input('nome: '))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)


