# soma de números pares
soma = 0
for c in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if (n % 2 == 0):
        soma += n
print(soma)
