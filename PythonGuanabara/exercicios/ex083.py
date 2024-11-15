listaA = []
listaB = []
exp = input('Digite a expressão: ')

for i in range(len(exp)):
    if exp[i] == '(':
        listaA.append(exp[i])
    elif exp[i] == ')':
        listaB.append(exp[i])

if len(listaA) == len(listaB):
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')