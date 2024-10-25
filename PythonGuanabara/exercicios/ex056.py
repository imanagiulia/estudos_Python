
soma = 0
media = 0
hoMaisVelho = ''
maiorIdaHo = 0
qtdMuMenos20 = 0
for p in range(4):
    print('------- {}° pessoa -------'.format(p+1))
    nome = input('Nome: ').capitalize()
    idade = int(input('Idade: '))
    soma += idade
    sexo = input('sexo [M/F]: ').upper().strip()
    if p == 1 and sexo == 'M':
        maiorIdaHo = idade
        hoMaisVelho = nome
    if sexo == 'M' and idade > maiorIdaHo:
        maiorIdaHo = idade
        hoMaisVelho = nome
    if sexo == 'F' and idade < 20:
        qtdMuMenos20 += 1

media = soma/4
print('A média de idade do grupo é {} anos!'.format(media))
print('O Homem mais velho é {}'.format(hoMaisVelho))
print('A quantidade de mulheres menores de 20 anos é {}'.format(qtdMuMenos20))
