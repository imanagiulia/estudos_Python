# FUNÇÕES 2

# interective help
# dá pra por no terminal 'help()' e em seguida digitar a função/biblioteca
# ou utilizar:
help(input)
# ou ainda:
print(print.__doc__)

# docstring - documentação de uma função
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = 1
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim!')


help(contador)

# parâmetros opcionais - faz a função funcionar mesmo se algum dos parâmetros pre-estabelecidos não for informado

def soma(a=0, b=0, c=0):
    s = a+b+c
    print(f'A soma é {s}')

soma(2, 3, 5)
soma(2, 3)
soma(1)
soma()

# retorno de valores

def somar(a=0, b=0, c=0):
    s = a+b+c
    return s

r1 = somar(2,5, 1)
r2 = somar(2, 3)
r3 = somar()

print(f'Os resultados foram {r1}, {r2} e {r3}')