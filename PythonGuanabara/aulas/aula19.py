# DICIONÁRIOS
# estrutura semelhante as listas, porém com eles é possivel dar nome aos indices

# SÃO DECLARADOS  COM {}
dados = {'nome': 'Pedro', 'idade': 25} # OS ÍNDICES SÃO: NOME  E IDADE

print(dados['nome'])
print(dados['idade'])

# COMANDO APPEND NÃO FUNCIONA COM DICIONÁRIOS
dados['sexo'] = 'M'

print(dados)

# PARA REMOVER ELEMENTOS UTILIZA-SE O COMANDO DEL
del dados['idade']

print(dados)

filme ={'título': 'star wars',
        'ano': '1977',
        'diretor': 'George Lucas'
}
catalogo = []
# TITULO, ANO E DIRETOR SÃO CHAMADOS DE KEYS (CHAVES)
print(filme.keys())

# STAR WARS, 1977, GEORGE LUCAS SÃO CHAMADOS DE VALUES (VALOREA)
print(filme.values())

# PARA ACESSAR OS DOIS UTILIZA-SE ITEMS (ITENS)
print(filme.items())

for k,v in filme.items():
    print(f'O {k} é {v}')

# PARA FAZER UMA CÓPIA (FATIAMENTO ) DE  UTILIZA-SE A FUNÇÃO COPY
catalogo.append(filme.copy())
print(catalogo)