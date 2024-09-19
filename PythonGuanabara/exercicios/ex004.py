# programa que mostra o antecessor e o sucessor de um número

num = int(input('Digite um núemro para saber o seu sucessor e seu antecessor: '))

ant = num-1
suc = num+1

print('O antecessor de {} é: {}. \nO sucessor de {} é: {}.'.format(num, ant, num, suc))