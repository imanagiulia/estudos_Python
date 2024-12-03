def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de acordo com a média
    :param n: notas que serão analisadas
    :param sit: situação, opcional
    :return: retorna um dicionário com a quantidade de notas, a maior, a menor, a média e situação(opcional)
    """
    soma = maior = menor =  0
    tot = len(n)
    lista = dict()
    for valor in n:
        if valor == n[0]:
            maior = menor = valor
        else:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
        soma += valor
    media = soma/tot
    if sit:
        if media < 6:
            situacao = 'Ruim'
        elif media == 6:
            situacao = 'Na média'
        else:
            situacao = 'Boa'
        lista = {'Total': tot, 'Maior': maior, 'Menor': menor, 'Média': media, 'Situação': situacao}
    else:
        lista = {'Total': tot, 'Maior': maior, 'Menor': menor, 'Média': media}
    return lista


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)