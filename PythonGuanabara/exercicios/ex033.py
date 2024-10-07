sal = float(input('Digite o valor do seu salário atual: '))

if sal > 1250:
    novoSal = sal + (sal * 10/100)
    print('Seu novo salário é de R${:.2f}'.format(novoSal))
elif sal <= 1250:
    novoSal = sal + (sal * 15/100)
    print('Seu novo salário é de R${:.2f}'.format(novoSal)) 
