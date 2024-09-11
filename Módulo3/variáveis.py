# variáveis, em python, armazenam endereços de memória e não valores;
# não é necessário declarar as variávies no inicio do código, pode ser feito a qualquer momento;
# não é necessário declarar o tipo da variável;
# tipos básicos: int, float, bool (true or false), str (string);

codigo = 10
salario = 1500.00
nome = 'ana'
situação = True

tipo = type (salario) #retorna o tipo da variável

print(salario)
print(tipo)

#saída concatenada com vírgula
print("Código: ", codigo, "Nome: ", nome,"Salário atual: ", salario)

#saída concatenada com operador + // para isso tem que converter as variáveis que não são strings para string
print("Código: " + str(codigo) + " Nome: " + nome + " Salário atual: " + str(salario))