from datetime import datetime

pessoa = {}

pessoa['nome'] = input('Nome: ').capitalize()
anoNascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - anoNascimento
pessoa['carteiraTrabalho'] = int(input('Carteira de trabalho (0 se não tem): '))
if pessoa['carteiraTrabalho'] != 0:
    pessoa['anoContratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['anoContratação'] + 35) - datetime.now().year)

for k, v in pessoa.items():
    print(f'{k} é {v}')

