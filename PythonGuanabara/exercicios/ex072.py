numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze','quatorze','quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

output = int(input('Digite um número [0 - 20] para saber como se escreve ele em extenso: '))

while(output < 0 or output > 20):
    print('[ERRO] Número não permitido! Digite novamente')
    output = int(input('Digite um número [0 - 20] para saber como se escreve ele em extenso: '))
print(f'O número {output} em extenso é {numeros[output]}')