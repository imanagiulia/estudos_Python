def calcular_gorjeta(total, porcent):
    porcent = porcent / 100
    gorjeta = total * porcent
    return (total + gorjeta), gorjeta


def calculadora():
    op = int(input("""Qual operação você deseja realizar? 
                   [1] - Soma
                   [2] - Subtração
                   [3] - Multiplicação
                   [4] - Divisão 
                   Sua opção: """))
    match op:
        case 1:
            num_1 = int(input('Digite o primeiro número: ')) 
            num_2 = int(input('Digite o segundo número: ')) 
            return num_1 + num_2
        case 2:
            num_1 = int(input('Digite o primeiro número: ')) 
            num_2 = int(input('Digite o segundo número: ')) 
            return num_1 - num_2
        case 3:
            num_1 = int(input('Digite o primeiro número: ')) 
            num_2 = int(input('Digite o segundo número: ')) 
            return num_1 * num_2
        case 4:
            num_1 = int(input('Digite o primeiro número: ')) 
            num_2 = int(input('Digite o segundo número: ')) 
            return num_1 / num_2
        case _:
            print('Opção inválida!')


def contador_cedulas(valor_saque):
    qtd_notas = {
        'R$ 100': 0, 
        'R$ 50': 0,
        'R$ 20': 0,
        'R$ 10': 0,
        'R$ 5': 0,
        'R$ 2': 0 
    }

    qtd_notas['R$ 100'] = valor_saque // 100
    resto = valor_saque % 100
    
    if resto != 0:
        qtd_notas['R$ 50'] = resto // 50
        resto = resto % 50

    if resto != 0:
        qtd_notas['R$ 20'] = resto // 20
        resto = resto % 20

    if resto != 0:
        qtd_notas['R$ 10'] = resto // 10
        resto = resto % 10

    if resto != 0:
        qtd_notas['R$ 5'] = resto // 5
        resto = resto % 5

    if resto != 0:
        qtd_notas['R$ 2'] = resto // 2
        resto = resto % 2

    print("Cédulas entregues:")
    return qtd_notas
    

