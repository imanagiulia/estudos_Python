from exercicios.ex104 import leiaInt


def linha(tam=42):
    return '-' * tam

def cabeçalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    return leiaInt('Sua opção: ')
