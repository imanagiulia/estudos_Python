import csv

# escrevendo em um arquivo csv
with open('dados.csv', 'w') as f:
    escritor = csv.writer(f)
    escritor.writerow(['nome', 'idade'])
    escritor.writerow(['Juliana', '41'])    
    escritor.writerow(['Marina', '19'])    


# lendo um arquivo csv
with open('dados.csv', newline='') as f:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)