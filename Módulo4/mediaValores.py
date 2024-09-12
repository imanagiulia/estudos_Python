qtd=0
soma=0
media=0
valor= float(input("Digite um valor: "))

while valor > 0.0:
    soma = soma + valor
    qtd = qtd + 1
    valor = float(input("Digite um valor: "))

media = soma/qtd
print("\n total soma: ", soma)
print("\n total de valores digitados: ", qtd)
print("\n media: %.2f"% media)
