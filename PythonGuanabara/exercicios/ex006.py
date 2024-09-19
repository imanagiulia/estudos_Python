#programa para calcular a média entre as duas notas de um aluno

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

media = (n1+n2)/2

print('A média das notas {} e {} é: {:.1f}'.format(n1, n2, media))