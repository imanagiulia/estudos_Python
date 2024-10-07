# estruturas de condicondição

n = int(input('Digite um número: '))

if  n != 1:
    print('o número é  diferente de 1 ')
else:
    print('O número é igual a 1')

# condição simplificada 

ano = int(input('Digite quantos anos o seu carro tem: '))
print('Carro novo' if ano <= 3 else 'Carro velho')
