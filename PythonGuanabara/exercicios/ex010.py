# progrma que calcula a area da parede e diz a quantidade necessária de tinta. Cada litro de tinta pinta 2m^2

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))

area = largura * altura
qtdTinta = area/2

print('A área da parede é igual à: {:.1f}m².\n Serão necessários {:.1f} litros de tinta'.format(area, qtdTinta))