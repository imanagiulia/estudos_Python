# adicionando cores ao python

# - acrescenta no final da linha :\033[style, text, backm
#style :
# 0 - none
# 1 - bold
# 4 -underline
# 7 - negative

# text :
# 30 - branco
# 31 - vermelho
# 32 - verde
# 33 - amarelo
# 34 - azul
# 35 - roxo
# 36 - ciano
# 37 - cinza

# back :
# 40 - branco
# 41 - vermelho
# 42 - verde
# 43 - amarelo
# 44 - azul
# 45 - roxo
# 46 - ciano
# 47 - cinza

print('\033[0;30;41mteste')
print('\033[1;30;43mteste')
print('\033[4;30;44mteste')
print('\033[7;30;47mteste')
print('\033[1;30;42mteste\033[m')
a = 2
b = 3
print('O valor das váriaveis são \033[31m{} \033[m e \033[34m{}\033[m!!!!'.format(a, b))
nome = 'naju'

print('ola me chamo {}{}{}!!!'.format('\033[36m', nome, '\033[m'))
