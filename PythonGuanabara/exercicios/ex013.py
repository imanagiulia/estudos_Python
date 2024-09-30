# programa para converter temperaturas (C para F)

c = float(input("Digite a temperatura em C: "))

f = (c * 1.8) + 32

print('A temperatura de {:.1f}C, corresponde a {:.1f}F'.format(c,f))