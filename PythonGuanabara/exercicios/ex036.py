# conversão de bases

num = int(input('Digite um número inteiro: '))
print('''
[1] BINÁRIA
[2] OCTAL
[4] HEXADÉCIMAL''')
opcao = int(input('Escolha uma das bases para conversão: '))

if opcao == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} convertido para HEXADÉCIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('[ERRO] Opção Inválida!')