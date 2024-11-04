sexo = ''
while  (sexo != 'M') and (sexo != 'F'):
    sexo = input('Digite o seu sexo: [M/F]').upper()
    if (sexo != 'M') and (sexo != 'F'):
        print('Modelo de digitação errado! Digite novamente!')