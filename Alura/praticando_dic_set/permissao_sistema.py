permissoes_principais = set(input('Permissões principais: ').split(', '))
permissoes_solicitadas = set(input('Permissões solicitadas: ').split(', '))


for solicitacao in permissoes_solicitadas:
    if solicitacao in permissoes_principais:
        permissao = True
    else:
        permissao = False
        break

if permissao:
    print('As permissões solicitadas fazem parte das permissões principais.')
else:
    print('As permissões solicitadas não fazem parte das permissões principais.')

