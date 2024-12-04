def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('\033[31mERRO! Preço inválido\033[m')
        else:
            valido = True
            return float(entrada)

