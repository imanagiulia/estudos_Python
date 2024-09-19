# programa para calcular o aumento do salário em 15%

sal = float(input('Qual o valor do seu salário atualmente? '))

novoSal = sal + (sal * 15/100)

print('Seu novo salário, com 15% de aumento, será de R${:.2f}'.format(novoSal))