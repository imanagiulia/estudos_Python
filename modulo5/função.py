def ler_notas():
    n = float(input("Digite uma nota : "))
    return n

def resultado (n1, n2):
    media = (n1+n2)/2
    print("Média: %.2f"% media)
    if media >=7.0:
        print("Aprovado!")
    else:
        print("Reprovado!")


a = ler_notas()
b = ler_notas()

resultado(a,b)