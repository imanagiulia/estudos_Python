import random

def gerar_senha():
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    especiais = '!@#$%&+/-'
    numeros = '0123456789'

    senha = [
        random.choice(alfabeto).upper(),
        random.choice(alfabeto).lower(),
        random.choice(numeros),
        random.choice(especiais)
    ]

    todos_car = alfabeto.upper() + alfabeto.lower() + numeros + especiais

    senha.extend(random.choices(todos_car, k=8))
    random.shuffle(senha)

    return ''.join(senha)

print(gerar_senha())