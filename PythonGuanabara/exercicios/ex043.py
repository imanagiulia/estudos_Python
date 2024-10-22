# calcular imc

peso = float(input('Digite seu peso, em kg: '))
altura = float(input('Digite sua altura, em metros: '))

imc = peso / (altura* altura)

if imc < 18.5:
    print('Seu IMC é de {:.1f}. Você está abaixo do peso!'.format(imc))
elif imc <= 25:
    print('Seu IMC é de {:.1f}. Você está no peso ideal!'.format(imc))
elif imc <= 30:
    print('Seu IMC é de {:.1f}. Você está acima do peso!'.format(imc))
elif imc <= 40:
    print('Seu IMC é de {:.1f}. Você está obeso!'.format(imc))
else:
    print('Seu IMC é de {:.1f}. Você está com obesidade mórbida!'.format(imc))

