from exercicios.ex104 import leiaInt

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
            break
        except KeyboardInterrupt:
            print('\033[31m [ERRO] O usuário preferiu não digitar esse número!\033[m ')
            return 0
        except (ValueError, TypeError):
            print('\033[31m [ERRO] Digite um número real válido!\033[m ')
            continue
        else:
            return num

i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
if r is None:
    r = 0
print(f'O valor inteiro digitado foi {i} e o real foi {r}')