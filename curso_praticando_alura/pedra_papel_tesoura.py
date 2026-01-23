import random

def jogar(escolha_user):
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_user.lower()

    escolha_maquina = random.choice(opcoes)
    print(f'Computador escolheu: {escolha_maquina}')

    if escolha_user == 'pedra':
        if escolha_maquina == 'pedra':
            return 'Empate!'
        elif escolha_maquina == 'papel':
            return 'Você perdeu!'
        else:
            return 'Você ganhou!'
    elif escolha_user == 'papel':
        if escolha_maquina == 'papel':
            return 'Empate!'
        elif escolha_maquina == 'tesoura':
            return 'Você perdeu!'
        else:
            return 'Você ganhou!'
    else: # tesoura
        if escolha_maquina == 'tesoura':
            return 'Empate!'
        elif escolha_maquina == 'pedra':
            return 'Você perdeu!'
        else:
            return 'Você ganhou!'