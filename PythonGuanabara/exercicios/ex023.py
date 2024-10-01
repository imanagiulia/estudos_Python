# programa para ler o nome da cidade e ver se começa com 'santo'

cidade = input('Digite o nome da sua cidade: ')
c = cidade.title().split()
print('Santo' in c[0])