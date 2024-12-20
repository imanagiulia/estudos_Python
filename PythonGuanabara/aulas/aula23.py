# TRATAMENTO DE ERRO

#try:
    #operação
#except:
    #falhou
#else: (opicional)
    #deu certo
#finally: (opicional)
    #vai acontecer sempre independente de erro

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Infelizmente tivemos um problema com os tipos de dados que você digitou! =(')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')