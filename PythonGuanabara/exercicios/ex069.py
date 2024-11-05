
sexo = idade = ''
maior18 = qtdHom = mulherMenor20 = 0

while True:
    print('-' *21)
    print(' CADASTRO DE PESSOAS')
    print('-' *21)
    while (sexo != 'F') and (sexo != 'M'):
        sexo = input('Sexo [M/F]: ').upper().strip()[0]
        if sexo == 'M':
            qtdHom += 1
    while True:
        try:
            idade = int(input('Idade: '))
            if idade > 18:
                maior18 += 1
            if sexo == 'F' and idade < 20:
                mulherMenor20 += 1
            break
        except ValueError:
            print()
    continuar = input('Quer continuar [S/N]: ').upper().strip()[0]
    sexo = ''
    if continuar == 'N':
        print('Programa encerrado!')
        break

print('')

print(f'''Foram cadastrados:
{maior18} pessoas maiores de 18
{qtdHom} homens
{mulherMenor20} mulheres menores de 18''')
