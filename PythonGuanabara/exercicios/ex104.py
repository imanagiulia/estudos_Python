def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            break
        else:
            print(f'\033[31m [ERRO] Digite um número inteiro válido.\033[0m')
    return int(num)


#n = leiaInt('Digite um número: ')
#print(f'Você acabou de digitar o número {n}. ')