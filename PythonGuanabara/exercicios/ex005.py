#programa que mostra o dobro, o triplo e a raiz quadrada de um número

n = int(input('Digite um número: '))

dobro = n*2
triplo = n*3
raizQ = n**(1/2)

print('O dobro de {} é {}.\nO triplo de {} é {}.\nA raiz quadrada de {} é {}'.format(n, dobro, n, triplo, n, raizQ))