# estudo de tuplas

# As tuplas são inutáveis, não da para mudar enquanto o programa está sendo executado

lanche = 'Hamburger', 'Suco', 'Pizza', 'Pudim'
print(lanche)

print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])

print(lanche[-4])
print(lanche[-3])
print(lanche[-2])
print(lanche[-1])

print(lanche[1:3])
print(lanche[:4])

# lanche[2] = 'Pastel' --> gera erro, não é possivel mudar a tupla fora  de sua declaração

lanche = 'Hamburger', 'Suco', 'Pizza', 'Pudim', 'Pastel' # --> forma que funciona 

print(lanche)

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(len(lanche)):
    print(lanche[cont])

for posição, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posição}')

a = (2, 4, 5)
b = (5, 8, 1, 4)
c = a + b
print(c)
c = b + a 
print(c) 
# A ordem importa

print(c.count(5) # mostra quantas vezes aparece 
print(c.index(8)) # --> mostra a posição

# é possivel ter dados de diferentes tipos nas tuplas

pessoa = ('Ana', 18, 'F', 70.1)
print(pessoa)
