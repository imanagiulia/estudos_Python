# para entrada de dados por meio do usuário utiliza-se a função input
from ExibirVariavel import ativo
from variáveis import codigo, salario

fruta = input("Digite o nome de uma fruta ")
print(fruta)

# input considera o dado como string
# para receber outros tipos de dados temso que converte-los

codigo = int(input("Digite o código do funcionário: "))
nome = input("Digite o nome do funcionario")
salario = float(input("Digite o salário do funcionário"))
ativo = True

print("Código: %d"% codigo)
print("Nome: %s"% nome)
print("Salário: %.2f"% salario)
print("Ativo: %r"% ativo)