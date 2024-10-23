# palindromo

frase = input('Digite uma frase: ').replace(' ', '')

polindromo = False
comp = len(frase) - 1
for c in range(0, comp+1 ):
    if frase[c] == frase[comp]:
        polindromo = True
    else:
        polindromo = False
    comp = comp - 1
if polindromo == True:
    print('É polindromo!')
else:
    print('Não é polindromo!')


