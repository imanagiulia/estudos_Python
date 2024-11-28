# FUNÇÕES

def mensagem(msg):
    print('=' *30)
    print(msg)
    print('=' *30)


def soma(a, b):
    s = a + b
    print(s)


mensagem('Olá')
soma(2, 3)

# EMPACOTAMENTO

def contador(*num):
    print(num)
    tam = len(num)
    for valor in num:
        print(valor, end='')
        print()
    print(f'recebi os valores {num} e são ao todo {tam} números')


contador(2, 3, 5, 6)
contador(1, 9)
contador(9, 5, 3, 2, 8, 3, 7, 4)

# DESEMPACOTAMENTO

def sum(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


sum(5, 5)
sum(9, 8)


# FUNÇÃO COM LISTAS


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [5, 3, 2, 4]
dobra(valores)
print(valores)