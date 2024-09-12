A = int(input("Informe um valor para a variável A: "))
B = int(input("Informe um valor para a variável B: "))

if (A>B):
    aux=A;
    A=B;
    B=aux;
print("O valor da variável A agora é:",  A);
print("O valor da variável B agora é: ",  B);


# calculo de media - estrutura composta

nota1 = float(input("Digite a nota 1"))
nota2 = float(input("Digite a nota 2"))

media = (nota1 + nota2)/2

if media >= 7.0:
    print("Aprovado! sua média foi %.2f"% media)
else:
    print("Reprovado! sua média foi %.2f"% media)

# quando há mais de duas condições ituliza-se comando elif