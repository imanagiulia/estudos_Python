soma = contador = 0
while True:
    n = int(input('Digite um número [o número 999 encerra o programa]: '))
    if n == 999:
        break
    soma += n
    contador += 1
print(f'Você digitou {contador} números e a soma deles é {soma}.')