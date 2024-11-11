classificação = 'Botafogo', 'Palmeiras', 'Fortaleza', 'Internacional', 'Flamengo', 'São Paulo', 'Cruzeiro', 'Bahia', 'Vasco da Gama', 'Corinthias', 'Athetico Mineiro', 'Grêmio', 'Vitória', 'Fluminense', 'Criciúma', 'Juventude', 'Red Bull Bragantino', 'Paranaense', 'Cuiabá', 'Goianiense'

print('Os 5 primeiros colocados são:')
for c in range(5):
    print(f' {c+1}° {classificação[c]}')
print('')
print('Os últimos 4 colocados são:')
for c in range(16, 20):
    print(f' {c+1}° {classificação[c]}')
print('')
print('Os times em ordem alfabética: ')
clasAlfabetica = sorted(classificação)
for c in range(20):
    print(f' {clasAlfabetica[c]}')
print('')
print(f'O time Vasco da Gama está na {(classificação.index('Vasco da Gama')) + 1}° posição')


