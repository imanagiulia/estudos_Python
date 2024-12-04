from trace import Trace


def formataMoeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def aumentar(n, t, formata=False):
    aum = n + (t/100 * n)
    if formata:
        return formataMoeda(aum)
    else:
        return aum



def diminuir(n, t, formata=False):
    dim = n - (t/100 * n)
    if formata:
        return formataMoeda(dim)
    else:
        return dim


def dobro(n, formata=False):
    if formata:
        return formataMoeda(n*2)
    else:
        return n*2


def metade(n, formata=False):
    if formata:
        return formataMoeda(n/2)
    else:
        return n/2

def resumo(v, au, red):
    msg = ' RESUMO DO VALOR '
    print('-' * (len(msg) * 2))
    print(f'{msg.center(34)}')
    print('-' * (len(msg) * 2))
    print(f'Preço analisado: \t{formataMoeda(v)}')
    print(f'Dobro do preço: \t{dobro(v, True)}')
    print(f'Metade do preço: \t{metade(v, True)}')
    print(f'{au}% de aumento: \t{aumentar(v, au, True)}')
    print(f'{red}% de redução: \t{diminuir(v, red, True)} ')
    print('-' * (len(msg) * 2))
