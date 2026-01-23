import calculadora 
import gerenciador_tarefas
import adivinha_num 
from validador_cpf import verificar_numeros_cpf
from frases import contar_vogais, dectar_palavras_longas
from gerador_senha import gerar_senha
from pedra_papel_tesoura import jogar


# Calcular Gorjeta Restaurante
try:
    valor_conta = float(input("Digite o valor da conta: "))
    gorjeta = int(input("Digite a porcentagem da gorjeta: "))

    total_conta, total_gorjeta = calculadora.calcular_gorjeta(valor_conta, gorjeta)

    print(f'Valor da gorjeta: R$ {total_gorjeta:.2f}')
    print(f'Total a pagar: R$ {total_conta:.2f}')
except ValueError:
    print('Erro: Digite apenas números!')

# Verificar CPF
cpf = input('Digite seu CPF: ')
print(verificar_numeros_cpf(cpf))

# Contar vogais em um frase
frase = input('Digite um texto: ')
tot_vogais = contar_vogais(frase)
print(f'O texto contém {tot_vogais} vogais')

# Encontrar palavras longas em um texto
texto = input('Digite um texto: ')
palavras_longas = dectar_palavras_longas(texto)
print(palavras_longas)

# Gerar senha aleatória
print(f'Senha gerada: {gerar_senha()}')

# pedra papel ou tesoura
escolha = input('Escolha: pedra, papel ou tesoura? ')
print(jogar(escolha))

# Jogo adivinhação
try:
    num = adivinha_num.gerar_num()

    while True:
        chute = int(input('Tente adivinhar o número (1 - 100): '))
        jogo = adivinha_num.adivinhar_numero(chute, num)

        if jogo:
            break
except ValueError:
    print("ERRO: Entrada inválida: invalid literal for int() with base 10: 'abc12'")

# Calculadora
try:
    resultado = calculadora.calculadora()
    print(f'Resultado: {resultado}')
except ValueError:
    print('Erro: Entrada inválida. Digite apenas números.')
except ZeroDivisionError:
    print('Erro: Divisão por zero não é permitida.')

# Gerenciador de tarefas
lista = []
gerenciador_tarefas.gerenciador(lista)

# Contador de cédulas únicas de saque
try:
    valor = int(input('Digite o valor do saque: '))
    resultado = calculadora.contador_celulas(valor)

    for valor, qtd in resultado.items():
        print(f'{qtd} de {valor}')

except ValueError:
    print('ERRO: O valor deve ser múltiplo de 2')