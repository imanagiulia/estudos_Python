# soma de números impares multiplos de 3 no intervalo 1-500

soma = 0

for c in range(1,500):
    if (c % 2 !=0) and (c % 3 == 0):
        soma += c
print(soma)