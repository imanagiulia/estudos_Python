import random

def gerar_num():
    num = random.randint(1, 100)
    return num

def adivinhar_numero(chute, num):

    if chute > 100 or chute < 1:
        print('Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.')
        
        
    if chute == num:
        print(f'Parabéns! Você acertou o número: {num}')
        return True
    elif chute > num:
        print(f'Muito alto! Tente novamente: {chute}')
        return False
    else:
        print(f'Muito baixo! Tente novamente: {chute}')
        return False
    



