# média aluno

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if media < 5:
    print('Aluno REPROVADO!')
elif (media >= 5) and (media <= 5.9):
    print('Aluno EM RECUPERAÇÃO!')
else:
    print('Aluno APROVADO!')