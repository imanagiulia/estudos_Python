# programa que recebe quanto dinheiro uma pessoa tem na carteira e mostre o quantos dolares ela pode comprar

real = float(input('Quantos reais você tem? '))

dolar = real/5.43

print('Com R${} você pode comprar USD{:.2f}'.format(real, dolar))