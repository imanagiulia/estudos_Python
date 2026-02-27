import csv

nome = input('Digite o nome do aluno: ')
nota = input('Digite a nota do aluno: ')


with open('alunos.csv', 'a') as f:
    escritor = csv.writer(f)
    escritor.writerow([nome, nota])


with open('alunos.csv', 'r') as f:
    leitor = csv.reader(f)
    print('Alunos com nota maior ou igual a 7.0: ')
    for linha in leitor:
        if linha:
            nome_aluno = linha[0]
            nota_aluno = float(linha[1])

            if nota_aluno >= 7:
                print(nome_aluno)